#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Formatting Output Cookbook.

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

def test_float_format():
    f = 12345.678
    assert format(f, '0.2f') == '12345.68' # two-digits accuracy
    assert format(f, '>10.2f') == '  12345.68' # right justified
    assert format(f, '<10.2f') == '12345.68  ' # left justified
    assert format(f, '^10.2f') == ' 12345.68 ' # centred
    assert format(f, ',') == '12,345.678' # thousands separator
    assert format(f, '0,.2f') == '12,345.68' # # thousands separator
    assert format(f, 'e') == '1.234568e+04' # exponential notation
    assert format(f, '0.2E') == '1.23E+04' # exponential notation
    
    
def test_int_format():
    i = 2
    assert bin(i) == '0b10' == format(i, '#b') # binary prefix
    assert format(i, 'b') == '10' # binary digit
    assert format(i, '08b') == '00000010' # binary padding
    assert format(i, '#010b') == '0b00000010' # binary prefix & padding
    
    assert hex(i) == '0x2' == format(i, '#x') # hex prefix
    assert format(i, 'x') == '2' # hex digit
    assert format(i, '02x') == '02' # hex padding
    assert format(i, '#04x') == '0x02' # hex prefix & padding
    
    assert oct(i) == '0o2' == format(i, '#o') # Python 2: oct(i) == '02'
    assert format(i, 'o') == '2' # hex digit
    assert format(i, '03o') == '002' # hex padding
    assert format(i, '#05o') == '0o002' # hex prefix & padding


if __name__ == '__main__':
    test_float_format()
    test_int_format()
