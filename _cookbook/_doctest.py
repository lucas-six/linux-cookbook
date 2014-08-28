#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package _cookbook
Docstring Testing Cookbook.

The `doctest` module searches for pieces of documents that look like
interactive Python sessions, and then executes those sessions to verify that
they work exactly as shown. There are several common ways to use `doctest`:

    - To check that a module's docstrings are up-to-date by verifying that all
      interactive examples still work as documented.
      
    - To perform regression testing by verifying that interactive examples
      from a test file or a test object work as expected.
    
    - To write tutorial documentation for a package, liberally illustrated
      with input-output examples. Depending on whether the examples or the
      expository text are emphasized, this has the flavor of "executable
      documentation".

      
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


def func_1():
    '''No return.

    >>> func_1()

    '''
    pass


def func_2():
    '''Print a blank line.

    >>> func_2()
    <BLANKLINE>

    '''
    print()


def func_3(msg):
    '''Print a string.

    @param msg -- A message to be printed out

    >>> func_3("Hello")
    Hello

    '''
    print(msg)


def func_4():
    '''Raise an exception (ValueError).

    @exception ValueError

    >>> func_4()
    Traceback (most recent call last):
        ...
    ValueError: error description
    '''
    raise ValueError("error description")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # You can also test examples in a text file:
    doctest.testfile('_doctest.md')
