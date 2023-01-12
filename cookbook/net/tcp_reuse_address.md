# TCP Reuse Address

## Introduction

The **`SO_REUSEADDR`** flag (or socket option) tells the kernel to reuse a local socket in
**`TIME_WAIT`** state, without waiting for its natural timeout to expire.

When multiple processes with differing UIDs assign sockets to an identical UDP socket address with *`SO_REUSEADDR`*,
incoming packets can become randomly distributed among the sockets.
Thus, **DONOT** use `SO_REUSEADDR` on UDP.

## Python Recipes

- [TCP Reuse Address - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/socket/tcp_reuse_address)

## References

- [Linux Programmer's Manual - `bind`(2)](https://manpages.debian.org/bullseye/manpages-dev/bind.2.en.html)
- [Linux Programmer's Manual - socket(7)](https://manpages.debian.org/bullseye/manpages/socket.7.en.html)
- [Linux Programmer's Manual - socket(7) - `SO_REUSEADDR`](https://manpages.debian.org/bullseye/manpages/socket.7.en.html#SO_REUSEADDR)
