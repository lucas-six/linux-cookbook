# TCP Reuse Address

## Introduction

The **`SO_REUSEADDR`** flag (or socket option) tells the kernel to reuse a local socket in
**`TIME_WAIT`** state, without waiting for its natural timeout to expire.

When multiple processes with differing UIDs assign sockets to an identical UDP socket address with *`SO_REUSEADDR`*,
incoming packets can become randomly distributed among the sockets.
Thus, **DONOT** use `SO_REUSEADDR` on UDP.

## Python Recipes

- [TCP Reuse Address - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/net/tcp_reuse_address)

## References

- [`bind`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/bind.2.en.html)
- [`SO_REUSEADDR` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#SO_REUSEADDR)
- [socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html)
