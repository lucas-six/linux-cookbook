#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Function Parameters Cookbook.

Function Argument Annotations (Python 3).
    
    The Python interpreter does not attach any semantic meaning to the attached
    annotations. They are not type checks, nor do they make Python behave any
    differently than it did before. However, they might give useful hints to
    others reading the source code about what you had in mind. Third-party
    tools and frameworks might also attach semantic meaning to the annotations.
    
    Although you can attach any kind of object to a function as an annotation
    (e.g., numbers, strings, instances, etc.), classes or strings often seem to
    make the most sense.
    
    Function annotations are merely stored in a function’s `__annotations__`
    attribute.
    
    For example:

        def f(x:int, y:int) --> int:
            return x + y

    
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

def func_default_value(arg, L=None):
    '''Default Values of Function Arguments.

    The default values are evaluated at the point of function definition in
    the defining scope only once.

    **NOTE**: When the default is a mutable object such as a list, dictionary,
    or instances of most classes, and if you don't want the default to be
    shared between subsequent calls, you can write the function like this
    instead.
    '''
    if L is None:
        L = []
    L.append(arg)
    return L

    
def func_unpack_args(arg1, arg2):
    '''Unpack arguments from dictionary or tuple, list.
    
    To use it,
    
        >>> mydict = {'arg1': 1, 'arg2': 2}
    
        >>> func_unpack_args(**mydict)
    
        >>> mytuple = ("a", "b")
    
        >>> func_unpack_args(*mytuple)
    
    '''
    pass


def func_vargs(arg, other='o', *vargs, **args):
    '''Variable Length Arguments List of Function.

    1. `*vargs` must be before `**args`.

    2. Any formal parameters which occur after the `*vargs` parameter are
       keyword-only arguments, meaning that they can only be used as keywords
       rather than positional arguments.

    '''
    # All parameters of `vargs` argument will be wrapped up in a tuple
    for param in vargs:
        # handle `*vargs`
        pass

    # All parameters of `args` argument will be wrapped up in an OrderedDict
    # class
    for key, value in args.items():
        # handle `**args`
        pass
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
