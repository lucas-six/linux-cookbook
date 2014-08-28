#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package _unittest
Unit testing framework.

The Python unit testing framework, sometimes referred to as “PyUnit,” is a
Python language version of JUnit, by *Kent Beck* and *Erich Gamma*. JUnit is,
in turn, a Java version of Kent’s Smalltalk testing framework. Each is the de
facto standard unit testing framework for its respective language.

To achieve this, `unittest` supports some important testing concepts:

  - test case
  
  > A **test case** is the smallest unit of testing. It checks for a specific
  > response to a particular set of inputs. `unittest` provides a base class,
  > `TestCase`, which may be used to create new test cases.
  
  - test suite
  
  > A **test suite** is a collection of test cases, test suites, or both. It is
  > used to aggregate tests that should be executed together.
  
  - test runner
  
  > A **test runner** is a component which orchestrates the execution of tests
  > and provides the outcome to the user. The runner may use a graphical
  > interface, a textual interface, or return a special value to indicate the
  > results of executing the tests.

      
Copyright (c) 2014 Li Yun <leven.cn@gmail.com>
All Rights Reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''

from __future__ import print_function

import unittest


def func_1():
    '''No return.
    '''
    pass


def func_2(a):
    '''Echo.
    '''
    return a


def func_3():
    '''Raise an exception (ValueError).

    @exception ValueError

    >>> func_4()
    Traceback (most recent call last):
        ...
    ValueError: error description
    '''
    raise ValueError("error description")
    
    
class _UnitTestTestCase(unittest.TestCase):
    def setUp(self):
        # Initialization
        pass
        
        
    def tearDown(self):
        # Clean up
        pass
        
        
    #@unittest.skip("<reason>")
    #@unittest.skipIf(<condition>, "<reason>")
    #@unittest.skipUnless(<condition>, "<reason>")
    #@unittest.expectedFailure()
    def test_func_1(self):
        # Testing
        #
        # self.assertTrue(a)               a
        # self.assertFalse(a)              not a
        # self.assertIs(a, b)              a is b
        # self.assertIsNot(a, b)           a is not b
        # self.assertIsNone(a)             a is None
        # self.assertIsNotNone(a)          a is not None
        # self.assertIn(a, b)              a in b
        # self.assertNotIn(a, b)           a not in b
        # self.assertIsInstance(a, b)      isinstance(a, b)
        # self.assertNotIsInstance(a, b)   not isinstance(a, b)
        # self.assertEqual(a, b)           a == b
        # self.assertNotEqual(a, b)        a != b
        # self.assertGreater(a, b)         a > b
        # self.assertLess(a ,b)            a < b
        # self.assertGreaterEqual(a, b)    a >= b
        # self.assertLessEqual(a, b)       a <= b
        #
        # with self.assertRaises(Error):   raise Error
        #     func(a, b)
        pass
        
        
    def test_func_2(self):
        self.assertTrue(func_2(True))
        self.assertFalse(func_2(False))
        self.assertIs(func_2(None), None)
        self.assertIsNot(func_2([1,2]), None)
        self.assertIsNone(func_2(None))
        self.assertIn(func_2(1), [1,2])
        self.assertNotIn(func_2(3), [1,2])
        self.assertIsInstance(func_2(1), int)
        self.assertNotIsInstance(func_2(1), str)
        self.assertEqual(func_2(1), 1)
        self.assertNotEqual(func_2(1), 2)
        self.assertGreater(func_2(1), 0)
        self.assertGreaterEqual(func_2(1), 0)
        self.assertGreaterEqual(func_2(1), 1)
        self.assertLess(func_2(1), 2)
        self.assertLessEqual(func_2(1), 2)
        self.assertLessEqual(func_2(1), 1)
        
        
    def test_func_3(self):
        with self.assertRaises(ValueError):
            func_3()


if __name__ == '__main__':
    unittest.main()
