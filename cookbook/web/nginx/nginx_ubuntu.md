# Nginx on Ubuntu

## Installation

See [Install on Ubuntu](https://nginx.org/en/linux_packages.html#Ubuntu).

```bash
# Install the prerequisites
apt install curl gnupg2 ca-certificates lsb-release openssl systemd

# stable nginx
echo "deb https://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

# mainline nginx
echo "deb https://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

# official nginx signing key
curl -fsSL https://nginx.org/keys/nginx_signing.key | sudo apt-key add -

# verify key
apt-key fingerprint ABF5BD827BD9BF62
# Output:
# pub   rsa2048 2011-08-19 [SC] [expires: 2024-06-14]
#       573B FD6B 3D8F BC64 1079  A6AB ABF5 BD82 7BD9 BF62
# uid   [ unknown] nginx signing key <signing-key@nginx.com>

apt update
apt install nginx
```

## Global Configuration

```bash
# openssl for nginx
openssl dhparam -out /etc/nginx/ssl_dh.params 4096
mkdir -p /etc/nginx/ssl
```

```conf
# /etc/sysctl.d/30-nginx.conf

net.ipv4.tcp_fastopen = 3
```

```bash
systemctl restart procps.service
```

```bash
ln -s nginx.conf /etc/nginx/.
systemctl enable|disable nginx
systemctl start|stop|restart|status nginx
```

## vHost Configuration

```nginx
server {
    listen  443 ssl http2 default_server;
    # listen  [::]:443 ssl default_server ipv6only=on;
    server_name  <domain.name>;

    access_log  /var/log/nginx/xxx.access.log main;
    error_log  /var/log/nginx/error.log error;

    ssl_certificate      /etc/nginx/ssl/xxx.pem;
    ssl_certificate_key  /etc/nginx/ssl/xxx.key;

    add_header  X-Content-Type-Options nosniff;
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

        # auth_basic "Restricted Access";
        # auth_basic_user_file /etc/nginx/htpasswd.users;
    }

    location ~ /\.ht {
        deny  all;
    }
    location ~/.env {
        return 444;
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

```nginx
location /status {
    auth_basic           "Access to the staging site";
    auth_basic_user_file  /etc/apache2/.htpasswd;
}
```

## References

- [Install on Ubuntu](https://nginx.org/en/linux_packages.html#Ubuntu)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Nginx Wiki - Pitfalls](http://wiki.nginx.org/Pitfalls)
- [Nginx Wiki - Quick Start](http://wiki.nginx.org/QuickStart)
- [Nginx Wiki - Configuration](http://wiki.nginx.org/Configuration)
