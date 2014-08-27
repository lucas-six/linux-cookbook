#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package admin
Admin Linux (Ubuntu)

This file contains some common functions:

  - error()
  - update_seq_type()
  

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
        
        
## Test Case of Admin
class AdminTestCase(unittest.TestCase):
    '''Test Case of Admin.
    '''
    def setUp(self):
        pass
        
        
    def tearDown(self):
        pass
        
        
    def test_update_seq_type(self):
        seq = [1 ,2, 3]
        update_seq_type(seq, str)
        for item in seq:
            self.assertIsInstance(item, str)
    
   
if __name__ == '__main__':
    error('Test error()')
    unittest.main()
                