# TCP Connect Timeout (Server Side)

## Introduction

The **`tcp_synack_retries`** variable. Since Linux *2.2*.

The maximum number of times a `SYN`/`ACK` segment for a passive TCP connection will be retransmitted.
This number should not be higher than *`255`*.
See [Linux - `tcp_synack_retries`](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#tcp_synack_retries)

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

## Python Examples or Recipes

See [TCP Connect Timeout (Server Side) - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/socket/tcp_connect_timeout_server).

## References

<!-- markdownlint-disable line-length -->

- [Linux Programmer's Manual - `accept`(2)](https://manpages.debian.org/bullseye/manpages-dev/accept.2.en.html)
- [Linux Programmer's Manual - tcp(7)](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html)
- [Linux Programmer's Manual - tcp(7) - `tcp_synack_retries`](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#tcp_synack_retries)
- [RFC 6298 - Computing TCP's Retransmission Timer](https://datatracker.ietf.org/doc/html/rfc6298.html)

<!-- markdownlint-enable line-length -->
