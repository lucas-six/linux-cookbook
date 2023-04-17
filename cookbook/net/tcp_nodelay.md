# TCP Nodelay (Nagle's Algorithm)

## Instroduction

The **`TCP_NODELAY`** option disables **Nagle algorithm**.

*Nagle's algorithm* works by combining a number of small outgoing messages
and sending them all at once. It was designed to solve "*small-packet problem*".

See [Linux Programmer's Manual - tcp(7) - `TCP_NODELAY`](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#TCP_NODELAY).

Original algorithm was described in [RFC 896 - Congestion Control in IP/TCP Internetworks (1984.1)](https://www.rfc-editor.org/rfc/rfc896).

## Python Examples or Recipes

See [TCP Nodelay (Nagle's Algorithm) - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/socket/tcp_nodelay).

## References

<!-- markdownlint-disable line-length -->

- [`TCP_NODELAY` - tcp(7) - Linux Programmer's Manual](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#TCP_NODELAY)
- [RFC 896 - Congestion Control in IP/TCP Internetworks (1984.1)](https://www.rfc-editor.org/rfc/rfc896) (Obsoleted by [RFC 5681](https://www.rfc-editor.org/rfc/rfc5681))
- [RFC 2001 - TCP Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery Algorithms (1997.1)](https://www.rfc-editor.org/rfc/rfc2001) (Obsoleted by [RFC 5681](https://www.rfc-editor.org/rfc/rfc5681))
- [RFC 2581 - TCP Congestion Control (1999.4)](https://www.rfc-editor.org/rfc/rfc2581) (Obsoleted by [RFC 5681](https://www.rfc-editor.org/rfc/rfc5681))
- [RFC 5681 - TCP Congestion Control (2009.9)](https://www.rfc-editor.org/rfc/rfc5681)
- [Nagle's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Nagle%27s_algorithm)
- [TCP Congestion Control - Wikipedia](https://en.wikipedia.org/wiki/TCP_congestion_avoidance_algorithm)

<!-- markdownlint-enable line-length -->
