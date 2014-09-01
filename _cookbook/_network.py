#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''@package _cookbook
Networking Programming Cookbook.

  - Synchronous TCP Server
  - Synchronous UDP Server
  - TCP Client
  - UDP Client
  - TCP Handler


## Module

  - socket: Low-level network interface
  - SocketServer: network server framework

## Address Family

  - AF_INET
  - AF_INET6
  - AF_UNIX
  - AF_NETLINK
  - AF_TIPC
  
## Socket Type

  - SOCK_STREAM
  - SOCK_DGRAM

## Socket Mode

  - blocking (default)
  - non-blocking
  - timeout
  
## Socket Option

  - SO_REUSEADDR

    
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

import socket
import errno
import time
import sys
import select
import SocketServer


def _eintr_retry(func, *args):
    '''restart a system call interrupted by EINTR.
    
    @param func system call
    @param args arguments of system call
    @return results of system call
    @exception OSError
    @exception select.error
    '''
    while True:
        try:
            print('BBB\n')
            return func(*args)
        except (OSError, select.error) as e:
            if e.errno != errno.EINTR:
                print('AAA\n')
                raise


class MyTCPServer(object):
    '''TCP Server (Only IPv4).
    '''
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 5 # used by POSIX `listen()`
    
    def __init__(self, address, buf_size=1024, timeout=None):
        '''Create an instance of TCP server.
        
        @param address server address, 2-tuple (host, port)
        @param buf_size receiving buffer size
        @param timeout timeout of socket object. None for blocking, 0.0 for
        non-blocking, others for timeout in seconds (float)
        @exception socket.error
        '''
        self.server_address = address
        self._timeout = timeout
        self._buf_size = buf_size
        
        # Setup
        self.socket = socket.socket(self.address_family, self.socket_type)
        self.socket.settimeout(self._timeout)
        
        # Non-blocking mode
        if self._timeout == 0.0:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind
        self.socket.bind(self.server_address)
        
        # Active
        self.socket.listen(self.request_queue_size)
        
        
    def serve_forever(self, select_timeout=0.5):
        '''Run server.
        
        @param select_timeout timeout used by POSIX `select()`
        @exception select.error
        '''
        while True:
            # Wait for client request
            print('Waiting for client on port {0}...'
                    .format(self.server_address[1]))
                
            # Set I/O multiplexing
            #
            # Polling reduces our responsiveness to a
            # shutdown request and wastes CPU at all other times.
            r, w, e = _eintr_retry(select.select, [self.socket], [], [],
                    select_timeout)
            
            # Handle request without blocking
            if self.socket in r:
                self._handle_request_nonblock()
        
        self.socket.close()
        
        
    def _handle_request_nonblock(self):
        '''Handle one request, without blocking.        
        '''        
        client, addr = self.socket.accept()
        print('Connected by {0}'.format(addr))
        
        # Message Communication
        #
        # Note: put the server’s `while` loop inside the `except` clause of a 
        # `try-except` statement and monitor for `EOFError` or
        # `KeyboardInterrupt` exceptions so that you can close the server’s
        # socket in the `except` or `finally` clauses.
        try:
            while True:
                data = client.recv(self._buf_size)
                if not data:
                    break
                print('Data from client: {0}'.format(data))
                    
                client.sendall('response')
        except socket.error as e:
            print(e)
        finally:
            client.close()
        
        
        
class MyUDPServer(object):
    '''Synchronous UDP Server (Only IPv4).
    '''
    address_family = socket.AF_INET
    socket_type = socket.SOCK_DGRAM
    
    def __init__(self, address, buf_size=1024):
        '''Create an instance of UDP server.
        
        @param address server address, 2-tuple (host, port)
        @param buf_size receiving buffer size
        @exception socket.error
        '''
        self.server_address = address
        self._buf_size = buf_size
        
        # Setup
        self.socket = socket.socket(self.address_family, self.socket_type)
        
        # Bind
        self.socket.bind(self.server_address)
        
        
    def serve_forever(self):
        '''Run server.
        '''
        # Message Communication
        #
        # Note: put the server’s `while` loop inside the `except` clause
        # of a `try-except` statement and monitor for `EOFError` or
        # `KeyboardInterrupt` exceptions so that you can close the server’s
        # socket in the `except` or `finally` clauses.
        try:
            while True:
                print('Waiting for client on port {0}...'.format(self.server_address[1]))
            
                data, addr = self.socket.recvfrom(self._buf_size)
                if not data:
                    break
                print('Data from client {0}: {1}'.format(addr, data))
            
                self.socket.sendto('response', addr)
        except socket.error as e:
            print(e)
        finally:
            self.socket.close()
            
        
def tcp_client(addr, buf_size=1024, reconn=3):
    '''TCP Client.
    
    @param addr server address, 2-tuple of (host, port)
    @param buf_size receiving buffer size
    @param reconn re-connect times
    @exception socket.error
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    wait_time = 1 # in second
    while reconn > 0:
        try:
            sock.connect(addr)
            print('Connected')
        except socket.error as e:
            # reconnect
            if e.errno == errno.ECONNREFUSED:
                reconn -= 1
                time.sleep(wait_time)
                wait_time += 1
                continue
                
            # already connected
            elif e.errno == errno.EISCONN:
                break
                
            # error
            else:
                sock.close()
                raise e
    
    # Message Communication
    try:
        sock.sendall('request\n')
        
        data = sock.recv(buf_size)
        if data:
            print('Data from server: {0}'.format(data))
    except socket.error as e:
        print(e)
    finally:
        sock.close()
        
        
def udp_client(addr, buf_size=1024):
    '''UDP Client.
    
    @param addr server address, 2-tuple of (host, port)
    @param buf_size receiving buffer size
    @exception socket.error
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Message Communication
    try:
        sock.sendto('request\n', addr)
        
        data, addr = sock.recvfrom(buf_size)
        if data:
            print('Data from server {0}: {1}'.format(addr, data))
    except socket.error as e:
        print(e)
    finally:
        sock.close()
        
        
class MyTCPHandler(SocketServer.StreamRequestHandler):
    '''TCP handler by framework "SocketServer"
    '''
    def handle(self):
        print('Connected by {0}'.format(self.client_address))
        
        # Message Communication
        self.data = self.rfile.readline().strip()
        print('Data from client: {0}'.format(self.data))
        self.wfile.write('response')
        
        
def tcp_server(host, port):
    '''SocketServer.TCPServer.
    
    @param host host name or IP of server
    @param port port number of server
    '''
    srv = SocketServer.TCPServer((host, port), MyTCPHandler)
    print('Waiting for client on port {0}...'.format(port))
    srv.serve_forever()
        
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        # Run blocking TCP server
        if sys.argv[1] == '1':
            srv = MyTCPServer(('', 10000))
            srv.serve_forever()
        
        # Run TCP client
        elif sys.argv[1] == '2':
            srv_addr = ('localhost', 10000)
            tcp_client(srv_addr)
            
        # Run synchronous UDP server
        elif sys.argv[1] ==  '3':
            srv = MyUDPServer(('', 10000))
            srv.serve_forever()
            
        # Run UDP client
        elif sys.argv[1] == '4':
            srv_addr = ('localhost', 10000)
            udp_client(srv_addr)
            
        # Run SocketServer.TCPServer
        elif sys.argv[1] == '5':
            tcp_server('', 10000)
            
        # Run non-blocking TCP server
        elif sys.argv[1] == '6':
            srv = MyTCPServer(('', 10000), timeout=0.0)
            srv.serve_forever(select_timeout=0.5)
    
    # usage
    else:
        print('1: Blocking TCP Server')
        print('2: TCP Client')
        print('3: Blocking UDP Server')
        print('4: UDP Client')
        print('5: SocketServer.TCPServer')
        print('6: Non-blocking TCP Server')
