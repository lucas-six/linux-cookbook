#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Setup Linux (Ubuntu)

    - Vim
    - Git

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

from __future__ import print_function

import sys
import os
import platform
import subprocess

import admin
        
        
def info(msg, end='\n'):
    '''Print informational message.
    
    @param msg Informational message
    '''
    print(msg, end=end, file=sys.stderr)
                        
            
def setup(test=False):
    '''Setup main.
    
    @param test True if testing usage.
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
            if not test:
                subprocess.check_call('sudo apt-get update', shell=True)

            pkgs = ['sudo', 'apt', 'apt-utils', \
                    'bash', 'python', 'coreutils', \
                    'vim', 'git', 'doxygen']
            subprocess.check_call('sudo apt-get install '+' '.join(pkgs), \
                    shell=True)
        except subprocess.CalledProcessError as e:
            sys.exit('Failed to install core packages: {0}'.format(e))
        info('System updated [OK]')
            
        vimrc_ok = False
        git_ok = False
            
        # Symbolic link vimrc, backup it if already existing.
        info('\n*** vimrc ***')
        vimrc = os.path.expanduser('~/.vimrc')
        try:
            if os.path.lexists(vimrc):
                old_vimrc = vimrc + '.old'
                admin.force_remove(old_vimrc)
                os.rename(vimrc, old_vimrc)
            myvimrc = os.path.join(os.getcwd(), '_setup', 'vimrc')
            os.symlink(myvimrc, vimrc)
            vimrc_ok = True
            info('Vimrc [OK]')
        except OSError as e:
            admin.error('Vimrc [FAILED]: {0}'.format(e))
            
        # Configure bashrc
        if not test:
            try:
                with open(os.path.expanduser('~/.bashrc'), 'a') as f:
                    if vimrc_ok:
                        # Set default editor to Vim
                        f.write('\nexport EDITOR=vim')
                        info('Set default editor to Vim [OK]')
                subprocess.check_call('. ~/.bashrc', shell=True)
            except IOError as e:
                admin.error('Failed to set default editor to Vim: {0}'.format(e))
            except subprocess.CalledProcessError as e:
                admin.error('Failed to reload bashrc: {0}'.format(e))
                        
        # Configure Git
        # For more details on Git, please refer to the Pro Git online
        # version:
        #
        #     http://www.git-scm.com/book/
        #
        # Or an online referernce:
        #
        #     http://gitref.org/
        info('\n*** Git ***')
        def _git_config(conf):
            subprocess.check_call('git config ' + conf, shell=True)
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
            git_version = admin.decode_version(git_version, prefix='git version')
            admin.debug(git_version)
            
            # Password cache (Git v1.7.10+)
            if admin.match_version(git_version, '1.7.10'):
                _git_config_global('credential.helper "cache --timeout=3600"')
            
            # Push default
            if admin.match_version(git_version, '1.7.11'):
                _git_config_global('push.default simple')
            else:
                _git_config_global('push.default upstream')
              
            # TODO: Git under Proxy              
            # sudo git config --system http.proxy http://<proxy-hostname>:<proxy-port>"
            
            git_ok = True
            git_conf = subprocess.check_output('git config --list', shell=True)
            git_conf.strip()
            info(git_conf)
            info('Git [OK]')
        except subprocess.CalledProcessError as e:
            admin.error('Git [FAILED]: {0}'.format(e))
            
            
def admin_unittest():
    '''Admin Unit Testing.
    '''
    try:
        subprocess.check_call('python admin/__init__.py', shell=True)
    except subprocess.CalledProcessError as e:
        sys.exit('Admin Unit Testing [FAILED]: {0}'.format(e))
        
                
if __name__ == '__main__':
    if len(sys.argv) == 2:
        option = sys.argv[1]
        if option == 'test':
            admin_unittest()
            setup(test=True)
    else:
        setup()
        