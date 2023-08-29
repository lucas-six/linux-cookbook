# TCP Fast Open (TFO)

Since Linux *3.6* (Client) and *3.7* (Server). (RFC 7413)

## System Configuration

```bash
# 0 - disable
# 1 - enabled by clients (default)
# 2 - enabled by servers
# 3 - enabled by both of clients and servers
sysctl -w net.ipv4.tcp_fastopen = 3

echo 3 > /proc/sys/net/ipv4/tcp_fastopen
```

## NGINX configuration

```ini
http {
    tcp_fastopen on;
}

server {
    listen 443 ssl fastopen=3;
}
```

## Python Recipe

```python
import socket

# Server
sock.setsockopt(socket.SOL_SOCKET, socket.TCP_FASTOPEN, 2)

# Client
sock.sendto(data, socket.MSG_FASTOPEN, addr)
```

## `curl` Recipe

```bash
curl --tcp-fastopen <url>
```

## References

- [IP Sysctl - Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/networking/ip-sysctl.html)
- [RFC 7413 - TCP Fast Open](https://datatracker.ietf.org/doc/html/rfc7413.html)
