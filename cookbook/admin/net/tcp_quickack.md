# TCP Quick ACK (Disable Delayed ACKs, 延迟确认)

## Introduction

Enable **TCP Quick ACK** mode, disabling *delayed ACKs*.

In quickack mode, `ACK`s are sent immediately,
rather than *delayed* if needed in accordance to normal TCP operation.

The **`TCP_QUICKACK`** flag is not permanent, it only enables a switch to
or from quickack mode. Subsequent operation of the TCP protocol will
once again enter/leave quickack mode depending on internal protocol
processing and factors such as delayed ack timeouts occurring and data
transfer. This option should not be used in code intended to be portable.

Since Linux *2.4.4*.

## Python Recipes

- [TCP Server (IPv4) - Python Cookbook](https://lucas-six.github.io/python-cookbook/cookbook/core/net/tcp_server_ipv4)

## References

<!-- markdownlint-disable line-length -->

- [`TCP_QUICKACK` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#TCP_QUICKACK)
- [RFC 813 - WINDOW AND ACKNOWLEDGEMENT STRATEGY IN TCP (1982.7)](https://datatracker.ietf.org/doc/html/rfc813.html) (Obsoleted)

<!-- markdownlint-enable line-length -->
