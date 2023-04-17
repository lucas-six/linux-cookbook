# TCP Selective ACK (SACK)

Since Linux *2.2*. (RFC 2018)

```bash
sysctl -w net.ipv4.tcp_sack = 1
```

## References

- [`tcp_sack` - tcp(7) - Linux Programmer's Manual](https://manpages.debian.org/bullseye/manpages/tcp.7.en.html#tcp_sack)
- [RFC 2018 - TCP Selective Acknowledgment Options](https://datatracker.ietf.org/doc/html/rfc2018.html)
- [RFC 7805 - Moving Outdated TCP Extensions and TCP-Related Documents to Historic or Informational Status (2016.4)](https://www.rfc-editor.org/rfc/rfc7805)
- [RFC 793 - TRANSMISSION CONTROL PROTOCOL (1981.9)](https://www.rfc-editor.org/rfc/rfc793)
