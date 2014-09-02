#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package _cookbook._thread
Multi-threading Programming.

The `threading` module constructs higher-level threading interfaces on top of
the lower level `thread` module.

**NOTE**: In CPython, due to the Global Interpreter Lock (GIL), only one
thread can execute Python code at once (even though certain
performance-oriented libraries might overcome this limitation).If you want
your application to make better use of the computational resources of
multi-core machines, you are advised to use multiprocessing. However,
threading is still an appropriate model if you want to run multiple I/O-bound
tasks simultaneously. In other words, I/O bound Python applicaitons stand a
much better chance of being able to take advantage of a multithreaded
environment than CPU-bound one.

**NOTE**: While the `import` machinery is thread-safe, there are two key
restrictions on threaded imports due to inherent limitations in the way that
thread-safety is provided:

    - Firstly, other than in the main module, an `import` should not have the
      side effect of spawning a new thread and then waiting for that thread in
      any way. Failing to abide by this restriction can lead to a deadlock if
      the spawned thread directly or indirectly attempts to import a module.

    - Secondly, all `import` attempts must be completed before the interpreter
      starts shutting itself down. This can be most easily achieved by only
      performing imports from non-daemon threads created through the threading
      module. Daemon threads and threads created directly with the `thread`
      module will require some other form of synchronization to ensure they do
      not attempt imports after system shutdown has commenced. Failure to
      abide by this restriction will lead to intermittent exceptions and
      crashes during interpreter shutdown (as the late imports attempt to
      access machinery which is no longer in a valid state).

      
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
