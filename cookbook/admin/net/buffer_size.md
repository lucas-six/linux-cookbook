# TCP/UDP Buffer Size

## System Configuration (Linux)

```bash
# recv buffer
# - default: 208KB
# - max: 208KB
$ cat /proc/sys/net/core/rmem_max
212992
$ sysctl net.core.rmem_max
net.core.rmem_max = 212992
$ cat /proc/sys/net/core/rmem_default
212992
$ sysctl net.core.rmem_default
net.core.rmem_default = 212992

# send buffer
# - default: 208KB
# - max: 208KB
$ cat /proc/sys/net/core/wmem_max
212992
$ sysctl net.core.wmem_max
net.core.wmem_max = 212992
$ cat /proc/sys/net/core/wmem_default
212992
$ sysctl net.core.wmem_default
net.core.wmem_default = 212992

$ cat /proc/sys/net/ipv4/tcp_rmem
4096    131072  6291456
$ sysctl net.ipv4.tcp_rmem
net.ipv4.tcp_rmem = 4096        131072  6291456
$ cat /proc/sys/net/ipv4/tcp_wmem
4096    16384   4194304
$ sysctl net.ipv4.tcp_wmem
net.ipv4.tcp_rmem = 4096        16384   4194304
$ cat /proc/sys/net/ipv4/tcp_window_scaling
1
$ sysctl -w net.ipv4.tcp_window_scaling = 1
```

## Python Recipes

- [TCP/UDP Buffer Size - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/net/buffer_size)

## References

- [`recv`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/recv.2.en.html)
- [`send`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/send.2.en.html)
- [socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html)
- [`SO_RCVBUF` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#SO_RCVBUF)
- [`SO_SNDBUF` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#SO_SNDBUF)
- [`rmem_default` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#rmem_default)
- [`rmem_max` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#rmem_max)
- [`wmem_default` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#wmem_default)
- [`wmem_max` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#wmem_max)
- [`tcp_rmem` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_rmem)
- [`tcp_wmem` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_wmem)
- [`tcp_window_scaling` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_window_scaling)
