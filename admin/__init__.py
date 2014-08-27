#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package admin
Admin Linux (Ubuntu)

This file contains some common functions:

  - error()
  - update_seq_type()
  - force_remove()
  - Version, decode_version(), match_version()
  

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
from collections import namedtuple


Version = namedtuple('Version', 'major, minor, patch')


## Print error messages.
#
# @param msg error message
def error(msg):
    '''Print error messages.
    '''
    print(msg, file=sys.stderr)
    
    
## Update type of all elements in specific sequence.
#
# @param seq (mutable) sequence to be update
# @param typename Target type name
def update_seq_type(seq, typename):
    '''Update type of all elements in specific sequence.
    '''
    for index, value in enumerate(seq[:]):
        seq[index] = typename(value)
        

## Like command `rm -f`.
#
# @param path Path name of entry to be removed
def force_remove(path):
    '''Like command `rm -f`.
    '''
    try:
        os.remove(path)
    except OSError:
        pass
        
    
## Decode version information string.
#
# @param version_info version information string (e.g. Python 2.7.8)
# @param prefix prefix string of version 
# @return Version named-tuple
def decode_version(version_info, prefix=''):
    '''Decode version information string.
    '''
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
def match_version(version, match):
    '''Match the specific version.
    '''
    version = decode_version(version)
    match = decode_version(match)
        
    return (version.major > match.major) \
            or (version.major == match.major and version.minor > match.minor) \
            or (version.minor == match.minor and version.patch >= match.patch)
        
        
## Test Case of Admin
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
    
   
if __name__ == '__main__':
    error('Test error()')
    unittest.main()
                