#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Admin Linux (Ubuntu)

    - update_seq_type()
    - shell tools
    - version tools
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
    @staticmethod
    def chown(path, user, group=None):
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
            shell.shell('sudo chown {0}:{1} {2}'.format(user, group, path))
        
        if os.path.isdir(path):
            if group_permission_on:
                # mode: drwxrwxr-x
                mode = stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH
                try:
                    os.chmod(path, mode)
                except PermissionError:
                    shell.shell('sudo chmod u=rwx,g=rwx,o=rx ' + path)
                    
                    
    ## Remove path entry.
    #
    # @param path path name of entry to be removed
    @staticmethod
    def remove(path):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        except OSError:
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
    # @param exist_ok True for raising OSError if the target directory already exists
    # @param user owner user name or uid
    # @param group owner group name or gid
    # @exception AdminError(OSError) - target directory already exists
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo mkdir` error
    # @exception AdminError(ValueError) - both user or group not given
    # @exception AdminError(LookupError) - user or group given not in system
    # @exception AdminError(subprocess.CalledProcessError) - change ownership error
    # @since Python 3.2
    def mkdir(path, exist_ok=False, user=None, group=None):
        try:
            os.makedirs(path, exist_ok=exist_ok)
        except PermissionError:
            if exist_ok:
                shell.shell('sudo mkdir -p ' + path)
            else:
                shell.shell('sudo mkdir ' + path)
        except OSError as e:
            raise AdminError(e)

        # change ownership
        if user is not None:
            shell.chown(path, user, group=group)
            
            
    ## Create a symbolic link pointing to source named `link_name`.
    #
    # @param src source file
    # @param link_name symbolic link name
    # @exception AdminError(subprocess.CalledProcessError) - shell `sudo ln -sf` error
    def symlink(src, link_name):
        try:
            os.symlink(src, link_name)
        except PermissionError:
            shell.shell('sudo ln -sf {0} {1}'.format(src, link_name))
            
            
    ## Read specific line(s) with line number(s).
    #
    # @param filename file name
    # @param lineno line number(s) to read (starting with 1)
    # @return generator object of line with no terminating line break
    # @exception TypeError, IOError
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
    def cpu_cores():
        try:
            i = subprocess.check_output('grep "cpu cores" /proc/cpuinfo', shell=True)
        except subprocess.CalledProcessError as e:
            raise AdminError(e)
        return int(i.split(b':')[1].strip())
        
        
## Version tools
#
# This module contains functions and classes for versions, including:
#
#   - Version
#   - decode()
#   - match()
class version(object):

    Version = namedtuple('Version', 'major, minor, patch')
    
    ## Decode version information string.
    #
    # @param version_info version information string (e.g. Python 3.4.1)
    # @param prefix prefix string of version 
    # @return Version named-tuple
    @staticmethod
    def decode(version_info, prefix=''):
        # Skip if it already decoded
        if isinstance(version_info, version.Version):
            return version_info
    
        version_info.strip()
        version_info = version_info[len(prefix):].strip().split('.')
    
        # Change version number from string to integer.
        update_seq_type(version_info, int)
        
        return version.Version._make(version_info)
        
        
    ## Match the specific version.
    #
    # @param v Version named-tuple
    # @param match version string (e.g. 1.2.3)
    # @return True if match
    @staticmethod
    def match(v, match):
        v = version.decode(v)
        match = version.decode(match)
        
        if v.major < match.major:
            return False
        
        return (v.major > match.major) \
                or (v.major == match.major and v.minor > match.minor) \
                or (v.minor == match.minor and v.patch >= match.patch)
                
             
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
        shell.mkdir(root, exist_ok=True, user=user, group=group)
        shell.mkdir(uwsgi_log_root, exist_ok=True, user=user, group=group)
        
        
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
        # @exception AdminError(subprocess.CalledProcessError) - shell error
        # @exception IOError - configuration file error
        #
        # NOTE: Before run uWSGI with Django, make sure that Django project
        # actually works:
        #
        #     python manage.py runserver 0.0.0.0:8000
        #
        #
        # @see https://www.djangoproject.com/
        # @since Django 1.7
        # @since Python 3.2
        @staticmethod
        def run(app, addr, init=False):
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
            pid_file = www.uwsgi._pidfile(app_name)
            ini_cmd = 'uwsgi --ini ' + ini_file
            shell.mkdir(app_root, exist_ok=True)

            # Configure uWSGI server
            config = configparser.ConfigParser(allow_no_value=True)
            config['uwsgi'] = {}            
            if True:
                # HTTP
                config['uwsgi']['http'] = addr
            else:
                # internal communication
                config['uwsgi']['socket'] = None                
            if is_module:
                # module path
                config['uwsgi']['chdir'] = None
                config['uwsgi']['module'] = None
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
        @staticmethod
        def stop(app):
            app_name = os.path.splitext(os.path.basename(app))[0]
            pid_file = www.uwsgi._pidfile(app_name)
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
    
        ## Setup nginx
        #
        # @param site site name
        # @param port site port number
        # @param name site server name
        # @exception IOError - site configuration file error
        # @exception AdminError(subprocess.CalledProcessError) - shell `sudo mv` error
        @staticmethod
        def setup(site, port=80, name='localhost'):
            with open('/tmp/nginx-{0}'.format(site), 'w') as f:
                f.write('# nginx site configuration for {0}\n\
# Generated by admin.py - DONOT edit!!!\n\
\n\
# virtual host\n\
server {{\n\
\tlisten {1} default_server;\n\
\tlisten [::]:{1} default_server ipv6only=on;\n\
\n\
\troot /usr/share/nginx/html;\n\
\tindex index.html index.htm;\n\
\n\
\t# Make site accessible from http://{2}/\n\
\tserver_name {2};\n\
\n\
\tlocation / {{\n\
\t\t# First attempt to serve request as file, then\n\
\t\t# as directory, then fall back to displaying a 404.\n\
\t\ttry_files $uri $uri/ =404;\n\
\t\t# Uncomment to enable naxsi on this location\n\
\t\t# include /etc/nginx/naxsi.rules\n\
\t}}\n\
\n\
\t# Only for nginx-naxsi used with nginx-naxsi-ui : process denied requests\n\
\t#location /RequestDenied {{\n\
\t\t#proxy_pass http://127.0.0.1:8080;\n\
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
}}\n'.format(site, port, name))
            shell.shell('sudo mv -u /tmp/nginx-{0} /etc/nginx/sites-available/{0}'.format(site))
            

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
            os.symlink(myvimrc, vimrc)
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
        # For more details on Git, please refer to the Pro Git online
        # version:
        #
        #     http://www.git-scm.com/book/
        #
        # Or an online referernce:
        #
        #     http://gitref.org/
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
            git_version = version.decode(git_version, prefix='git version')
            print(git_version, file=sys.stderr)
            
            # Password cache (Git v1.7.10+)
            if version.match(git_version, '1.7.10'):
                _git_config_global('credential.helper "cache --timeout=3600"')
            
            # Push default
            if version.match(git_version, '1.7.11'):
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
    sys.exit('Usage: python {0} quick-setup|setup|run-uwsgi|stop-uwsgi|init-run-uwsgi|build'.format(sys.argv[0]))
        
        
def build(name='zl'):
    '''Build projects.
    
    @param name project name
    @exception ConfigParser.NoSectionError
    @exception subprocess.CalledProcessError
    '''
    #proj = admin.project.Project(types=['python'], name=name)
    #proj.uwsgi(app='../_setup/uwsgi_app.py')

    proj = admin.project.Project(types=['django'], name=name)
    #proj.uwsgi()
    proj.uwsgi(nginx=':8001')
    info('\nuWSGI [OK]')
    
    proj.doxygen()
    
                
if __name__ == '__main__':
    if len(sys.argv) < 2:
       _usage()
       
    option = sys.argv[1]

    if option == 'setup':
        _setup()

    elif option == 'quick-setup':
        _setup(quick=True)

    elif option == 'build':
        if len(sys.argv) != 3:
            sys.exit('Usage: {0} build <project-name>'.format(sys.argv[0]))
        build(name=sys.argv[2])
        
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
        
    elif option == 'test':
        _setup(quick=True)
        
        time.sleep(2)
        test_app = '_setup/hello_uwsgi_app.py'
        test_addr = ':8000'
        www.uwsgi.run(test_app, test_addr)
        
        time.sleep(2)
        www.uwsgi.stop(test_app)
        
        www.nginx.setup('hello_nginx_app')
        
    else:
        _usage() 
