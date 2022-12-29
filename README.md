# Linux Cookbook

<section align="center">
  <img src="https://leven-cn.github.io/linux-cookbook/imgs/linux-logo.svg"
    alt="Linux Logo" width="250" height="250" style="text-align:center;" title="Linux Logo">
  <br><br>
  <p>
    <a href="https://github.com/leven-cn/linux-cookbook/actions/workflows/lint.yml">
      <img src="https://github.com/leven-cn/linux-cookbook/actions/workflows/lint.yml/badge.svg"
      alt="GitHub Actions - lint" style="max-width:100%;">
    </a>
    <a href="https://github.com/pre-commit/pre-commit">
      <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"
      alt="pre-commit" style="max-width:100%;">
    </a>
  </p>
  <p>Recipes for <code>Linux</code>.
  Hands-on system administration examples and guides for daily work.</p>
  <p><a href="https://leven-cn.github.io/linux-cookbook/">https://leven-cn.github.io/linux-cookbook/</a></p>
</section>

<!-- markdownlint-disable line-length -->

## Date & Time

### Representation of Dates and Times

- [ISO 8601 Format](https://leven-cn.github.io/linux-cookbook/cookbook/time/fmt_iso_8601)
- [RFC 3339 Format](https://leven-cn.github.io/linux-cookbook/cookbook/time/fmt_rfc_3339)

## System Administration (系统管理)

- [Setup Ubuntu](https://leven-cn.github.io/linux-cookbook/cookbook/sys/ubuntu_setup)
- [Virtualization (虚拟化)](https://leven-cn.github.io/linux-cookbook/cookbook/sys/virtualization)
- [Cloud Computing (云计算)](https://leven-cn.github.io/linux-cookbook/cookbook/sys/cloud_computing)

### Container (容器)

- [Docker: Basic Usage](https://leven-cn.github.io/linux-cookbook/cookbook/sys/docker_basic)
- [Docker: MongoDB](https://leven-cn.github.io/linux-cookbook/cookbook/sys/docker_mongodb)

## Networking (网络)

- [Endianness](https://leven-cn.github.io/linux-cookbook/cookbook/net/endianness)

### TCP

- TCP Connect Timeout (*handshaking timeout*)
  - [Client Side](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_connect_timeout_client)
  - [Server Side](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_connect_timeout_server)
- [TCP Nodelay (Nagle's Algorithm)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_nodelay)
- [TCP Quick ACK (Disable Delayed ACKs, 禁用延迟确认)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_quickack)
- [TCP Keep Alive](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_keepalive)
- [TCP Slow Start (慢启动)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_slowstart)
- [Fix *TIME-WAIT Assassination Hazards* (TIME-WAIT 暗杀), enable **`tcp_rfc1337`**](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_rfc1337)
- [TCP Selective ACK (SACK)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_sack)

## Web

- [URL, URI, URN](https://leven-cn.github.io/linux-cookbook/cookbook/web/uri_url_urn)

### HTTP

- [HTTP Basic](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_basic)
- [HTTP Connection Management](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_connection)
- [HTTP Cookie](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_cookie)
- [HTTP Authentication](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_authentication)
- [HTTP Caching](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_caching)
- [HTTP Range Requests: `Range`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_range)
- HTTP Client
  - [`curl`](https://leven-cn.github.io/linux-cookbook/cookbook/web/curl)
  - [`httpie`](https://leven-cn.github.io/linux-cookbook/cookbook/web/httpie)
  - `Postman`
- [Cross-Site Request Forgery (CSRF) (跨站请求伪造)](https://leven-cn.github.io/linux-cookbook/cookbook/web/csrf)

## Recipes

- [Docker: PostgreSQL](https://leven-cn.github.io/linux-cookbook/recipes/docker_postgresql)

<!-- markdownlint-enable line-length -->

## User Guide

```bash
python3 admin.py setup
```

**STEP 3**: Build projects

```bash
# uWSGI
python3 admin.py run-uwsgi <app-path> <address>
python3 admin.py stop-uwsgi <app-path>
python3 admin.py init-run-uwsgi <app-path> <address>
tail -f /var/log/uwsgi/<app-name>.log

# nginx
python3 admin.py enable-nginx <app-path> [<upstream-address>]
python3 admin.py disable-nginx [<app-path> <upstream-address>]
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

# doc
python admin.py doc <project-path>
```
