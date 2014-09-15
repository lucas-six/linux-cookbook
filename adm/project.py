#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package admin
Admin Project

This file contains classes and functions to build projects.

  - Project

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

import os
import errno
import subprocess
import configparser

import admin


## Project.
#    
#  ## Usage
#
#  <pre><code>
#      import admin
#      import admin.project
#
#      try:
#          proj = admin.project.Project(types=['python'], name='test')
#      except os.error as e:
#          admin.error(e)
#        
#      # Setup uWSGI server
#      try:
#          proj.uwsgi()
#      except (configparser.NoSectionError, subprocess.CalledProcessErro) as e:
#          admin.error(e)
#
#      # Generate documentation
#      try:
#          proj.doxygen()
#      except subprocess.CalledProcessError as e:
#          admin.error(e)
#      except IOError as e:
#          admin.error(e)
#  </code></pre>
class Project(object):
    _setup_dir = os.path.realpath('_setup')

    ## Create an instance of Project.
    #
    # @param types project types (python, django, c, java, cpp)
    # @param name project name
    # @exception os.error
    def __init__(self, types, name='test'):
        self.types = types
        self.path = os.path.realpath(name)
        self.name = os.path.basename(self.path)

        self._uwsgi_ini = None

        # Project brief
        README_file = os.path.join(self.path, 'README.md')
        try:
            for line in admin.read_lines(README_file, 4):
                self.brief = line
        except IOError as e:
            self.brief = ''
                
        # Project version
        default_version = '0.0.0'
        try:
            versions = subprocess.check_output('git tag', shell=True)
            if len(versions) == 0:
                self.version_info = default_version
            else:
                self.version_info = versions[-1]
        except subprocess.CalledProcessError as e:
            self.version_info = default_version
            
        # Create a project directory
        if 'django' in self.types:
            if not os.path.lexists(self.path):
                admin.shell('django-admin.py startproject ' + self.name)
                os.chdir(self.name)
                admin.shell('python manage.py migrate')
                os.chdir('..')
        else:
            try:
                os.makedirs(self.path)
            except os.error as e:
                # already exists, ignore
                if e.errno != errno.EEXIST:
                    raise
            
            
    # Setup uWSGI server.
    #
    # @param app uWSGI App
    # @param nginx address of bridge between nginx and uWSGI
    # @exception ConfigParser.NoSectionError
    # @exception subprocess.CalledProcessError
    #
    # @see https://uwsgi.readthedocs.org/en/latest/index.html
    # @since uWSGI 2.0.6
    def uwsgi(self, app='', nginx=None):
        single_app_file = True
        if os.path.splitext(app)[1] != '.py':
            single_app_file = False

        # Create uWSGI configuration from template
        ini_tpl = os.path.join(self._setup_dir, 'uwsgi_app.ini')
        ini = os.path.join(admin.www_root, self.name, 'uwsgi_app.ini')
        config = ConfigParser.SafeConfigParser(allow_no_value=True)
        with open(ini_tpl) as tpl_f:
            config.readfp(tpl_f)
            
            # Number of processes
            config.set('uwsgi', 'processes', str(admin.cpu_cores()))

            # PID file
            config.set('uwsgi', 'pidfile', '/tmp/uwsgi-' + self.name + '.pid')
            
            # Log file
            config.set('uwsgi', 'daemonize', \
                    '{0}/{1}.log'.format(admin.uwsgi_log_root, self.name))
            
            # nginx
            if nginx is not None:
                config.remove_option('uwsgi', 'http')
                config.set('uwsgi', 'socket', nginx)
            else:
                config.remove_option('uwsgi', 'socket')
            
            # wsgi-file/module 
            if not single_app_file:
                config.remove_option('uwsgi', 'wsgi-file')
                config.set('uwsgi', 'chdir', self.path) 
                config.set('uwsgi', 'module', self.name + '.wsgi')
            else:
                app_path = os.path.join(self.path, app)
                config.remove_option('uwsgi', 'chdir')
                config.remove_option('uwsgi', 'module')
                config.set('uwsgi', 'wsgi-file', app_path)
                
            with open('/tmp/uwsgi_app.ini', 'w') as f:
                config.write(f)
              
        admin.shell('sudo cp /tmp/uwsgi_app.ini ' + ini)
        admin.force_remove('/tmp/uwsgi_app.ini')

    
    ## Generate documentation for codes under Git by Doxygen.
    #
    # @param doxyfile name of Doxygen configuration file
    # @exception subprocess.CalledProcessError
    # @exception IOError
    def doxygen(self, doxyfile='Doxyfile'):
        # Generate Doxygen configuration file
        os.chdir(self.path)
        admin.shell('doxygen -g {0}'.format(doxyfile))
            
        # Update Doxygen configuration file
        optimize_for_c = 'NO'
        optimize_for_java_or_python = 'NO'
        if 'c' in self.types:
            optimize_for_c = 'YES'        
        if 'java' in self.types or 'python' in self.types or 'django' in self.types:
            optimize_for_java_or_python = 'YES'
        configs = {'PROJECT_NAME': '\"{0}\"'.format(self.name),
                'PROJECT_NUMBER': self.version_info,
                'PROJECT_BRIEF': '\"{0}\"'.format(self.brief),
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
                'INPUT': '../admin',
                'FILE_PATTERNS': '*.py *.c *.h *.cpp *.hh',
                'RECURSIVE': 'YES',
                'SOURCE_BROWSER': 'YES',
                'EXCLUDE_PATTERNS': '*/test/*',
                'USE_MDFILE_AS_MAINPAGE': 'YES',
                'HTML_TIMESTAMP': 'YES',
                'HTML_DYNAMIC_SECTIONS': 'YES',
                'GENERATE_MAN': 'YES',
                'MAN_LINKS': 'YES'}
        with open(os.path.join(self.path, doxyfile), 'r+') as f:
            config_file = admin.ConfigFile(f)
            config_file.set(configs)
        
        # Generate documentation by Doxygen
        admin.shell('doxygen {0}'.format(doxyfile))

        # Back to top directory, NOT project directory
        os.chdir('..')
        
