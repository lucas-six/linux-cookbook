# NGINX Configuration: TCP Fast-Open

## Recipes

```conf
# /etc/sysctl.d/30-nginx.conf

net.ipv4.tcp_fastopen = 3
```

```bash
systemctl restart procps.service
```

```conf
http {
    tcp_fastopen on;
}

server {
    listen 443 ssl fastopen=3 http2 default_server;
}
```

## More

- [TCP Fast Open](../../admin/net/tcp_fastopen)

## References

- [Nginx Documentation](https://nginx.org/en/docs/)
