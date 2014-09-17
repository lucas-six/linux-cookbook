#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Admin Linux (Ubuntu)

    - update_seq_type()
    - shell tools
    - build tools
    - www tools
    - ConfigFile
    - Setup Linux (server)
    - Build Python (Django) projects
  

Copyright 2014 Li Yun <leven.cn@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import sys
import os
import platform
import subprocess
import shutil
import stat
import errno
import configparser
import time
from collections import namedtuple
from collections import OrderedDict
import unittest


## admin error
class AdminError(Exception):
    def __init__(self, e):
        self.error = e

    
    def __str__(self):
        return str(self.error)
            

## Update type of all elements in specific sequence.
#
# @param seq (mutable) sequence to be update
# @param typename target type name
def update_seq_type(seq, typename):
    for index, value in enumerate(seq[:]):
        seq[index] = typename(value)

## Linux shell tools
#
# This module contains functions and classes for Linux shell, including:
#
#   - shell(), chown(), remove(), mkdir(), symlink()
#   - start_init_service(), stop_init_service(), restart_init_service()
#   - read_lines()
#   - eintr_retry()
#   - cpu_cores() (Only /proc supported system)
class shell(object):

    ## Run shell command without output.
    #
    # @param cmd shell command
    # @exception AdminError(subprocess.CalledProcessError) - shell command error
    @staticmethod
    def shell(cmd):
        try:
            subprocess.check_call(cmd, shell=True)
        except subprocess.CalledProcessError as e:
            raise AdminError(e)
            
            
    ## Change owner user and group of the given path.
    #
    # @param path path whose ownership to be changed
    # @param user owner user name or uid
    # @param group owner group name or gid
    # @exception AdminError(ValueError) - both user or group not given
    # @exception AdminError(LookupError) - user or group given not in system
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo chown` error
    @classmethod
    def chown(cls, path, user, group=None):
        group_permission_on = True

        # group name is same as user name by default
        if group is None:
            group = user
            group_permission_on = False

        try:
            # shutil.chown() is high-level interface based onos.chown()
            shutil.chown(path, user, group)
        except (ValueError, LookupError) as e:
            raise AdminError(e)
        except PermissionError:
            cls.shell('sudo chown {0}:{1} {2}'.format(user, group, path))
        
        if os.path.isdir(path):
            if group_permission_on:
                # mode: drwxrwxr-x
                mode = stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH
                try:
                    os.chmod(path, mode)
                except PermissionError:
                    cls.shell('sudo chmod u=rwx,g=rwx,o=rx ' + path)
                    
                    
    ## Remove path entry.
    #
    # @param path path name of entry to be removed
    # @exception AdminError(subprocess.CalledProcessError) - shell 'sudo rm -f' error
    @classmethod
    def remove(cls, path):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        except PermissionError:
            cls.shell('sudo rm -f ' + path)
        except OSError as e:
            # `path` is a directory
            try:
                os.rmdir(path)
            except OSError:
                # not empty directory
                try:
                    shutil.rmtree(path, ignore_errors=True)
                except shutil.Error as e:
                    raise AdminError(e)
                    
                    
    ## Create a directory or directories recursively.
    #
    # @param path directory path
    # @param user owner user name or uid
    # @param group owner group name or gid
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo mkdir` error
    # @exception AdminError(ValueError) - both user or group not given
    # @exception AdminError(LookupError) - user or group given not in system
    # @exception AdminError(subprocess.CalledProcessError) - change ownership error
    #
    # @since Python 3.2
    @classmethod
    def mkdir(cls, path, user=None, group=None):
        try:
            os.makedirs(path, exist_ok=True)
        except PermissionError:
            cls.shell('sudo mkdir -p ' + path)

        # change ownership
        if user is not None:
            cls.chown(path, user, group=group)
            
            
    ## Create a symbolic link pointing to source named `link_name`.
    #
    # @param src source file
    # @param link_name symbolic link name
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo ln -sf` error
    @classmethod
    def symlink(cls, src, link_name):
        try:
            os.symlink(src, link_name)
        except FileExistsError:
            cls.remove(link_name)
            cls.symlink(src, link_name) # re-try
        except PermissionError:
            cls.shell('sudo ln -sf {0} {1}'.format(src, link_name))
            
            
    ## Start init service.
    #
    # @param service service name
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo /etc/init.d` error
    @classmethod
    def start_init_service(cls, service):
        cls.shell('sudo /etc/init.d/{0} start'.format(service))
        
        
    ## Stop init service.
    #
    # @param service service name
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo /etc/init.d` error
    @classmethod
    def stop_init_service(cls, service):
        cls.shell('sudo /etc/init.d/{0} stop'.format(service))
        
        
    ## Restart init service.
    #
    # @param service service name
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo /etc/init.d` error
    @classmethod
    def restart_init_service(cls, service):
        cls.shell('sudo /etc/init.d/{0} restart'.format(service))
            
            
    ## Read specific line(s) with line number(s).
    #
    # @param filename file name
    # @param lineno line number(s) to read (starting with 1)
    # @return generator object of line with no terminating line break
    # @exception TypeError, IOError
    @staticmethod
    def read_lines(filename, lineno):
        if isinstance(lineno, int):
            lineno = [lineno]
                
        with open(filename) as f:
            for n, line in enumerate(f):
                if len(lineno) == 0:
                    break
                if n+1 in lineno:
                    yield line.rstrip('\n') # Remove terminating line break (\n)
                    lineno.remove(n+1) # Reduce size for better performance
            
            
    ## Restart a system call interrupted by `EINTR`.
    #
    # @param func system call
    # @param args arguments of system call
    # @exception socket.error - socket error
    # @exception select.error - select module error
    # @exception OSError - other OS errors
    @staticmethod
    def eintr_retry(func, *args):
        while True:
            try:
                return func(*args)
            except (OSError, socket.error, select.error) as e:
                if e.errno != errno.EINTR:
                    raise
                    
                    
    # Get number of CPU cores from /proc file system.
    #
    # @return number of CPU cores
    # @exception AdminError(subprocess.CalledProcessError) - from `grep` or `/proc/cpuinfo`
    @staticmethod
    def cpu_cores():
        try:
            i = subprocess.check_output('grep "cpu cores" /proc/cpuinfo', shell=True)
        except subprocess.CalledProcessError as e:
            raise AdminError(e)
        return int(i.split(b':')[1].strip())
        
        
## Build tools
#
# This module contains functions and classes for versions, including:
#
#   - Version
#   - decode_version(), match_version()
class build(object):

    Version = namedtuple('Version', 'major, minor, patch')
    
    ## Decode version information string.
    #
    # @param version_info version information string (e.g. Python 3.4.1)
    # @param prefix prefix string of version 
    # @return Version named-tuple
    @classmethod
    def decode_version(cls, version_info, prefix=''):
        # Skip if it already decoded
        if isinstance(version_info, cls.Version):
            return version_info
    
        version_info.strip()
        version_info = version_info[len(prefix):].strip().split('.')
    
        # Change version number from string to integer.
        update_seq_type(version_info, int)
        
        return cls.Version._make(version_info)
        
        
    ## Match the specific version.
    #
    # @param v Version named-tuple
    # @param match version string (e.g. 1.2.3)
    # @return True if match
    @classmethod
    def match_version(cls, v, match):
        v = cls.decode_version(v)
        match = cls.decode_version(match)
        
        if v.major < match.major:
            return False
        
        return (v.major > match.major) \
                or (v.major == match.major and v.minor > match.minor) \
                or (v.minor == match.minor and v.patch >= match.patch)
                
                
    ## Generate documentation for codes under Git by Doxygen.
    #
    # @param path project path
    # @param doxyfile name of Doxygen configuration file
    # @exception subprocess.CalledProcessError
    # @exception IOError
    #
    # @see http://www.stack.nl/~dimitri/doxygen/manual/
    # @since Doxygen 1.8.6
    @staticmethod
    def doxygen(path, doxyfile='Doxyfile.in'):
        # Project path and name
        path = os.path.realpath(path)
        name = os.path.basename(path)
        cur_path = os.getcwd()
        os.chdir(path)
        
        # Project programming language(s)
        exts = set()
        for files in os.walk(path):
            for f in files[2]:
                exts.add(os.path.splitext(f)[1])
            
        # Project version
        version = '0.0.0'
        try:
            versions = subprocess.check_output('git tag', shell=True)
            if len(versions) != 0:
                version = versions.decode()[-1] # latest version
        except subprocess.CalledProcessError as e:
            pass # default version
            
        # Project brief
        brief = ''
        README_file = os.path.join(path, 'README.md')
        try:
            for line in shell.read_lines(README_file, 4):
                brief = line
        except IOError as e:
            pass
        
        # Update Doxygen configuration file
        optimize_for_c = 'NO'
        optimize_for_java_or_python = 'NO'
        if '.c' in exts:
            optimize_for_c = 'YES'
        if {'.java', '.py'} & exts:
            optimize_for_java_or_python = 'YES'
        configs = {'PROJECT_NAME': '\"{0}\"'.format(name),
                'PROJECT_NUMBER': version,
                'PROJECT_BRIEF': '\"{0}\"'.format(brief),
                'OUTPUT_DIRECTORY': 'doc',
                'CREATE_SUBDIRS': 'YES',
                'OPTIMIZE_OUTPUT_FOR_C': optimize_for_c,
                'OPTIMIZE_OUTPUT_JAVA': optimize_for_java_or_python,
                'BUILTIN_STL_SUPPORT': 'YES',
                'TYPEDEF_HIDES_STRUCT': 'YES',
                'SKIP_FUNCTION_MACROS': 'NO',
                'EXTRACT_ALL': 'YES',
                'EXTRACT_PRIVATE': 'YES',
                'EXTRACT_STATIC': 'YES',
                'INPUT': '.',
                'FILE_PATTERNS': '*.py *.c *.h *.cpp *.hh',
                'RECURSIVE': 'YES',
                'SOURCE_BROWSER': 'YES',
                'EXCLUDE_PATTERNS': 'test*',
                'USE_MDFILE_AS_MAINPAGE': 'YES',
                'HTML_TIMESTAMP': 'YES',
                'HTML_DYNAMIC_SECTIONS': 'YES',
                'GENERATE_MAN': 'YES',
                'MAN_LINKS': 'YES'}
        shell.shell('doxygen -g {0}'.format(doxyfile))
        with open(os.path.join(path, doxyfile), 'r+') as f:
            config_file = ConfigFile(f)
            config_file.set(configs)
            
        shell.mkdir(os.path.join(path, 'doc'))
        
        # Generate documentation by Doxygen
        shell.shell('doxygen {0}'.format(doxyfile))
        
        # Back to top directory, NOT project directory
        os.chdir(cur_path)
                
             
## WWW (Internet) tools
#
# This module contains functions and classes for Internet, including:
#
#   - root, uwsgi_root_log
#   - user, group
#   - uwsgi
#   - nginx
class www(object):
    
    root = '/var/spool/www'
    uwsgi_log_root = '/var/log/uwsgi'
    user = 'www-data'
    group = 'adm'
            
    
    ## Setup WWW.
    #
    # @param root root path of WWW
    # @param uwsgi_log_root root path of uWSGI log
    # @param user user of WWW
    # @param group group of WWW
    # @exception AdminError - shell error
    @staticmethod
    def setup(root=None, uwsgi_log_root=None, user=None, group=None):
        if root is None:
            root = www.root
        if uwsgi_log_root is None:
            uwsgi_log_root = www.uwsgi_log_root
        if user is None:
            user = www.user
        if group is None:
            group = www.group
        shell.mkdir(root, user=user, group=group)
        shell.mkdir(uwsgi_log_root, user=user, group=group)
        
        
    ## uWSGI server.
    #
    # @see https://uwsgi.readthedocs.org/en/latest/index.html
    # @since uWSGI 2.0.6
    class uwsgi(object):
    
        ## Run (or Reload) uWSGI server
        #
        # @param app app path
        # @param addr uWSGI server address
        # @param init True for adding to init system
        # @param gateway True for internal gateway
        # @exception AdminError(subprocess.CalledProcessError) - shell error
        # @exception IOError - configuration file error
        #
        # NOTE: Before run uWSGI with Django, make sure that Django project
        # actually works:
        #
        #     python manage.py runserver 0.0.0.0:8000
        #
        # @see https://www.djangoproject.com/
        # @since Django 1.7
        # @since Python 3.2
        @classmethod
        def run(cls, app, addr, init=False, gateway=False):
            is_module = True
            app_split = os.path.splitext(app)
            if app_split[1] == '.py':
                app = app_split[0]
                is_module = False
            app_name = os.path.basename(app)

            app_root = os.path.join(www.root, app_name)
            log_file = os.path.join(www.uwsgi_log_root, app_name) + '.log'
            ini_name = app_name + '.ini'
            ini_file = os.path.join(app_root, ini_name)
            pid_file = cls._pidfile(app_name)
            ini_cmd = 'uwsgi --ini ' + ini_file
            shell.mkdir(app_root)

            # Configure uWSGI server
            config = configparser.ConfigParser(allow_no_value=True)
            config['uwsgi'] = {}            
            if not gateway:
                # HTTP
                config['uwsgi']['http'] = addr
            else:
                # internal communication
                config['uwsgi']['socket'] = addr                
            if is_module:
                # module path
                config['uwsgi']['chdir'] = app
                config['uwsgi']['module'] = '{0}.wsgi'.format(app_name)
            else:
                # app path
                app_path = os.path.realpath(app) + '.py'
                config['uwsgi']['wsgi-file'] = app_path
            config['uwsgi']['uid'] = www.user
            config['uwsgi']['master'] = 'true'
            config['uwsgi']['pidfile'] = pid_file # PID file
            config['uwsgi']['daemonize'] = log_file # log file
            config['uwsgi']['processes'] = str(shell.cpu_cores()) # CPU cores
            config['uwsgi']['max-requests'] = '5000'
            config['uwsgi']['enable-threads'] = 'true'
            config['uwsgi']['limit-as'] = '128' # max memory size
            config['uwsgi']['vacuum'] = 'true' # clear environment on exit
            
            # Write uWSGI configuration
            with open(ini_file, 'w') as f:
                config.write(f)
                
            # Create (Django) site
            if is_module and not os.path.exists(app):
                # create parent directories
                top_dir = os.path.split(app)[0]
                shell.mkdir(top_dir)
                
                # Init Django project
                os.chdir(top_dir)
                shell.shell('django-admin.py startproject ' + app_name)
                os.chdir(app_name)
                shell.shell('python manage.py migrate')
                os.chdir('..')

            # Generate uwsgi init script
            if init:
                tmp_file = '/tmp/uwsgi_{0}.conf'.format(app)
                with open(tmp_file, 'w') as f:
                    f.write('# uwsgi server for {0}\n\
# Generated by admin.py - DONOT edit!!!\n\
\n\
description "uWSGI server for {0}"\n\
\n\
start on socket PROTO=inet PORT={1}\n\
stop on runlevel [!2345]\n\
\n\
exec {2}\n'.format(app, port, ini_cmd))
                shell.shell('sudo mv -u {0} /etc/init/.'.format(tmp_file))
    
            # Run once
            else:
                if os.path.lexists(pid_file):
                    shell.shell('uwsgi --reload ' + pid_file)
                else:
                    shell.shell(ini_cmd)
                    
            
        ## Stop uWSGI server.
        #
        # @param app app path
        # @exception AdminError(subprocess.CalledProcessError) - shell error
        @classmethod
        def stop(cls, app):
            app_name = os.path.splitext(os.path.basename(app))[0]
            pid_file = cls._pidfile(app_name)
            if os.path.exists(pid_file):
                shell.shell('uwsgi --stop ' + pid_file)
                
                
        ## Return uWSGI pid file from app name.
        #
        # @param app app name
        @staticmethod
        def _pidfile(app):
            return '/tmp/uwsgi-{0}.pid'.format(app)
            
            
    ## nginx server.
    #
    # @see http://wiki.nginx.org/Pitfalls
    # @see http://wiki.nginx.org/QuickStart
    # @see http://wiki.nginx.org/Configuration
    # @since nginx 1.4.6
    class nginx(object):
    
        site_avail_root = '/etc/nginx/sites-available'
        site_enable_root = '/etc/nginx/sites-enabled'
        uwsgi_params_url = 'https://raw.githubusercontent.com/nginx/nginx/master/conf/uwsgi_params'
        uwsgi_params_path = '/etc/nginx/uwsgi_params'
    
        ## Setup nginx
        #
        # @param site site path
        # @param port site port number
        # @param name site server name
        # @param upstream upstream host address (uWSGI gateway)
        # @exception IOError - site configuration file error
        # @exception AdminError(subprocess.CalledProcessError) - shell `sudo mv` error
        # @exception AdminError(subprocess.CalledProcessError) - download uwsgi_params file error
        @classmethod
        def enable(cls, site, port=80, name='localhost', upstream=None, proxy=':8080'):
            site_name = site
            site_split = os.path.splitext(site)
            if site_split[1] == '.py':
                site_name = site_split[0]
                is_module = False
            site_name = os.path.basename(site_name)
        
            # Download the `uwsgi_params` file at GitHub.com
            if not os.path.exists(cls.uwsgi_params_path):
                shell.shell('sudo wget -c {0} -O {1}'.format(cls.uwsgi_params_url, cls.uwsgi_params_path))
            
            with open('/tmp/nginx-{0}'.format(site_name), 'w') as f:
                # title
                f.write('# nginx site configuration for {0}\n\
# Generated by admin.py - DONOT edit!!!\n\
\n'.format(site_name))

                # upstream host (uWSGI)
                if upstream is not None:
                    f.write('# upstream host\n\
upstream uwsgi_host {{\n\
\tserver {0}; # deployment on different hosts\n\
\t#server unix:///path/to/site.sock; # deployment on the same host\n\
}}\n\
\n'.format(upstream))

                # basic settings
                f.write('# virtual host\n\
server {{\n\
\tlisten {0} default_server;\n\
\tlisten [::]:{0} default_server ipv6only=on;\n\
\n\
\troot /usr/share/nginx/html;\n\
\tindex index.html index.htm;\n\
\n\
\t# Make site accessible from http://{1}/\n\
\tserver_name {1};\n\
\n\
\tcharset utf-8;\n\
\tclient_max_body_size 75M; # max upload size\n\
\n\
\t# static files requests\n\
\t# Images, CSS, JavaScript, Video, etc.\n\
\tlocation ~ ^/(images|css|js|media|static)/ {{\n\
\t\troot {2};\n\
\t\taccess_log off;\n\
\t\texpires 30d;\n\
\t}}\n\
\n\
\tlocation / {{\n'.format(port, name, os.path.join(www.root, site_name)))
                if upstream is not None:
                    f.write('\t\t# Pass non-static requests to uWSGI gateway\n\
\t\tuwsgi_pass uwsgi_host;\n\
\t\tinclude {0};\n\
\n'.format(cls.uwsgi_params_path))

                f.write('\t\t# First attempt to serve request as file, then\n\
\t\t# as directory, then fall back to displaying a 404.\n\
\t\ttry_files $uri $uri/ =404;\n\
\t\t# Uncomment to enable naxsi on this location\n\
\t\t# include /etc/nginx/naxsi.rules\n\
\t}}\n\
\n\
\t# Only for nginx-naxsi used with nginx-naxsi-ui : process denied requests\n\
\t#location /RequestDenied {{\n\
\t\t#proxy_pass http://127.0.0.1:{0};\n\
\t#}}\n\
\n\
\t#error_page 404 /404.html;\n\
\n\
\t# redirect server error pages to the static page /50x.html\n\
\t#\n\
\t#error_page 500 502 503 504 /50x.html;\n\
\t#location = /50x.html {{\n\
\t\t#root /usr/share/nginx/html;\n\
\t#}}\n\
\n\
\t# deny access to .htaccess files, if Apache\'s document root\n\
\t# concurs with nginx\'s one\n\
\t#\n\
\tlocation ~ /\.ht {{\n\
\t\tdeny all;\n\
\t}}\n\
}}\n'.format(proxy))
            shell.shell('sudo mv -u /tmp/nginx-{0} {1}'.format(site_name, cls._site_avail_path(site_name)))
            
            # Setup and run uWSGI gateway
            if upstream is not None:
                www.uwsgi.run(site, upstream, gateway=True)
            
            shell.symlink(cls._site_avail_path(site_name), cls._site_enable_path())
            
            # Restart nginx server
            shell.restart_init_service('nginx')
            
            
        ## Disable nginx server
        #
        # @param site site path
        # @param upstream upstream host address (uWSGI gateway)
        # @exception AdminError(subprocess.CalledProcessError) - shell `sudo ln -sf` or `sudo /etc/init.d` error
        @classmethod
        def disable(cls, site=None, upstream=None):
            shell.remove(cls._site_enable_path())
            
            # Stop uWSGI gateway
            if upstream is not None:
                www.uwsgi.stop(site)
                
            # Restart nginx server
            shell.restart_init_service('nginx')
        
        
        ## Return path of available site by name
        #
        # @param site_name site name
        # @return path of given site
        @classmethod
        def _site_avail_path(cls, site_name):
            return os.path.join(cls.site_avail_root, site_name)
        
       
        ## Return path of enabled site by name
        #
        # @param site_name site name
        # @return path of given site
        @classmethod
        def _site_enable_path(cls, site_name=None):
            if site_name is None:
                site_name = 'default'
            return os.path.join(cls.site_enable_root, site_name)
            

def _setup(quick=False):
    '''Setup Linux.
    
    @param quick True if quick setup.
    @todo Git under Proxy
    '''
    # Determine current system type
    sys_type = platform.system()
    if sys_type == 'Linux':
        linux_distribution = platform.linux_distribution()
        sys_type += ('/' + linux_distribution[0])
        if sys_type.endswith('Ubuntu'):  # Linux/Ubuntu
            if float(linux_distribution[1]) >= 14.04:
                # Ubuntu 14.04 specific features here
                pass
    else:
        sys.exit('Unsupported system {0}'.format(sys_type))
        
    if sys_type.endswith('Ubuntu'):
        # Install/Update core packages
        try:
            # Skip updating index files of package system to reduce
            # testing time.
            if not quick:
                shell.shell('sudo apt-get update')

            pkgs = ['sudo', 'apt', 'apt-utils', \
                    'bash', 'python', 'coreutils', \
                    'vim', 'git', 'doxygen', 'wget', \
                    'nginx', 'build-essential', 
                    'python-pip', 'python-dev', 'python-virtualenv']
            pip_pkgs = ['Django', 'uwsgi']
            shell.shell('sudo apt-get install ' + ' '.join(pkgs))
            
            # Skip updating pip packages to reduce testing time.
            if not quick:
                for p in pip_pkgs:
                    shell.shell('sudo pip install --upgrade ' + p)
        except AdminError as e:
            sys.exit('Failed to install core packages: {0}'.format(e))
        print('System updated [OK]')
            
        vimrc_ok = False
        git_ok = False
            
        # Symbolic link vimrc, backup it if already existing.
        print('\n*** vimrc ***')
        vimrc = os.path.expanduser('~/.vimrc')
        try:
            if os.path.lexists(vimrc):
                old_vimrc = vimrc + '.old'
                shell.remove(old_vimrc)
                os.rename(vimrc, old_vimrc)
            myvimrc = os.path.join(os.getcwd(), '_setup', 'vimrc')
            shell.symlink(myvimrc, vimrc)
            vimrc_ok = True
            print('Vimrc [OK]')
        except OSError as e:
            print('Vimrc [FAILED]: {0}'.format(e), file=sys.stderr)
            
        # Configure bashrc
        def _set_EDITOR_to_Vim(vim_ok):
            try:
                with open(os.path.expanduser('~/.bashrc'), 'a') as f:
                    if vimrc_ok:
                        # Set default editor to Vim
                        f.write('\nexport EDITOR=vim')
                        print('Set default editor to Vim [OK]')
                    shell.shell('. ~/.bashrc')
            except IOError as e:
                print('Failed to set default editor to Vim: {0}'.format(e), file=sys.stderr)
            except subprocess.CalledProcessError as e:
                print('Failed to reload bashrc: {0}'.format(e), file=sys.stderr)

        try:
            if os.environ['EDITOR'] != 'vim':
                _set_EDITOR_to_Vim(vim_ok)
        except KeyError:
            _set_EDITOR_to_Vim(vim_ok)
                        
        # Configure Git
        #
        # @see http://www.git-scm.com/book/
        # @see http://gitref.org/
        # @since Git 1.7
        print('\n*** Git ***')
        def _git_config(conf):
            shell.shell('git config ' + conf)
        def _git_config_global(conf):
            _git_config('--global '+conf)

        try:
            _git_config_global('core.eol lf')
            _git_config_global('core.autocrlf input')
            _git_config_global('core.fileMode false')
            _git_config_global('core.ui auto')
            if vimrc_ok:
                _git_config_global('core.editor vim')
                _git_config_global('diff.tool vimdiff')
                _git_config_global('merge.tool vimdiff')
                
            git_version = subprocess.check_output('git version', shell=True)
            git_version = git_version.decode()  # byte => str
            git_version = build.decode_version(git_version, prefix='git version')
            print(git_version, file=sys.stderr)
            
            # Password cache (Git v1.7.10+)
            if build.match_version(git_version, '1.7.10'):
                _git_config_global('credential.helper "cache --timeout=3600"')
            
            # Push default
            if build.match_version(git_version, '1.7.11'):
                _git_config_global('push.default simple')
            else:
                _git_config_global('push.default upstream')
              
            # TODO: Git under Proxy              
            # sudo git config --system http.proxy http://<proxy-hostname>:<proxy-port>"
            
            git_ok = True
            git_conf = subprocess.check_output('git config --list', shell=True)
            git_conf.strip()
            git_conf = git_conf.decode()
            print(git_conf)
            print('Git [OK]')
        except (subprocess.CalledProcessError, AdminError) as e:
            print('Git [FAILED]: {0}'.format(e), file=sys.stderr)
            
        # Configure WWW
        try:
            www.setup()
            print('WWW [OK]')
        except AdminError as e:
            print('WWW [FAILED]: {0}'.format(e), file=sys.stderr)
            
            
## Configuration file.
#
# ## Usage
#
# <pre><code>
#     import os
#     import sys
#     import admin
#
#     configs = {'PROJECT_NAME': '\"AAA\"',
#           'PROJECT_NUMBER': '1.2.3'}
#     try:
#         with open(os.path.join(os.getcwd(), 'Doxyfile'), 'r+') as f:
#             config_file = admin.ConfigFile(f)
#             config_file.set(configs)
#         except IOError as e:
#             print('error', file=sys.stderr)
# </code></pre>
class ConfigFile(object):

    ## Parse configuration file.
    #
    # @param config_file configuration file object
    # @param sep separator for option/value pair
    # @param comments comments leading character
    def __init__(self, config_file, sep='=', comments='#'):
        self._config_file = config_file
        self._sep = sep
        self._comments = comments
        self._config = OrderedDict()
        for line in config_file:
            # Skip blank line or comments
            if line.strip() == '' or line.startswith(comments):
                continue
                
            # Get "OPTION = value"
            pair = line.split(sep)
            self._config[pair[0].strip()] = pair[1].strip()
                
    
    ## Get value of specific option.
    #
    # @param option option name
    # @return option value
    # @exception KeyError - no optinon exists
    def get(self, option):
        return self._config[option]
        
        
    ## Set value of specific option.
    #
    # @param pairs Pairs of option name-value.
    def set(self, pairs):
        self._config_file.seek(0)
        lines = []
        for line in self._config_file:
            # Skip blank line or comments
            if line.strip() == '' or line.startswith(self._comments):
                lines.append(line)
                continue
                
            # Set option
            pair = line.split(self._sep)
            option = pair[0].strip()
            if option in pairs:
                pair[1] = ' ' + pairs[option] + '\n'
                line = self._sep.join(pair)
                del pairs[option] # Reduce size of pairs for better performance
            
            lines.append(line)
        
        # Update configuration file
        self._config_file.seek(0)
        self._config_file.writelines(lines)
            
      
def _usage():
    sys.exit('Usage: python {0} quick-setup|setup|run-uwsgi|stop-uwsgi|init-run-uwsgi|enable-nginx|disable-nginx|doc'.format(sys.argv[0]))
        
                
if __name__ == '__main__':
    if len(sys.argv) < 2:
       _usage()
       
    option = sys.argv[1]

    if option == 'setup':
        _setup()

    elif option == 'quick-setup':
        _setup(quick=True)
        
    elif option == 'run-uwsgi':
        app = sys.argv[2]
        addr = sys.argv[3]
        www.uwsgi.run(app, addr)
        
    elif option == 'stop-uwsgi':
        app = sys.argv[2]
        www.uwsgi.stop(app)
        
    elif option == 'init-run-uwsgi':
        app = sys.argv[2]
        addr = sys.argv[3]
        www.uwsgi.run(app, addr, init=True)
        
    elif option == 'enable-nginx':
        app = sys.argv[2]
        if len(sys.argv) == 4:
            upstream = sys.argv[3]
            www.nginx.enable(app, upstream=upstream)
        else:
            www.nginx.enable(app)
        
    elif option == 'disable-nginx':
        if len(sys.argv) == 4:
            app = sys.argv[2]
            upstream = sys.argv[3]
            www.nginx.disable(site=app, upstream=upstream)
        else:
            www.nginx.disable()
            
    elif option == 'doc':
        project_path = sys.argv[2]
        build.doxygen(project_path)
        
    elif option == 'test':
        _setup(quick=True)
        
        # single app on uWSGI
        time.sleep(2)
        test_app = '_setup/hello_uwsgi_app.py'
        test_addr = ':8000'
        www.uwsgi.run(test_app, test_addr)
        time.sleep(2)
        www.uwsgi.stop(test_app)
        
        # (Django) site on uWSGI
        time.sleep(2)
        test_app = '/tmp/zl'
        www.uwsgi.run(test_app, test_addr)
        time.sleep(2)
        www.uwsgi.stop(test_app)
        
        build.doxygen('.')
        
    else:
        _usage() 
