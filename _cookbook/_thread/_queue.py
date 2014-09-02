#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package _cookbook._thread
Multi-threading using Queue.

The `Queue` module implements multi-producer, multi-cusumer queues.
It is especially useful in threaded programming when information must be
exchanged safely between multiple threads.

**NOTE**: `collections.deque` is an alternative implementation of unbounded
queues with fast atomic `append()` and `popleft()` operations that do not
require locking.


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
from Queue import Queue


q = Queue(maxsize=10)
        
        
class Producer(threading.Thread):
    def __init__(self, times=1):
        super(Producer, self).__init__(name='Producer')
        self._times = times
        self._item = 'item'

    def run(self):
        while self._times > 0:
            self._times -= 1
            q.put(self._item)
            print('Thread {0} put()'.format(self.name))


class Cusumer(threading.Thread):
    def __init__(self, times=1):
        super(Cusumer, self).__init__(name='Cusumer')
        self._times = times
        self._item = None

    def run(self):
        while self._times > 0:
            self._times -= 1
            self._item = q.get()
            q.task_done()
            print('Thread {0} get() {1}'.format(self.name, self._item))


def test_queue():
    threads = []
    p = Producer(5)
    c = Cusumer(5)
    threads.append(p)
    threads.append(c)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    q.join()


if __name__ == '__main__':
    test_queue()

