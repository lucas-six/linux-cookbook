# TCP RFC 1337 - TIME-WAIT Assassination Hazards (TIME-WAIT 暗杀)

## OS Configuration

```bash
$ cat /proc/sys/net/ipv4/tcp_rfc1337
0
$ sysctl net.ipv4.tcp_rfc1337
net.ipv4.tcp_rfc1337 = 0

$ sudo sysctl -w net.ipv4.tcp_rfc1337 = 1
```

## References

- [`tcp_rfc1337` - tcp(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/tcp.7.en.html#tcp_rfc1337)
- [RFC 1337 - TIME-WAIT Assassination Hazards in TCP (1992.5)](https://datatracker.ietf.org/doc/html/rfc1337.html)
- [RFC 7805 - Moving Outdated TCP Extensions and TCP-Related Documents to Historic or Informational Status (2016.4)](https://datatracker.ietf.org/doc/html/rfc7805.html)
