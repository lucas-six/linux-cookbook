#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Sort a collection.

The reference implementation of itemgetter() as follows:

    def itemgetter(*items):
        if len(items) == 1:
            item = items[0]
            def g(obj):
                return obj[item]
        else:
            def g(obj):
                return tuple(obj[item] for item in items)
        return g
        
        
The reference implementation of attrgetter() as follows:

    def attrgetter(*items):
        if len(items) == 1:
            attr = items[0]
            def g(obj):
                return resolve_attr(obj, attr)
        else:
            def g(obj):
                return tuple(resolve_attr(obj, attr) for attr in items)
        return g

    def resolve_attr(obj, attr):
        for name in attr.split("."):
            obj = getattr(obj, name)
        return obj


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

import operator


d = [
    {'name': 'b', 'value': 3},
    {'name': 'a', 'value': 2},
    {'name': 'c', 'value': 1}
]

# Sort a list of dictionaries by name
assert sorted(d, key=operator.itemgetter('name')) == [
    {'name': 'a', 'value': 2},
    {'name': 'b', 'value': 3},
    {'name': 'c', 'value': 1}
]

# Sort a list of dictionaries by value
assert sorted(d, key=operator.itemgetter('value')) == [
    {'name': 'c', 'value': 1},
    {'name': 'a', 'value': 2},
    {'name': 'b', 'value': 3}
]


# Sort a list of dictionaries by two keys
d = [
    {'name': 'b', 'v': 3, 'v2': 2},
    {'name': 'a', 'v': 3, 'v2': 1},
    {'name': 'c', 'v': 2, 'v2': 3}
]

assert sorted(d, key=operator.itemgetter('v', 'v2')) == [
    {'name': 'c', 'v': 2, 'v2': 3},
    {'name': 'a', 'v': 3, 'v2': 1},
    {'name': 'b', 'v': 3, 'v2': 2}
]


# Sort objects without native comparison support 
class App:
    def __init__(self, id):
        self.id = id
        
apps = [App(1), App(2), App(3)]
assert sorted(apps, key=operator.attrgetter('id'))
