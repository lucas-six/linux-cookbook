#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Object-Oriented Programming (OOP) Cookbook.

Built-in attributes:

    Class attributes:

        - __name__   : string name of class
        - __doc__    : documentation string
        - __bases__  : tuple of class's base classes
        - __slots__  : list of attribute names (reduce memory)

    Instance attributes:

        - __doc__    : documentation string
        - __class__  : class for instance
        - __module__ : module where class is defined
        
Built-in methods:

    - __init__()     : constructor
    - __str__()      : string representation, str(obj)
    - __len__()      : length, len(obj)
    
    # Context Manager
    - __enter__()
    - __exit__()
    
    # Iterator
    - __iter__()
    - __next__()
    - __reversed__()

Built-in functions:

    - isinstance(obj, cls)
    - issubclass(sub_cls, sup_cls)

    
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

class A(object):
    '''A class.
    
        >>> assert isinstance(A(), A)
        
    '''

    # Python does not provide any internal mechanism track how many instances
    # of a class have been created or to keep tabs on what they are. The best
    # way is to keep track of the number of instances using a class attribute.
    num_of_instances = 0

    def __init__(self, a1=None, a2=None):
        A.num_of_instances += 1
        self.public_instance_attribute = a1
        self.private_instance_attribute = a2
        

    def public_instance_method(self):
        return (A.num_of_instances,
                self.publuc_instance_attribute,
                self.private_instance_attribute)
                
    
    def _private_instance_method(self):
        pass
        

    @staticmethod
    def static_method():
        return A.num_of_instances
        

    @classmethod
    def class_method(cls):
        return cls.__name__
        
        
class B(A):
    '''Subclass of A.
    
        >>> assert issubclass(B ,A)
    
    '''

    def __init__(self, b, a1=None, a2=None):
        super(B, self).__init__(a1, a2)
        self.b = b
        
        
    def public_instance_method(self):
        print('Override method of {0}'.format(self.__class__.__bases__[0]))
        
        
    def new_method(self):
        print('New method without inheritance from {0}'
                .format(self.__class__.__bases__[0]))    
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
