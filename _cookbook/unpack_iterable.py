#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Unpack N elements from iterables.

This works with sequences, tuples, strings, files, iterators, and generators.

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

seq = [1, 2, 3, 4, 5]
v1, v2, v3, v4, v5 = seq

# Skip some elements
v1, _, v3, _, v5 = seq

# Too many elements
try:
    v1, v2, v3 = seq
except ValueError as err:
    # print(err): too many values to unpack

    # Python 3 "star expressions" can be used to address this problem.
    v1, *v2, v3 = seq
    assert isinstance(v2, list)

    # Python 2.7 star parameters in function can be a replacement.
    #def unpack3(v1, v2, *v3):
    #    return v1, v2, v3
    #v1, v2, v3 = unpack3(*seq)
    #assert isinstance(v3 ,tuple)

# Too many variables
try:
    v1, v2, v3, v4, v5, v6 = seq
except ValueError as err:
    # print(err): need more than 5 values to unpack
    pass
