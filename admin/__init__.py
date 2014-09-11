#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package admin
Admin Linux (Ubuntu)

This file contains some common functions and classes:

  - error(), debug()
  - update_seq_type()
  - shell(), force_remove()
  - Version, decode_version(), match_version()
  - ConfigFile
  - cpu_cores() (Only /proc supported system)
  - run_uwsgi()
  

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
import unittest
import errno
import subprocess
from collections import namedtuple
from collections import OrderedDict


Version = namedtuple('Version', 'major, minor, patch')


www_root = '/var/spool/www'
uwsgi_log_root = '/var/log/uwsgi'


## Print error messages.
#
# @param msg error message
def error(msg):
    print(msg, file=sys.stderr)
    
    
## Print debugging message.
#
# @param msg Debugging message
#
# **NOTE**: This function could be turned off by `-O` or `-OO` option.
def debug(msg, prefix='[DBG]'):
    if __debug__:
        print('{0}:'.format(prefix), end=' ', file=sys.stderr)
        print(msg, file=sys.stderr)
    
    
## Update type of all elements in specific sequence.
#
# @param seq (mutable) sequence to be update
# @param typename target type name
def update_seq_type(seq, typename):
    for index, value in enumerate(seq[:]):
        seq[index] = typename(value)


## Run shell commandi without output.
#
# @param cmd shell command
# @exception subprocess.CalledProcessError - from `cmd`
def shell(cmd):
    subprocess.check_call(cmd, shell=True)
        

## Command `rm -f`.
#
# @param path path name of entry to be removed
def force_remove(path):
    try:
        os.remove(path)
    except OSError:
        pass
        
        
## Restart a system call interrupted by `EINTR`.
#
# @param func system call
# @param args arguments of system call
# @exception socket.error
# @exception select.error
# @exception OSError
def eintr_retry(func, *args):
    while True:
        try:
            return func(*args)
        except (OSError, socket.error, select.error) as e:
            if e.errno != errno.EINTR:
                raise
        
    
## Decode version information string.
#
# @param version_info version information string (e.g. Python 2.7.8)
# @param prefix prefix string of version 
# @return Version named-tuple
def decode_version(version_info, prefix=''):
    # Skip if it already decoded
    if isinstance(version_info, Version):
        return version_info
    
    version_info.strip()
    version_info = version_info[len(prefix):].strip().split('.')
    
    # Change version number from string to integer.
    update_seq_type(version_info, int)
        
    return Version._make(version_info)
    
    
## Match the specific version.
#
# @param version Version named-tuple
# @param match version string (e.g. 1.2.3)
# @return True if match
def match_version(version, match):
    version = decode_version(version)
    match = decode_version(match)
        
    if version.major < match.major:
        return False
        
    return (version.major > match.major) \
            or (version.major == match.major and version.minor > match.minor) \
            or (version.minor == match.minor and version.patch >= match.patch)
            
            
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
        
        
## Configuration file.
#
# ## Usage
#
# <pre><code>
#     import os
#     import admin
#
#     configs = {'PROJECT_NAME': '\"AAA\"',
#           'PROJECT_NUMBER': '1.2.3'}
#     try:
#         with open(os.path.join(os.getcwd(), 'Doxyfile'), 'r+') as f:
#             config_file = admin.ConfigFile(f)
#             config_file.set(configs)
#         except IOError as e:
#             admin.error('error')
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
        
        
# Get number of CPU cores from /proc file system.
#
# @return number of CPU cores
# @exception subprocess.CalledProcessError - from `grep` or `/proc/cpuinfo`
def cpu_cores():
    i = subprocess.check_output('grep "cpu cores" /proc/cpuinfo', shell=True)
    return int(i.split(':')[1].strip())


## Run (or Reload) uWSGI server
#
# @param app app name
# @param port uWSGI server port
# @exception subprocess.CalledProcessError
#
# NOTE: Before run uWSGI with Django, make sure that Django project actually
# works:
#
#     python manage.py runserver 0.0.0.0:8000
#
#
# @see https://www.djangoproject.com/
# @since uWSGI 2.0.6
# @since Django 1.7
def run_uwsgi(app, port):
    # Generate uwsgi init script
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
exec uwsgi --ini /var/spool/www/{0}/uwsgi_app.ini\n'.format(app, port))
        f.flush()
    shell('sudo mv -u {0} /etc/init/.'.format(tmp_file))
 
        
class AdminTestCase(unittest.TestCase):
    '''Test Case of Admin.
    '''
    def setUp(self):
        self.version_info = 'Python 2.7.8'
        self.version_prefix = 'Python'
        
        
    def tearDown(self):
        pass
        
        
    def test_update_seq_type(self):
        seq = [1 ,2, 3]
        update_seq_type(seq, str)
        for item in seq:
            self.assertIsInstance(item, str)
            
            
    def test_decode_version(self):
        v = decode_version(self.version_info, self.version_prefix)
        self.assertIsInstance(v, Version)
        self.assertEqual(v.major, 2)
        self.assertEqual(v.minor, 7)
        self.assertEqual(v.patch, 8)
        
        
    def test_match_version(self):
        v = decode_version(self.version_info, self.version_prefix)
        self.assertTrue(match_version(v, '2.7.8'))
        self.assertTrue(match_version(v, '2.7.6'))
        self.assertFalse(match_version(v, '2.7.9'))
        self.assertTrue(match_version(v, '2.6.8'))
        self.assertTrue(match_version(v, '2.6.6'))
        self.assertTrue(match_version(v, '2.6.9'))
        self.assertFalse(match_version(v, '2.8.8'))
        self.assertFalse(match_version(v, '2.8.6'))
        self.assertFalse(match_version(v, '2.8.9'))
        self.assertTrue(match_version(v, '1.7.8'))
        self.assertTrue(match_version(v, '1.8.8'))
        self.assertTrue(match_version(v, '1.6.8'))
        self.assertTrue(match_version(v, '1.7.6'))
        self.assertTrue(match_version(v, '1.7.9'))
        self.assertFalse(match_version(v, '3.7.8'))
        self.assertFalse(match_version(v, '3.8.8'))
        self.assertFalse(match_version(v, '3.6.8'))
        self.assertFalse(match_version(v, '3.7.6'))
        self.assertFalse(match_version(v, '3.7.9'))
        
    
    def test_read_lines(self):
        # Invalid file name
        with self.assertRaises(TypeError):
            for line in read_lines(None, 0):
                pass
                
        # File not exists
        with self.assertRaises(IOError):
            for line in read_lines('Not-exist-file', 0):
                pass
                
        # Normal
        for line in read_lines(__file__, 1):
            self.assertEqual(line, '#!/usr/bin/env python')
        for index, line in enumerate(read_lines(__file__, [1, 2, 3])):
            self.assertIn(index, [0, 1, 2])
            if index == 0:
                self.assertEqual(line, '#!/usr/bin/env python')
            elif index == 1:
                self.assertEqual(line, '# -*- coding: utf-8 -*-')
            elif index == 2:
                self.assertEqual(line, '')
    
   
if __name__ == '__main__':
    error('Test error()')
    debug('Test debug()')
    debug('CPU Cores: ' + str(cpu_cores()))
    unittest.main()
                
