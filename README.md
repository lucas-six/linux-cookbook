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
- [OpenSSH](https://leven-cn.github.io/linux-cookbook/cookbook/sys/ssh)
- [Virtualization (虚拟化)](https://leven-cn.github.io/linux-cookbook/cookbook/sys/virtualization)
- [Cloud Computing (云计算)](https://leven-cn.github.io/linux-cookbook/cookbook/sys/cloud_computing)

### Container (容器)

- [Docker: Basic Usage](https://leven-cn.github.io/linux-cookbook/cookbook/sys/docker_basic)

## Networking (网络)

- [Endianness](https://leven-cn.github.io/linux-cookbook/cookbook/net/endianness)
- [TCP/UDP Reuse Port: `SO_REUSEPORT`](https://leven-cn.github.io/linux-cookbook/cookbook/net/reuse_port)
- [TCP/UDP (Recv/Send) Buffer Size: `SO_RCVBUF`, `SO_SNDBUF`](https://leven-cn.github.io/linux-cookbook/cookbook/net/buffer_size)
- [Zero-Copy: `mmap()`, `sendfile()`, `TCP_CORK`](https://leven-cn.github.io/linux-cookbook/cookbook/net/zero_copy)

### TCP

- TCP Connect Timeout (*handshaking timeout*)
  - [Client Side](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_connect_timeout_client)
  - [Server Side](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_connect_timeout_server)
- [TCP Reuse Address: `SO_REUSEADDR`](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_reuse_address)
- [TCP `listen()` Queue](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_listen_queue)
- [TCP Keep Alive: `SO_KEEPALIVE`, `TCP_KEEPIDLE`, `TCP_KEEPCNT`, `TCP_KEEPINTVL`](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_keepalive)
- [TCP Nodelay (Nagle's Algorithm): `TCP_NODELAY`](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_nodelay)
- [TCP Quick ACK (Disable Delayed ACKs, 禁用延迟确认)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_quickack)
- [TCP Transmission Timeout: `SO_RCVTIMEO`, `SO_SNDTIMEO`](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_transmission_timeout)
- [TCP Slow Start (慢启动)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_slowstart)
- [Fix *TIME-WAIT Assassination Hazards* (TIME-WAIT 暗杀), enable **`tcp_rfc1337`**](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_rfc1337)
- [TCP Selective ACK (SACK)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_sack)

## Web

- [URL, URI, URN](https://leven-cn.github.io/linux-cookbook/cookbook/web/uri_url_urn)

### HTTP

- [HTTP Basic](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_basic)
- [HTTP Connection Management](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_connection)
- [HTTP Cookie](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_cookie)
- [HTTP Authentication: `WWW-Authenticate`, `Authorization`, `Proxy-Authenticate`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_authentication)
- [HTTP Caching: `Cache-Control`, ~~`Expires`~~, `ETag`, `Vary`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_caching)
- [HTTP Range Requests: `Range`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_range)
- HTTP Client
  - [`curl`](https://leven-cn.github.io/linux-cookbook/cookbook/web/curl)
  - [`httpie`](https://leven-cn.github.io/linux-cookbook/cookbook/web/httpie)
  - `Postman` (GUI)
  - Python API
    - `urllib` (built-in), [*`requests`*](https://requests.readthedocs.io/en/latest/) (sync io), [**`aiohttp`**](https://docs.aiohttp.org/en/stable/) (asyncio)
- [Cross-Site Request Forgery (CSRF) (跨站请求伪造)](https://leven-cn.github.io/linux-cookbook/cookbook/web/csrf)

### MongoDB

- [MongoDB: Overview](https://leven-cn.github.io/linux-cookbook/cookbook/web/mongodb/mongodb)
- [MongoDB (Standalone) in Docker](https://leven-cn.github.io/linux-cookbook/cookbook/web/mongodb/mongodb_standalone_docker)
- [MongoDB on Ubuntu](https://leven-cn.github.io/linux-cookbook/cookbook/web/mongodb/mongodb_ubuntu)
- CLI: **`mongosh`**
- GUI: **Mongo Compass**
- [Python API](https://www.mongodb.com/docs/drivers/python/)
  - Sync: [**`pymongo`**](https://www.mongodb.com/docs/drivers/pymongo/)
  - Async: [**`motor`**](https://www.mongodb.com/docs/drivers/motor/)

### Nginx

- [Nginx Installation](https://leven-cn.github.io/linux-cookbook/cookbook/web/nginx/nginx_installation)
- [Nginx Configuration](https://leven-cn.github.io/linux-cookbook/cookbook/web/nginx/nginx_configuration)

### Redis

- [Redis - Setup](https://leven-cn.github.io/linux-cookbook/cookbook/web/redis/redis_setup)
- [CLI: **`redis-cli`** - Basic Usage](https://leven-cn.github.io/linux-cookbook/cookbook/web/redis/redis_usage_basic)
- GUI: [**RedisInsight**](https://redis.com/redis-enterprise/redis-insight/) (Official), ~~Redis Desktop Manager~~, *Another Redis Desktop Manager*
- Python API:
  - Sync: [**`redis-py`**](https://redis.readthedocs.io/en/latest/)
  - Async: [**`aioredis`**](https://aioredis.readthedocs.io/en/latest/)
  - ORM: *`pyton-redis-orm`*

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

# doc
python admin.py doc <project-path>
```
