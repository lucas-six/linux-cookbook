# NGINX vHost Configuration

## Basic

```conf
upstream xxx_servers {
    ip_hash;
    #server unix:///tmp/app.sock;
    server 127.0.0.1:1234 weight=1 max_fails=3;
}

server {
    listen 443 ssl reuseport default_server;
    http2 on;
    server_name <domain.name>;

    access_log  /var/log/nginx/xxx.access.log main;
    error_log  /var/log/nginx/error.log error;

    ssl_certificate      /etc/nginx/ssl/xxx.pem;
    ssl_certificate_key  /etc/nginx/ssl/xxx.key;

    add_header X-Content-Type-Options nosniff;
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
        access_log off;
        proxy_pass http://127.0.0.1:8000;
    }
    location ~* ^/(api2) {
        access_log off;
        uwsgi_pass xxx_servers;
        include uwsgi_params;
    }

    # Kibana
    location /_kibana {
        access_log off;
        proxy_pass http://kibana_servers/;
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

## IPv6

```conf
server {
    listen [::]:443 ssl default_server ipv6only=on;
}
```

## Basic Auth

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

## Django Admin Static

```conf
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
