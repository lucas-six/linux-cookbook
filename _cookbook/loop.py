#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Loop techniques Cookbook.

Loop over index-value pair:

    >>> for index, value in enumerate([1,2,3]):
    ...    print(index, value)
    0 1
    1 2
    2 3
    
        
    >>> for index, value in enumerate([1,2,3], start=1):
    ...    print(index, value)
    1 1
    2 2
    3 3
    
    
Join multiple containers with avoiding nested loops without losing the
readability of the code:

    >>> for item in itertools.chain([1,2,3], ['a','b']):
    ...    print(item)
    1
    2
    3
    a
    b
    
    
Reference implementation of `chain()`:

    def chain(iterators):
        for i in iterators:
            yield from i
    
    
Multiple containers simultaneously:

    >>> for value1, value2 in zip([1,2,3], [7,8,9]):
    ...    print(value1, value2)
    1 7
    2 8
    3 9
    

    >>> for value1, value2 in zip([1,2,3], [7,8,9,10]):
    ...        print(value1, value2)
    1 7
    2 8
    3 9
    
   
    # Python 2: itertools.izip_longest()
    >>> for value1, value2 in itertools.zip_longest([1,2,3], [7,8,9,10]):
    ...     print(value1, value2)
    1 7
    2 8
    3 9
    None 10

   
    # Python 2: itertools.izip_longest()
    >>> for value1, value2 in \
               itertools.zip_longest([1,2,3], [7,8,9,10], fillvalue=0):
    ...    print(value1, value2)
    1 7
    2 8
    3 9
    0 10
    
        
Replace infinitive while loop with an iterator:

    while True:
        a = get()
        if a == b:
            break
        set(a)
        
        ||
        \/
        
    for a in iter(lambda: get(), b):
        set(a)
        

Iterate permutations & combinations,
    
    >>> for item in itertools.permutations([1,2,3]):
    ...    print(item)
    (1, 2, 3)
    (1, 3, 2)
    (2, 1, 3)
    (2, 3, 1)
    (3, 1, 2)
    (3, 2, 1)
        
        
    >>> for item in itertools.permutations([1,2,3], 2):
    ...    print(item)
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)
        
        
    >>> for item in itertools.combinations([1,2,3], 3):
    ...    print(item)
    (1, 2, 3)
     
    
    >>> for item in itertools.combinations([1,2,3], 2):
    ...    print(item)
    (1, 2)
    (1, 3)
    (2, 3)
            
    
    >>> for item in itertools.combinations_with_replacement([1,2,3], 3):
    ...    print(item)
    (1, 1, 1)
    (1, 1, 2)
    (1, 1, 3)
    (1, 2, 2)
    (1, 2, 3)
    (1, 3, 3)
    (2, 2, 2)
    (2, 2, 3)
    (2, 3, 3)
    (3, 3, 3)
    
    
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

import itertools
        

# Sorted order
seq = []
for value in sorted(seq):
    pass
    

# In reverse
seq = []
for value in reversed(seq):
    pass

    
# To change a sequence you are iterating over while inside the loop (for
# example to duplicate certain items), it is recommended that you first make a
# copy.
words = []
for word in words[:]:  # Loop over a slice copy of the entire list.
    if len(word) > 6:
        words.insert(0, word)
            
            
# Dictionary
mydict = {}
for key, value in mydict.items(): # Python 2: mydict.iteritems()
    pass
    
      
class MyIterator(object):
    '''Iterator.
    
    Python supports a concept of iteration over containers. This is
    implemented using two distinct methods (`__iter__()`, and `next()`); these
    are used to allow user-defined classes to support iteration.
    
    To use it,

        >>> for i in MyIterator([1, 2, 3]):
        ...    print(i)
        1
        2
        3
        
    '''
    def __init__(self, seq):
        self._container = seq
        self._index = -1
        

    def __iter__(self):
        return iter(self._container)

    
    def __next__(self):
        if self._index == len(self._container) - 1:
            raise StopIteration
        self._index += 1
        return self._container[self._index]
        
        
def my_generator(n):
    '''Generator

    Python’s _generators_ provide a convenient way to implement the _iterator_
    protocol. If a container object’s `__iter__()` method is implemented as a
    _generator_, it will automatically return an _iterator_ object
    (technically, a _generator_ object) supplying the `__iter__()` and
    `next()` methods.

    The `yield` keyword could be implemented by _iterators_.
    
    To use it,
   
        >>> index = 0
        
        >>> for item in my_generator(0):
        ...    index += 1
        ...    if index > 3: break
        ...    print(item)
        0
        1
        2
        
    To use it with iterator/generator slicing,
            
        >>> for item in itertools.islice(my_generator(0), 5, 9):
        ...    print(item)
        5
        6
        7
        8
        
    **NOTE**: It’s important to emphasize that `islice()` will consume data on
    the supplied iterator. Since iterators can’t be rewound, that is something
    to consider. If it’s important to go back, you should probably just turn
    the data into a list first.
    '''
    while True:
        yield n
        n += 1
        
    # Type Testing
    assert type(my_generator).__name__ == 'function'
    assert type(my_generator(10)).__name__ == 'generator'
    import types
    assert isinstance(my_generator, types.FunctionType)
    assert isinstance(my_generator(10), types.GeneratorType)
        

def test_filter():
    # The easiest way to filter a sequence data is often to use a list (or
    # dictionary, tuple, etc.) comprehension.
    l = [1, 3, 5, -2, 0, 8]
    assert [i for i in l if i > 0] == [1, 3, 5, 8]
    assert [i if i > 0 else 0 for i in l] == [1, 3, 5, 0, 0, 8]
    d = {'A': 1, 'B': 2, 'C': 3}
    assert {key: value for key, value in d.items() if value > 1} == \
            {'B': 2, 'C': 3}  # Python 2: d.iteritems()
            
    # One potential downside of using a list comprehension is that it might
    # produce a large result if the original input is large. If this is a
    # concern, generator expression could be used to produce the filtered
    # values iteratively.
    for i in (i for i in l if i > 0):
        pass
        
    # Sometimes, the filtering criteria cannot be easily expressed in a list
    # comprehension or generator expression. For example, suppose that the
    # filtering process involves exception handling or some other complicated
    # detail.
    #
    # NOTE: the `filter()` returns a list in python 2, and an iterable in
    # Python 3.
    def is_int(val):
        try:
            int(val)
            return True
        except ValueError:
            return False
    assert list(filter(is_int, ['1', '-', '2', 'N/A', '-'])) == ['1', '2']

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    test_filter()
