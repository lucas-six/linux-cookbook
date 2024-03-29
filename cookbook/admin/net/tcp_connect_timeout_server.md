# TCP Connect Timeout (Server Side)

## Introduction

The **`tcp_synack_retries`** variable. Since Linux *2.2*.

The maximum number of times a `SYN`/`ACK` segment for a passive TCP connection will be retransmitted.
This number should not be higher than *`255`*.
See [`tcp_synack_retries` - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_synack_retries)

## OS Configuration

```bash
$ cat /proc/sys/net/ipv4/tcp_synack_retries
5
$ sysctl net.ipv4.tcp_synack_retries
net.ipv4.tcp_synack_retries = 5

sysctl -w net.ipv4.tcp_synack_retries = 2
```

```c
// linux kernel 2.6.32
icsk->icsk_rto = min(icsk->icsk_rto << 1, TCP_RTO_MAX)
```

```python
timeout = 1
while tcp_synack_retries:
    tcp_synack_retries -= 1
    timeout += 2 ** (tcp_synack_retries - r)
return timeout
```

## Python Examples or Recipes

- [TCP Server (IPv4) - Python Cookbook](https://lucas-six.github.io/python-cookbook/cookbook/core/net/tcp_server_ipv4)

## References

<!-- markdownlint-disable line-length -->

- [`accept`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/accept.2.en.html)
- [`tcp_synack_retries` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_synack_retries)
- [tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html)
- [RFC 6298 - Computing TCP's Retransmission Timer](https://datatracker.ietf.org/doc/html/rfc6298.html)

<!-- markdownlint-enable line-length -->
