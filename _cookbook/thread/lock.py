#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package _cookbook._thread
Multi-threading using Lock.

A primitive lock is a synchronization primitive that is not owned by a
particular thread when locked. In Python, it is currently the lowest level
synchronization primitive available, implemented directly by the
<code>thread</code> extension module.

A primitive lock is in one of two states, "locked" or "unlocked". It is
created in the unlocked state. It has two basic methods, `acquire()` and
`release()`. When the state is unlocked, `acquire()` changes the state to
locked and returns immediately. When the state is locked, `acquire()` blocks
until a call to `release()` in another thread changes it to unlocked, then the
`acquire()` call resets it to locked and returns. The `release()` method
should only be called in the locked state; it changes the state to unlocked
and returns immediately. If an attempt is made to release an unlocked lock, a
`ThreadError` will be raised.


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

import threading


share = []
lock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, arg, name=None):
        super(MyThread, self).__init__(name=name)
        self.arg = arg


    def run(self):
        print('Run {0}'.format(self.name))

        # Same with:
        #
        #     lock.acquire()
        #     share.append(self.arg)
        #     print(share)
        #     lock.release()
        with lock:
            share.append(self.arg)
            print(share)


def test_lock():
    threads = []
    t1 = MyThread(1)
    t2 = MyThread(2)
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    test_lock()
