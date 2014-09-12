#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Context Manager Cookbook.

Python’s `with` statement supports the concept of a runtime context defined by
a _context manager_. This is implemented using two separate methods
(`__enter__()`, and `__exit__()`) that allow user-defined classes to define a
runtime context that is entered before the statement body is executed and
exited when the statement ends.

A example of context manager as follows:

    >>> class MyContextManager(object):
    ...    def __init__(self):
    ...        # initialization here ...
    ...        # if error, raise Exception.
    ...        pass
    ...
    ...        
    ...    def close(self):
    ...        # clearing context here ...
    ...        pass
    ...
    ...
    ...    def do(self):
    ...        # do something here ...
    ...        # if error, raise Exception.
    ...        pass
    ...
    ...     
    ...    def __enter__(self):
    ...        return self
    ...
    ... 
    ...    def __exit__(self, etype, evalue, traceback):
    ...        if etype is not None:
    ...            print(etype, evalue, traceback)
    ...        self.close()
            
Simple usage of it:

    >>> try:
    ...    with MyContextManager() as cm:
    ...        cm.do()
    ... except Exception:
    ...    # handle error
    ...    pass


For more details on Context Manager and <code>with</code> statement, please
refer to the _PEP 0343_ online:

    http://www.python.org/dev/peps/pep-0343
    

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

from contextlib import contextmanager


class MyContextManagerWithDecorator(object):
    def __init__(self, ok=True):
        if ok:
            print('open OK')
        else:
            print('open failed')
            raise IOError

            
    def close(self):
        print('closed')

        
    def do(self, ok=True):
        if ok:
            print('operation OK')
        else:
            print('operation failed')
            raise IOError


@contextmanager
def opening(ok):
    my_context_manager = MyContextManagerWithDecorator(ok)
    try:
        yield my_context_manager
    finally:
        my_context_manager.close()


@contextmanager
def closing(context_manager):
    '''Python standard library contains this function'''
    try:
        yield context_manager
    finally:
        context_manager.close()


def test(mycontextmanager_ok, operation_ok):
    print('Test Case: MyContextManager={0}, Operation={1}\n==='\
          .format(mycontextmanager_ok, operation_ok))
          
    try:
        with opening(mycontextmanager_ok) as cm:
            cm.do(operation_ok)
    except IOError:
        print('Error')
        
    print('')


if __name__ == '__main__':

    # Test Case 1: MyContextManager() OK, operation() OK
    test(True, True)

    # Test Case 2: MyContextManager() failed, operation() OK
    test(False, True)

    # Test Case 3: MyContextManager() OK, operation() failed
    test(True, False)

    # Test Case 4: MyContextManager() failed, operation() failed
    test(False, False)
    
    import doctest
    doctest.testmod()
