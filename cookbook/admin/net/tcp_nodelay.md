# TCP Nodelay (Nagle's Algorithm)

## Instroduction

The **`TCP_NODELAY`** option disables **Nagle algorithm**.

*Nagle's algorithm* works by combining a number of small outgoing messages
and sending them all at once. It was designed to solve "*small-packet problem*".

See [`TCP_NODELAY` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#TCP_NODELAY).

Original algorithm was described in [RFC 896 - Congestion Control in IP/TCP Internetworks (1984.1)](https://www.rfc-editor.org/rfc/rfc896).

## Python Examples or Recipes

- [TCP Server (IPv4) - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/net/tcp_server_ipv4)

## References

<!-- markdownlint-disable line-length -->

- [`TCP_NODELAY` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#TCP_NODELAY)
- [RFC 896 - Congestion Control in IP/TCP Internetworks (1984.1)](https://www.rfc-editor.org/rfc/rfc896) (Obsoleted by [RFC 5681](https://www.rfc-editor.org/rfc/rfc5681))
- [RFC 2001 - TCP Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery Algorithms (1997.1)](https://www.rfc-editor.org/rfc/rfc2001) (Obsoleted by [RFC 5681](https://www.rfc-editor.org/rfc/rfc5681))
- [RFC 2581 - TCP Congestion Control (1999.4)](https://www.rfc-editor.org/rfc/rfc2581) (Obsoleted by [RFC 5681](https://www.rfc-editor.org/rfc/rfc5681))
- [RFC 5681 - TCP Congestion Control (2009.9)](https://www.rfc-editor.org/rfc/rfc5681)
- [Nagle's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Nagle%27s_algorithm)
- [TCP Congestion Control - Wikipedia](https://en.wikipedia.org/wiki/TCP_congestion_avoidance_algorithm)

<!-- markdownlint-enable line-length -->
