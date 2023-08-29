# NGINX Global Configurations

```bash
ln -s nginx.conf /etc/nginx/nginx.conf
nginx -t
```

## Basic

```conf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /dev/null debug;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

# Override the `ulimit -n`
worker_rlimit_nofile 65535;

events {
    worker_connections 8192;
    multi_accept on;
    use epoll;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    charset       utf-8;

    # default
    # log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                   '$status $body_bytes_sent "$http_referer" '
    #                   '"$http_user_agent" "$http_x_forwarded_for"';

    log_format  main    '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    server_tokens                  off;
    server_names_hash_max_size     512;
    server_names_hash_bucket_size  256;

    sendfile                       on;
    tcp_nopush                     on;
    tcp_nodelay                    on;
    keepalive_timeout              30s;

    types_hash_max_size            1024;

    client_body_timeout            20s;
    client_header_timeout          10s;
    send_timeout                   30s;
    client_header_buffer_size      4k;
    client_body_buffer_size        32k;
    large_client_header_buffers    4 16k;
    client_max_body_size           8m;

    # GZip
    gzip  on;
    gzip_http_version  1.1;
    gzip_types  text/plain text/css text/javascript application/javascript application/x-javascript application/json text/xml application/xml application/xml+rss image/svg+xml;
    gzip_disable  "msie6";
    gzip_vary  on;
    gzip_proxied  any;
    gzip_comp_level  6;
    gzip_buffers  16 8k;

    proxy_http_version  1.1;
    proxy_set_header    Host               $host;
    proxy_set_header    X-Real-IP          $remote_addr;
    proxy_set_header    X-Forwarded-For    $proxy_add_x_forwarded_for;
    proxy_set_header    X-Forwarded-Proto  $scheme;
    proxy_connect_timeout  1s;
    proxy_ignore_client_abort off;
    proxy_buffering     on;
    proxy_buffer_size   16k;
    proxy_buffers       8 8k;
    proxy_busy_buffers_size  32k;
    proxy_max_temp_file_size  2048m;

    # uWSGI
    uwsgi_connect_timeout 1s;
    uwsgi_ignore_client_abort off;
    uwsgi_buffering on;
    uwsgi_buffer_size 16k;
    uwsgi_buffers 8 8k;
    uwsgi_busy_buffers_size 32k;
    uwsgi_temp_file_write_size 32k;

    # FastCGI
    fastcgi_connect_timeout  1s;
    fastcgi_ignore_client_abort off;
    fastcgi_buffering on;
    fastcgi_buffer_size 16k;
    fastcgi_buffers     8       8k;
    fastcgi_busy_buffers_size   32k;
    fastcgi_temp_file_write_size 32k;

    # SSL/TLS
    ssl_session_timeout 30m;
    ssl_session_cache shared:SSL:20m;
    ssl_session_tickets on;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1.2 TLSv1.3;

    include /etc/nginx/conf.d/*.conf;
}
```

## PFS with DH

![TLS False Start](https://leven-cn.github.io/linux-cookbook/imgs/tls-false-start.png)

```bash
# Perfect Forward Secrecy, PFS with Diffie-Hellman, DH algorithm
openssl dhparam -out /etc/nginx/ssl_dh.params 4096
```

```conf
http {
    # support for TLS False Start
    # enable Forward Secrecy
    ssl_prefer_server_ciphers on;  # 缓解 BEAST 攻击
    ssl_dhparam ssl_dh.params;  # Perfect Forward Secrecy, PFS with Diffie-Hellman, DH algorithm
}
```

## Log

### syslog

```conf
http {
    error_log syslog:server=127.0.0.1,facility=local5 notice;
    access_log syslog:server=127.0.0.1,facility=local6,severity=info,nohostname main;
}
```

### FileBeat Log Format

```conf
http {
    # Log to FileBeat-7.4
    log_format  filebeat_json   '{"nginx.remote_addr": "$remote_addr",'
                                '"nginx.remote_user": "$remote_user",'
                                '"nginx.time_local": "$time_local",'
                                '"nginx.request": "$request",'
                                '"nginx.status": "$status",'
                                '"nginx.body_bytes_sent": "$body_bytes_sent",'
                                '"nginx.http_referer": "$http_referer",'
                                '"nginx.http_user_agent": "$http_user_agent",'
                                '"nginx.uri": "$uri",'
                                '"nginx.server_addr": "$server_addr",'
                                '"nginx.host": "$host",'
                                '"nginx.request_time": "$request_time",'
                                '"nginx.http_x_forwarded_for": "$http_x_forwarded_for",'
                                '"nginx.upstream_addr": "$upstream_addr",'
                                '"nginx.upstream_response_time": "$upstream_response_time",'
                                '"nginx.upstream_http_ctx_transaction_id": "$upstream_http_ctx_transaction_id"}';
}
```

## More

- [Zero-Copy: `sendfile()` - Linux Cookbook](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/zero_copy)

## References

- [Nginx Documentation](https://nginx.org/en/docs/)
