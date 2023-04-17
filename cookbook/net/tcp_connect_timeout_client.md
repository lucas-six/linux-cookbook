# TCP Connect Timeout (Client Side)

## Introduction

The **`tcp_syn_retries`** variable. Since Linux *2.2*.

The maximum number of times initial `SYN`s for an active TCP connection attempt will be retransmitted.
This value should not be higher than *`255`*. The default value is *`6`*,
which corresponds to retrying for up to approximately *127 seconds*.

Before Linux *3.7*, the default value was *`5`*,
which (in conjunction with calculation based on other kernel parameters)
corresponded to approximately *180 seconds*.

See [Linux - `tcp_syn_retries`](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#tcp_syn_retries)

## OS Configuration

```bash
$ cat /proc/sys/net/ipv4/tcp_syn_retries
6
$ sysctl net.ipv4.tcp_syn_retries
net.ipv4.tcp_syn_retries = 6

sysctl -w net.ipv4.tcp_syn_retries = 2
```

```c
// linux kernel 2.6.32
icsk->icsk_rto = min(icsk->icsk_rto << 1, TCP_RTO_MAX)
```

## Python Examples or Recipes

See [TCP Connect Timeout (Client Side) - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/socket/tcp_connect_timeout_client).

## References

<!-- markdownlint-disable line-length -->

- [`tcp_syn_retries` - tcp(7) - Linux Programmer's Manual](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#tcp_syn_retries)
- [RFC 6298 - Computing TCP's Retransmission Timer](https://datatracker.ietf.org/doc/html/rfc6298.html)

<!-- markdownlint-enable line-length -->
