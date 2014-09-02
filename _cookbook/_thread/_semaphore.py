#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package _cookbook._thread
Multi-threading using Semaphore.

A primitive semaphore is one of the oldest synchronization primitives in the
history of computer science, invented by the early Dutch computer scientist
Edsger W. Dijkstra (he used `P()` and `V()` instead of `acquire()` and
`release()`).

A semaphore manages an internal counter which is decremented by each
`acquire()` call and incremented by each `release()` call. The counter can
never go below zero; when `acquire()` finds that it is zero, it blocks,
waiting until some other thread calls `release()`.


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

import threading


share = []
MAX_COUNTS = 5
semaphore = threading.BoundedSemaphore(MAX_COUNTS)
        
        
class Producer(threading.Thread):
    def __init__(self, arg):
        super(Producer, self).__init__(name='Producer')
        self.arg = arg


    def run(self):
        print('Run {0}'.format(self.name))
        with semaphore:
            print('Thread {0}: Semaphore value is {1}'.\
                    format(self.name, semaphore._Semaphore__value))
            share.append(self.arg)
            print(share)


class Cusumer(threading.Thread):
    def __init__(self):
        super(Cusumer, self).__init__(name='Cusumer')
        self.arg = None


    def run(self):
        print('Run {0}'.format(self.name))
        with semaphore:
            print('Thread {0}: Semaphore value is {1}'.\
                    format(self.name, semaphore._Semaphore__value))
            if len(share) > 0:
                self.arg = share.pop()
            print(share)


def test_semaphore():
    '''Test multithreading using Semaphore.'''
    threads = []
    t1 = Producer(1)
    t2 = Cusumer()
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    test_semaphore()
