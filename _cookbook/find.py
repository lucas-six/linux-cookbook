#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Find the largest or smallest N items in a collection.

**NOTE**: If you are looking for the _N_ smallest or largest items, and _N_ is
small compared to the overall size of the collection, the `nsmallest()` and
`nlargest()` methods of `heapq` module provide superior performance.

For larger _N_, it is more efficient to use the `sorted()` function first, and
take a slice. Also, when `N==1`, it is more efficient to use the built-in
`min()` and `max()` functions.

**NOTE**: When doing these calculations, be aware that `zip()` creates an
iterator that can only consumed once.


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

import heapq


# Find in a list of integers
seq = [1, 8, 2, 23, 7, -2, 18, 23, 42, 37, 2]
assert heapq.nlargest(3, seq) == [42, 37, 23]
assert heapq.nsmallest(3, seq) == [-2, 1, 2]


# Find in a list of dictionaries
list_of_dict = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.74},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name':'ACME', 'shares': 75, 'price': 115.65}
]
assert heapq.nsmallest(3, list_of_dict, key=lambda s: s['price']) == [
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.74}
        ]
        
        
# Find in a dictionary
d = {
        'IBM': 91.1,
        'AAPL': 543.22,
        'FB': 21.09
}
assert min(zip(d.values(), d.keys())) == (21.09, 'FB')
assert max(zip(d.values(), d.keys())) == (543.22, 'AAPL')


# Order a list as a heap, transformed in-place, in linear time
heapq.heapify(seq)


# Pop and return the smallest item from the heap, maintaining the heap
# invariant.
try:
    assert heapq.heappop(seq) == -2
except IndexError as e:
    # Heap is empty
    pass
