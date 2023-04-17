# NGINX Configuration

## Global Configuration

### PFS with DH

![TLS False Start](https://leven-cn.github.io/linux-cookbook/imgs/tls-false-start.png)

```bash
# Perfect Forward Secrecy, PFS with Diffie-Hellman, DH algorithm
openssl dhparam -out /etc/nginx/ssl_dh.params 4096
```

```conf
# /etc/nginx/nginx.conf

# support for TLS False Start
# enable Forward Secrecy
ssl_prefer_server_ciphers on;  # 缓解 BEAST 攻击
ssl_dhparam ssl_dh.params;  # Perfect Forward Secrecy, PFS with Diffie-Hellman, DH algorithm
```

### TCP Fast-Open

```conf
# /etc/sysctl.d/30-nginx.conf

net.ipv4.tcp_fastopen = 3
```

```bash
systemctl restart procps.service
```

### `zstd` Support

```conf
# /etc/nginx/nginx.conf
# --add-module=/path/to/zstd-nginx-module

http {
    zstd on;
    zstd_dict_file /path/to/dict;
    # zstd_types text/html;
    # zstd_comp_level 11;
    # zstd_min_length 256;  # in bytes
    # zstd_buffers 32 4k | 16 8k;
    # zstd_static off;
}
```

### TLS False Start / Forward Secrecy

```conf

```

### Validate Configuration

```bash
ln -s nginx.conf /etc/nginx/nginx.conf
nginx -t
```

## vHost Configuration

```conf
# conf.d/vhost.conf

server {
    listen  443 ssl http2 default_server;
    # listen  [::]:443 ssl default_server ipv6only=on;
    server_name  <domain.name>;

    access_log  /var/log/nginx/xxx.access.log main;
    error_log  /var/log/nginx/error.log error;

    ssl_certificate      /etc/nginx/ssl/xxx.pem;
    ssl_certificate_key  /etc/nginx/ssl/xxx.key;

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

    # XSS Prevention
    add_header X-Frame-Options 'SAMEORIGIN';  # 只允许本网站的frame嵌套
    add_header X-XSS-Protection '1; mode=block';  # 开启XSS过滤器
    add_header X-Content-Type-Options 'nosniff';  # 禁止嗅探文件类型

    client_max_body_size  75M;  # max upload size

    root  /var/spool/nginx/xxx-root;
    location / {
        index  beian.html index.html;
        try_files  $uri $uri/ =404;
        error_page  405 =200 https://$host$request_uri;
        expires  3600;
    }

    # static files
    location = /favicon.ico {
        access_log  off;
        expires max;
    }
    location ~* \.(txt)$ {
        access_log  off;
        expires max;
    }
    location ~* \.(css|js|svg)$ {
        root <static-path>;
        access_log  off;
        expires 120d;
    }
    location ~* \.(jpg|png|mp3|mp4)$ {
        root <static-path>;
        access_log  off;
        expires max;
    }

    # API
    location ~* ^/(api) {
        proxy_pass  http://127.0.0.1:8000;
    }

    # Kibana
    location /_kibana {
        access_log  off;
        proxy_pass  http://kibana_servers/;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_cache_bypass $http_upgrade;
        rewrite ^/_kibana/(.*)$ /$1 break;

        # auth_basic  "Restricted Access";
        # auth_basic_user_file  /etc/nginx/htpasswd.users;
    }

    location ~ /\.ht {
        deny  all;
    }
    location ~/.env {
        return 444;
    }

    # HEAD
    if ($request_method ~ ^(HEAD)$ ) {
        return 200 "All OK";
    }
}

server {
    listen  80;
    server_name  <domain.name>;
    return  301 https://$host$request_uri;
}
```

### Basic Auth

```bash
apt install apache2-utils  # 安装htpasswd
htpasswd -bc /etc/nginx/<htpasswd.users> <用户名> <密码>
```

```conf
# conf.d/vhost.conf

location /status {
    auth_basic           "Access to the staging site";
    auth_basic_user_file  /etc/apache2/.htpasswd;
}
```

### TCP Fast Open

```conf
# conf.d/vhost.conf

server {
    443 ssl fastopen=3;
}
```

### Django Admin Static

```conf
# conf.d/vhost.conf

location /dj-static/admin {
    access_log  off;
    alias /var/spool/nginx/tanxun-root/admin;
    expires max;
}
location /dj-static/rest_framework {
    access_log  off;
    alias /var/spool/nginx/tanxun-root/rest_framework;
    expires max;
}
```

## References

- [Nginx Documentation](https://nginx.org/en/docs/)
- [Forward Secrecy - Wikipedia](https://en.wikipedia.org/wiki/Forward_secrecy)
- [Nginx `valid_referers`](https://nginx.org/en/docs/http/ngx_http_referer_module.html#valid_referers)
