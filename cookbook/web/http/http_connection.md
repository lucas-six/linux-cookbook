# HTTP Connection Management

**HTTP** = HyperText Transfer Protocol

## TCP

```ini
# sysctl.conf

# reduce TCP connect time (handshaking time)
net.ipv4.tcp_syn_retries           = 2  # reduce it (`socket.TCP_SYNCNT`)
net.ipv4.tcp_synack_retries        = 2  # reduce it

# TCP Keep-Alive
net.ipv4.tcp_keepalive_time        = 1800  # default 7200 (since Linux 2.2)
net.ipv4.tcp_keepalive_probes      = 9  # default 9 (since Linux 2.2)
net.ipv4.tcp_keepalive_intvl       = 15

# enable TCP RFC-1337
net.ipv4.tcp_rfc1337               = 1
```

- [Enable **Persistent Connection** (*TCP Keep-Alive*, *`socket.SO_KEEPALIVE`*)](../../admin/net/tcp_keepalive)
- [Disable *Nagle Algorithm*, enable *`socket.TCP_NODELAY`*](../../admin/net/tcp_nodelay)
- [Disable *Delayed ACK*, enable **TCP Quick ACK** (*`socket.TCP_QUICKACK`*)](../../admin/net/tcp_quickack)
- [Fix *TIME-WAIT Assassination Hazards* (TIME-WAIT 暗杀), enable **`tcp_rfc1337`**](../../admin/net/tcp_rfc1337)

### Keep-Alive

When a client wants to close the connection, send:

```http
Connection: keep-alive
Proxy-Connection: keep-alive

Connection: close
```

## More

- TCP connect time (*handshaking time*)
  - [**`tcp_syn_retries`** (`TCP_SYNCNT`) for client](../../admin/net/tcp_connect_timeout_client)
  - [**`tcp_synack_retries`** for server](../../admin/net/tcp_connect_timeout_server)

## References

<!-- markdownlint-disable line-length -->

- [HTTP - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- David Gourley & Brian Totty. *HTTP: The Definitive Guide* (2002) ISBN: 978-1-56592-509-0 (《HTTP权威指南》)
- [RFC 2616 - Hypertext Transfer Protocol -- HTTP/1.1 (1999)](https://www.rfc-editor.org/rfc/rfc2616) (Obsoleted by [RFC 9112 - HTTP/1.1 (2022.6)](https://www.rfc-editor.org/rfc/rfc9112))
- [RFC 2068 - Hypertext Transfer Protocol -- HTTP/1.1 (1997.1)](https://www.rfc-editor.org/rfc/rfc2068) (Obsoleted by [RFC 9112 - HTTP/1.1 (2022.6)](https://www.rfc-editor.org/rfc/rfc9112))
- [RFC 7230 - Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing (2014)](https://www.rfc-editor.org/rfc/rfc7230) (Obsoleted by [RFC 9112 - HTTP/1.1 (2022.6)](https://www.rfc-editor.org/rfc/rfc9112))
- [RFC 9112 - HTTP/1.1 (2022.6)](https://www.rfc-editor.org/rfc/rfc9112)

<!-- markdownlint-enable line-length -->
