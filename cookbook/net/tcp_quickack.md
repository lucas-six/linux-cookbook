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

- [TCP Quick ACK (Disable Delayed ACKs, 延迟确认) - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/socket/tcp_quickack)

## References

<!-- markdownlint-disable line-length -->

- [`TCP_QUICKACK` - tcp(7) - Linux Programmer's Manual](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#TCP_QUICKACK)
- [RFC 813 - WINDOW AND ACKNOWLEDGEMENT STRATEGY IN TCP (1982.7)](https://www.rfc-editor.org/rfc/rfc813) (Obsoleted)

<!-- markdownlint-enable line-length -->
