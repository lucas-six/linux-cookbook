# TCP Fast Open (TFO)

Since Linux *2.6.34*. (RFC 7413)

## System Configuration

```bash
sysctl -w net.ipv4.tcp_fastopen = 3  # 1 by default

echo 3 > /proc/sys/net/ipv4/tcp_fastopen
```

## NGINX configuration

```ini
http {
    tcp_fastopen on;
}

server {
    listen  443 ssl fastopen=3 http2 default_server;
}
```

## Python Recipe

```python
import socket

sock.setsockopt(socket.SOL_SOCKET, socket.TCP_FASTOPEN, 3)
```

## `curl` Recipe

```bash
curl --tcp-fastopen <url>
```

## References

- [IP Sysctl - Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/networking/ip-sysctl.html)
- [RFC 7413 - TCP Fast Open](https://datatracker.ietf.org/doc/html/rfc7413.html)
