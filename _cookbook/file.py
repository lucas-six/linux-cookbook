#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''@package _cookbook
File I/O Cookbook.

By reading and writing only large chunks of data even when the user asks for a
single byte, **buffered I/O** is designed to hide any inefficiency in calling
and executing the operating system’s unbuffered I/O routines. The gain will
vary very much depending on the OS and the kind of I/O which is performed (for
example, on some contemporary OSes such as Linux, unbuffered disk I/O can be as
fast as buffered I/O). The bottom line, however, is that buffered I/O will
offer you predictable performance regardless of the platform and the backing
device. Therefore, _it is most always preferable to use buffered I/O rather
than unbuffered I/O_.

The I/O system is built from layers. Text files are constructed by adding a
text encoding/decoding layer on top of a buffered binary-mode file. The
`buffer` attribute simply points at this underlying file. If you access it,
you’ll bypass the text encoding/decoding layer. You could write raw bytes to a
file opened in text mode using this technique.


For **text I/O**, reading line by line is more common.

    `for line in f`

    
For **binary I/O**,

    >>> test_bin_io('_file.data')
    2 bytearray(b'ab')
    2 bytearray(b'cd')
    2 bytearray(b'ef')
    1 bytearray(b'Gf')
    b'ab'
    b'cdefG'
    
For **Memory-mapped I/O**,

    >>> test_mmap('_file.data')
    b'Hello World'


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

import functools
import sys

            
def test_bin_io(filename):
    '''Binary I/O'''
    # Write a binary file
    try:
        with open(filename, 'wb') as f:
            f.write(b'abcdefG')
    except IOError as e:
        error()
        
    # Read fixed-size data directly into buffer without intermediate copying.
    #
    # Unlike `read()` method, `readinto()` method doesn't need to allocate new
    # objects and return them, avoding making extra memory allocations.
    size = 2
    buf = bytearray(size)
    try:
        with open(filename, 'rb') as f:
            for nbytes in iter(functools.partial(f.readinto, buf), 0):
                print(nbytes, buf)
    except IOError as e:
        print('error')
        
    
    # Var-size
    try:
        with open(filename, 'rb') as f:
            print(f.read(2))
            print(f.read(6))
    except IOError as e:
        print('error')
        
        
def test_mmap(filename):
    '''Memory-mapped I/O.
    
    It should be emphasized that memory mapping a file does not cause the
    entire file to be read into memory. That is, it’s not copied into some kind
    of memory buffer or array. Instead, the operating system merely reserves a
    section of virtual memory for the file contents. As you access different
    regions, those portions of the file will be read and mapped into the memory
    region as needed. However, parts of the file that are never accessed simply
    stay on disk. This all happens transparently, behind the scenes.
    
    If more than one Python interpreter memory maps the same file, the
    resulting mmap object can be used to exchange data between interpreters.
    That is, all interpreters can read/write data simultaneously, and changes
    made to the data in one interpreter will automatically appear in the
    others. Obviously, some extra care is required to synchronize things, but
    this kind of approach is sometimes used as an alternative to transmitting
    data in messages over pipes or sockets.
    '''
    import mmap
    import os
    
    # Initially create a binary file and expand it to a desired size.
    size = 10000 # 10K
    try:
        with open(filename, 'wb') as f:
            f.seek(size-1)
            f.write(b'\x00')
    except IOError as e:
        print('error')
    assert os.path.getsize(filename) == size
    
    # Memory map a file
    try:
        with open(filename, 'r+b') as f:
            # Note: If you want to create a memory-mapping for a writable,
            # buffered file, you should flush() the file first. This is
            # necessary to ensure that local modifications to the buffers are
            # actually available to the mapping.
            f.flush()
            
            m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
            assert len(m) == size
            assert m[0:10] == b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            
            # Modify in place
            m[0:11] = b'Hello World'
            m.close()
    except IOError as e:
        print('error')
    
    # Verify the modifications
    try:
        with open(filename, 'rb') as f:
            print(f.read(11))
    except IOError as e:
        print('error')
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
