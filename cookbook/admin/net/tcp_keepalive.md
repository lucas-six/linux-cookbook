# TCP Keep Alive

## OS Configuration (Linux)

### `tcp_keepalive_time`

Since Linux *2.2*.

The number of seconds a connection needs to be idle before TCP begins sending out keep-alive probes.

(空闲时，启动探测间隔时间（秒）)

```bash
$ cat /proc/sys/net/ipv4/tcp_keepalive_time
7200
$ sysctl net.ipv4.tcp_keepalive_time
net.ipv4.tcp_keepalive_time = 7200

$ sudo sysctl -w net.ipv4.tcp_keepalive_time = 3600
```

See [`tcp_keepalive_time` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_keepalive_time).

### `tcp_keepalive_probes`

Since Linux *2.2*.

The maximum number of TCP keep-alive probes to send before giving up and killing the connection
if no response is obtained from the other end.

(网络不可达时，重发探测次数)

```bash
$ cat /proc/sys/net/ipv4/tcp_keepalive_probes
9
$ sysctl net.ipv4.tcp_keepalive_probes
net.ipv4.tcp_keepalive_probes = 9

$ sudo sysctl -w net.ipv4.tcp_keepalive_probes = 9
```

See [`tcp_keepalive_probes` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_keepalive_probes).

### `tcp_keepalive_intvl`

Since Linux *2.4*.

The number of seconds between TCP keep-alive probes.

(网络不可达时，重发探测间隔时间（秒）)

```bash
$ cat /proc/sys/net/ipv4/tcp_keepalive_intvl
75
$ sysctl net.ipv4.tcp_keepalive_intvl
net.ipv4.tcp_keepalive_intvl = 75

$ sudo sysctl -w net.ipv4.tcp_keepalive_intvl = 25
```

See [`tcp_keepalive_intvl` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_keepalive_intvl).

## Python Recipes

- [TCP Keep Alive - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/net/tcp_keepalive)

## References

- [`SO_KEEPALIVE` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#SO_KEEPALIVE)
- [`TCP_KEEPIDLE` -  tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#TCP_KEEPIDLE)
- [`TCP_KEEPCNT` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#TCP_KEEPCNT)
- [`TCP_KEEPINTVL` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#TCP_KEEPINTVL)
- [`tcp_keepalive_time` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_keepalive_time)
- [`tcp_keepalive_probes` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_keepalive_probes)
- [`tcp_keepalive_intvl` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_keepalive_intvl)
- [tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html)
- [RFC 793 - TRANSMISSION CONTROL PROTOCOL (1981.9)](https://www.rfc-editor.org/rfc/rfc793)
