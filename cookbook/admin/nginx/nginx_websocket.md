# NGINX: WebSocket Support

## Recipes

```conf
http {
    # WebSocket
    map $http_upgrade $connection_upgrade {
        default upgrade;
        ''      close;
    }
}

server {
    # WebSocket
    location ~^ /ws {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version  1.1;
        proxy_read_timeout  3600s;
        # proxy_set_header  X-Real-IP  $remote_addr;
        # proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}
```

## References

- [NGINX Documentation](https://nginx.org/en/docs/)
