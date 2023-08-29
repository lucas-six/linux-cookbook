# NGINX Configuration: CSRF (跨站请求伪造)

## Recipes

```conf
server {
    # CSRF
    # HTTP Referer header
    # https://nginx.org/en/docs/http/ngx_http_referer_module.html#valid_referers
    valid_referers none blocked server_names 127.0.0.1 *.<domain.name>;
    # referer_hash_max_size 2048;
    # referer_hash_bucket_size 64;
    if ($invalid_referer) {
        # rewrite   ^/   https://$host;
        return 403;
    }
}
```

## More

- [Cross-Site Request Forgery (CSRF) (跨站请求伪造)](../csrf)

## References

- [Nginx Documentation](https://nginx.org/en/docs/)
- [Nginx `valid_referers`](https://nginx.org/en/docs/http/ngx_http_referer_module.html#valid_referers)
