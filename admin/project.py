#!/usr/bin/env python
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
import subprocess
import ConfigParser

import admin


## Project.
#    
#  ## Usage
#
#  <pre><code>
#      import admin
#      import admin.project
#
#      proj = admin.project.Project(lang=['python'])
#      try:
#          # Setup uWSGI server
#          proj.uwsgi()
#
#          # Setup Django
#          proj.django()
#
#          # Generate documentation
#          proj.doxygen()
#      except subprocess.CalledProcessError as e:
#          admin.error('error')
#      except IOError as e:
#          admin.error('error')
#  </code></pre>
class Project(object):
    ## Create an instance of Project.
    #
    # @param lang programming language (python, c, java, cpp)
    # @param build_dir building directory
    # @param default_version default version string
    def __init__(self, lang, build_dir='build', default_version='0.0.0'):
        self.lang = lang
        self.path = os.getcwd()
        self.name = os.path.basename(self.path)
        self._build_dir = build_dir
        README_file = os.path.join(self.path, 'README.md')
        try:
            for line in admin.read_lines(README_file, 4):
                self.brief = line
        except IOError as e:
            admin.error('Get brief description [FAILED]: {0}'.format(e))
            self.brief = ''
                
        # Project version
        try:
            versions = subprocess.check_output('git tag', shell=True)
            if len(versions) == 0:
                self.version_info = default_version
            else:
                self.version_info = versions[-1]
        except subprocess.CalledProcessError as e:
            admin.error('Get project version [FAILED]: {0}'.format(e))
            self.version_info = default_version
            
        # Create a building directory
        try:
            os.mkdir(self._build_dir)
        except OSError:
            # already exists, ignore
            pass
            
            
    # Setup (or Run) uWSGI server.
    #
    # Support 2.0.6
    #
    # @param wsgi_file uWSGI App
    # @param django Django site name
    # @param nginx address of bridge between nginx and uWSGI
    # @param run True to run uWSGI server
    # @exception ConfigParser.NoSectionError - from `uwsgi_app.ini`
    # @exception subprocess.CalledProcessError - from `uwsgi`
    def uwsgi(self, wsgi_file='_setup/uwsgi_app.py', django=None, nginx=None, run=False):
        # Create uWSGI configuration from template
        ini_tpl = os.path.join(self.path, '_setup/uwsgi_app.ini')
        ini = os.path.join(self.path, self._build_dir, 'uwsgi_app.ini')
            
        # Update uWSGI configuration
        config = ConfigParser.SafeConfigParser(allow_no_value=True)
        if django is not None:
            wsgi_file = os.path.join(self._build_dir, django)
        app_path = os.path.join(self.path, wsgi_file)
        with open(ini_tpl) as tpl_f:
            config.readfp(tpl_f)
            
            # nginx
            if nginx is not None:
                config.remove_option('uwsgi', 'http')
                config.set('uwsgi', 'socket', nginx)
            else:
                config.remove_option('uwsgi', 'socket')
            
            # Django
            if django is not None:
                config.remove_option('uwsgi', 'wsgi-file')
                config.set('uwsgi', 'module', django+'.wsgi')
                
            # uWSGI
            else:
                config.remove_option('uwsgi', 'module')
                config.set('uwsgi', 'wsgi-file', app_path)
                
            with open(ini, 'w') as f:
                config.write(f)
              
        # Run uWSGI server
        if run:
            subprocess.check_call('uwsgi --ini '+ini, shell=True)
        
    
    # Setup Django project.
    #
    # Support 1.7
    #
    # @param site Django site directory name
    # @param nginx address of bridge between nginx and uWSGI
    # @param run True to run server with Django
    # @exception subprocess.CalledProcessError - from `django`
    def django(self, site='mysite', nginx=None, run=False):
        # Create Django project
        os.chdir(self._build_dir)
        if not os.path.lexists(site):
            subprocess.check_call('django-admin.py startproject '+site, \
                    shell=True)
        
        # Run uWSGI with Django
        # NOTE: Before it, make sure that Django project actually works:
        #
        #     python manage.py runserver 0.0.0.0:8000
        #
        os.chdir(site)
        self.uwsgi(django=site, nginx=nginx, run=run)
        
        # Back to top directory of project 
        os.chdir(self.path)
            
            
    ## Generate documentation for codes under Git by Doxygen.
    #
    # @param doxyfile name of Doxygen configuration file
    # @exception subprocess.CalledProcessError - from `doxygen`
    # @exception IOError - configuration file written error
    def doxygen(self, doxyfile='Doxyfile'):
        # Generate Doxygen configuration file
        subprocess.check_call('doxygen -g {0}'.format(doxyfile), shell=True)
            
        # Update Doxygen configuration file
        optimize_for_c = 'NO'
        optimize_for_java_or_python = 'NO'
        if 'c' in self.lang:
            optimize_for_c = 'YES'        
        if 'java' in self.lang or 'python' in self.lang:
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
                'INPUT': 'admin',
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
        subprocess.check_call('doxygen {0}'.format(doxyfile), shell=True)
        