#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Testing Admin Linux (Ubuntu)

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

import admin
from admin import shell
from admin import build
import unittest
            
            
class AdminTestCase(unittest.TestCase):
        '''Test Case of admin module.
        '''
        def setUp(self):
            pass
            
        
        def tearDown(self):
            pass
                
                
        def test_update_seq_type(self):
            seq = [1 ,2, 3]
            admin.update_seq_type(seq, str)
            for item in seq:
                self.assertIsInstance(item, str)
                

class AdminShellTestCase(unittest.TestCase):
        '''Test Case of admin.shell module.
        '''
        def setUp(self):
            pass
            
        
        def tearDown(self):
            pass
            
            
        def test_ShellError(self):
            with self.assertRaises(admin.AdminError):
                raise admin.AdminError(KeyError)
                
                
        def test_cpu_cores(self):
            print('CPU Cores: ' + str(shell.cpu_cores()))
            
            
        def test_read_lines(self):
            # Invalid file name
            with self.assertRaises(TypeError):
                for line in shell.read_lines(None, 0):
                    pass
                
            # File not exists
            with self.assertRaises(IOError):
                for line in shell.read_lines('Not-exist-file', 0):
                    pass
                
            # Normal
            banner_line = '#!/usr/bin/env python3'
            for line in shell.read_lines(__file__, 1):
                self.assertEqual(line, banner_line)
            for index, line in enumerate(shell.read_lines(__file__, [1, 2, 3])):
                self.assertIn(index, [0, 1, 2])
                if index == 0:
                    self.assertEqual(line, banner_line)
                elif index == 1:
                    self.assertEqual(line, '# -*- coding: utf-8 -*-')
                elif index == 2:
                    self.assertEqual(line, '')
    
    
class AdminBuildTestCase(unittest.TestCase):
        '''Test Case of admin.build module.
        '''
        def setUp(self):
            self.version_info = 'Python 2.7.8'
            self.version_prefix = 'Python'
            
        
        def tearDown(self):
            pass
                
                
        def test_decode_version(self):
            v = build.decode_version(self.version_info, self.version_prefix)
            self.assertIsInstance(v, build.Version)
            self.assertEqual(v.major, 2)
            self.assertEqual(v.minor, 7)
            self.assertEqual(v.patch, 8)
        
        
        def test_match(self):
            v = build.decode_version(self.version_info, self.version_prefix)
            self.assertTrue(build.match_version(v, '2.7.8'))
            self.assertTrue(build.match_version(v, '2.7.6'))
            self.assertFalse(build.match_version(v, '2.7.9'))
            self.assertTrue(build.match_version(v, '2.6.8'))
            self.assertTrue(build.match_version(v, '2.6.6'))
            self.assertTrue(build.match_version(v, '2.6.9'))
            self.assertFalse(build.match_version(v, '2.8.8'))
            self.assertFalse(build.match_version(v, '2.8.6'))
            self.assertFalse(build.match_version(v, '2.8.9'))
            self.assertTrue(build.match_version(v, '1.7.8'))
            self.assertTrue(build.match_version(v, '1.8.8'))
            self.assertTrue(build.match_version(v, '1.6.8'))
            self.assertTrue(build.match_version(v, '1.7.6'))
            self.assertTrue(build.match_version(v, '1.7.9'))
            self.assertFalse(build.match_version(v, '3.7.8'))
            self.assertFalse(build.match_version(v, '3.8.8'))
            self.assertFalse(build.match_version(v, '3.6.8'))
            self.assertFalse(build.match_version(v, '3.7.6'))
            self.assertFalse(build.match_version(v, '3.7.9'))
            
                
if __name__ == '__main__':
    unittest.main()
