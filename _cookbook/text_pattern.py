#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook
Text Pattern Cookbook.

  - Regular Expression (RE): re
  - Shell-style Wildcards: fnmatch, glob


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

import os


def test_re_pattern():
    '''Regular Expression (RE) pattern.
    
    re1|re2 - or
    re1.re2 - any character except `\n`
    ^str - start of string
    str$ - end of string
    re* - 0+ occurrences
    re+ - 1+ occurrences
    re? - 0 or 1 occurrences
    re{N} - N occurrences
    re{M,N} - from M to N occurrences
    [...] - any single character from character set
    [x-y] - any single character from x to y
    [^...] - NOT any character from character set
    (...) - subgroup
    
    \d - digit, `[0-9]`
    \D - NOT digit, `[^0-9]`
    \w - alphanumeric character, `[A-Za-z0-9_]`
    \W - NOT alphanumeric character, `[^A-Za-z0-9_]`
    \s - white space, `[ \n\t\r\v\f]`
    \S - NOT white space, `[^ \n\t\r\v\f]`
    \bword\b - word boundary
    \A - ^
    \Z - $
    
    '''
    import re
    
    # Compile pattern object
    pattern = re.compile(r'patern-string')
    
    # Get match object
    match = pattern.match('string')          # Search from beginning
    match = pattern.search('string')         # Search until end

    # Get match object list with scanning the whole string
    match_list = pattern.findall('string')

    # Loop over a iterator with scanning the whole string
    for match in pattern.finditer('string'): 
        # handle match
        pass
    
    # Handle match object
    if match is not None:          # Match found
        result = match.group()     # string
        pos_start = match.start()  # int
        pos_end = match.end()      # int
        pos = match.span()         # tuple: (pos_start, pos_end)
    else:
        # Not match
        pass
    
    # Search and replace with strings
    # repl_tuple = (repl_str, count)
    repl_str = pattern.sub('replacement', 'origin', count=0)
    repl_tuple = pattern.subn('replacement', 'origin', count=0)
    
    # Search and replace with strings returned by functions
    def repl_func(match_obj):
        if match_obj.group() == 'something':
            return 'string 1'
        else:
            return 'string 2'
    repl_str = pattern.sub(repl_func, 'string', count=0)
    repl_tuple = pattern.subn(repl_func, 'string', count=0)    

    # Split strings on any of multiple delimiters
    #
    # **NOTE**: When using `re.split()`, you need to be a bit careful should
    # the regular expression pattern involve a capture group enclosed in
    # parentheses. If capture groups are used, then the matched text is also
    # included in the result.
    s = 'a b; cd, efg,hijkl,     mn'
    assert re.split(r'[;,\s]\s*', s) == ['a','b','cd','efg','hijkl','mn']
    assert re.split(r'(;|,|\s)\s*', s) == \
            ['a',' ','b',';','cd',',','efg',',','hijkl',',','mn']
    assert re.split(r'(?:;|,|\s)\s*', s) == ['a','b','cd','efg','hijkl','mn']


def test_shell_pattern():
    '''Shell-style wildcards pattern matching.
    
    Pattern | Meaning
    ---------------------------------------------
    *       | matches everything
    ---------------------------------------------
    ?       | matches any single character
    ---------------------------------------------
    [seq]   | matches any character in _seq_
    ---------------------------------------------
    [!seq]  | matches any character not in _seq_
    ---------------------------------------------
    
    For a literal match, wrap the meta-characters in brackets. Note that the
    filename separator ('/' on Unix) is not special to `fnmatch` module.
    
    Unlike `fnmatch.fnmatch()`, `glob` module treats file names beginning with
    a dot (.) as special cases.
    
    **NOTE**: The matching performed by `fnmatch` module sits somewhere
    between the functionality of simple string methods, such as
    `startswith()`, `endswith()`, and the full power of regular expressions.
    If you're just trying to provide a simple mechanism for allowing wildcards
    in data processing operations, it's often a reasonable solution.
    '''
    import fnmatch
    #import glob
    
    assert fnmatch.fnmatch('aaa.txt', '*.txt') == True
    assert fnmatch.fnmatch('aaa.txt', '?aa.txt') == True

    if os.name == 'posix': # On POSIX
        assert fnmatch.fnmatch('aaa.txt', '*.TXT') == False
    elif os.name == 'nt': # On Windows
        assert fnmatch.fnmatch('aaa.txt', '*.TXT') == True
        
    # Both POSIX and Windows (Case-insensitive)
    assert fnmatch.fnmatchcase('aaa.txt', '*.TXT') == False
    
    # Filter
    assert fnmatch.filter(['a.txt','b.txt', 'c.log'], '*.txt') == \
            ['a.txt','b.txt']
    
    
if __name__ == '__main__':
    test_re_pattern()
    test_shell_pattern()
