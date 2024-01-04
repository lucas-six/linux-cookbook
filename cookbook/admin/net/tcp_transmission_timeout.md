# TCP Transmission Timeout

## Introduction

The **`tcp_retries1`** and **`tcp_retries2`** variable. Since Linux *2.2*.

## System Configuration (Linux)

```bash
$ cat /proc/sys/net/ipv4/tcp_retries1
3
$ sysctl net.ipv4.tcp_retries1
net.ipv4.tcp_retries1 = 3
$ cat /proc/sys/net/ipv4/tcp_retries2
15
$ sysctl net.ipv4.tcp_retries2
net.ipv4.tcp_retries2 = 15

sysctl -w net.ipv4.tcp_retries1 = 3
sysctl -w net.ipv4.tcp_retries2 = 5
```

## More Details

*Karn's algorithm*:

Retransmission: *RTO* (Retransmission Time-Out), *RTT* (Round Trip Time),

```plaintext
new_RTTs = (1 - α) × (old_RTTs) + α × (new_RTT_sample), 0 <= α < 1 (0.125 recommended)
RTO = RTTs + 4 × RTTd
new_RTTd = (1 - β) × (old_RTTd) + β × |RTTs - new_RTT_sample|, 0 <= β < 1 (0.25 recommended)
```

See [RFC 6298](https://datatracker.ietf.org/doc/html/rfc6298.html).

## Python Recipes

- [TCP Server (IPv4) - Python Cookbook](https://lucas-six.github.io/python-cookbook/cookbook/core/net/tcp_server_ipv4)

## References

<!-- markdownlint-disable line-length -->

- [`recv`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/recv.2.en.html)
- [`send`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/send.2.en.html)
- [`SO_RCVTIMEO` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#SO_RCVTIMEO)
- [`SO_SNDTIMEO` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#SO_SNDTIMEO)
- [`tcp_retries1` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_retries1)
- [`tcp_retries2` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_retries2)
- [RFC 6298 - Computing TCP's Retransmission Timer](https://datatracker.ietf.org/doc/html/rfc6298.html)

<!-- markdownlint-enable line-length -->
