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
  Hands-on system administration and development examples and guides for daily work.</p>
  <p><a href="https://leven-cn.github.io/linux-cookbook/">https://leven-cn.github.io/linux-cookbook/</a></p>
</section>

**Linux** (`/ˈlinʊks/` LEEN-uuks or `/ˈlɪnʊks/` LIN-uuks)
is a family of open-source *Unix-like operating systems* based on the Linux kernel,
an operating system kernel first released on *September 17, 1991*, by *Linus Torvalds*.

<!-- markdownlint-disable line-length -->

## Quick Start

- [Linux Distributions](https://leven-cn.github.io/linux-cookbook/cookbook/start/linux_distributions)
- Setup: [Ubuntu](https://leven-cn.github.io/linux-cookbook/cookbook/start/setup_ubuntu)
- [Basic Usage (GNU `coreutils`)](https://leven-cn.github.io/linux-cookbook/cookbook/start/basic)
- I/O: File & Directory
  - [File & Directory: Access & Permission & Digest (GNU `coreutils`)](https://leven-cn.github.io/linux-cookbook/cookbook/start/file_dir)
  - [Join Files: `join` (GNU `coreutils`)](https://leven-cn.github.io/linux-cookbook/cookbook/start/join-files)
  - [Search Files: `find`](https://leven-cn.github.io/linux-cookbook/cookbook/start/find)
  - [Search File Contents: `grep`](https://leven-cn.github.io/linux-cookbook/cookbook/start/grep)
  - [Linux Filesystem Hierarchy Standard (FHS)](https://leven-cn.github.io/linux-cookbook/cookbook/start/linux_fhs)
- [Date & Time: `date` (GNU `coreutils`)](https://leven-cn.github.io/linux-cookbook/cookbook/start/coreutils_date)
- [Time Zone](https://leven-cn.github.io/linux-cookbook/cookbook/start/tz)
- [Process Control](https://leven-cn.github.io/linux-cookbook/cookbook/start/proc)
- [System Information (GNU `coreutils`)](https://leven-cn.github.io/linux-cookbook/cookbook/start/coreutils_sysinfo)
- [Environment Variables](https://leven-cn.github.io/linux-cookbook/cookbook/start/env)
- Diff: `diff`, `colordiff`
- [Archive & Compression: `tar`](https://leven-cn.github.io/linux-cookbook/cookbook/start/archive)
- Network: `wget`, [GNU `wget2`](https://gitlab.com/gnuwget/wget2), [`curl`](https://leven-cn.github.io/linux-cookbook/cookbook/start/curl)
- Scripts
  - [Bash Cookbook](https://leven-cn.github.io/bash-cookbook/)
  - [Python Cookbook](https://leven-cn.github.io/python-cookbook/)
- [OpenSSH](https://leven-cn.github.io/linux-cookbook/cookbook/start/ssh)

## General Concepts

- [Data Type](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/data_type)
- [Character (字符)](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/char)
- [Character Encoding (字符编码)](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/char_encoding)
  - [ASCII](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/ascii)
  - [Unicode](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/unicode)
  - [UTF-8](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/utf_8)
  - [Mojibake](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/Mojibake)
- [String (字符串)](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/str)
- [End of Line (EOL): **CRLF**](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/eol_crlf)
- [Input/Output (I/O)](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/io)
- Time
  - [Computer Time](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/time)
  - [ISO 8601 Format](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/datetime_fmt_iso_8601)
  - [RFC 3339 Format](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/datetime_fmt_rfc_3339)
- [Compression Algorithms (压缩算法)](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/compression_algorithms)
- [Process](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/proc)
- [URL, URI, URN](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/uri_url_urn)
- [Endianness](https://leven-cn.github.io/linux-cookbook/cookbook/general_concepts/endianness)

## System Programming (系统编程)

- [Standard I/O (standard C library): File](https://leven-cn.github.io/linux-cookbook/cookbook/programming/stdio_file)
- [Standard I/O (standard C library): Directory](https://leven-cn.github.io/linux-cookbook/cookbook/programming/stdio_dir)
- [UNIX I/O (system call)](https://leven-cn.github.io/linux-cookbook/cookbook/programming/syscall_io)
- [File Metadata](https://leven-cn.github.io/linux-cookbook/cookbook/programming/file_metadata)

## System Administration (系统管理)

- [Virtualization (虚拟化)](https://leven-cn.github.io/linux-cookbook/cookbook/sys/virtualization)
- [Cloud Computing (云计算)](https://leven-cn.github.io/linux-cookbook/cookbook/sys/cloud_computing)

### Network

- [TCP/UDP Reuse Port: `SO_REUSEPORT`](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/reuse_port)
- [TCP/UDP (Recv/Send) Buffer Size: `SO_RCVBUF`, `SO_SNDBUF`](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/buffer_size)

#### TCP

- TCP Connect Timeout (*handshaking timeout*)
  - [Client Side](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_connect_timeout_client)
  - [Server Side](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_connect_timeout_server)
- [TCP `listen()` Queue](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_listen_queue)
- [TCP Reuse Address: `SO_REUSEADDR`](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_reuse_address)
- [TCP Keep Alive: `SO_KEEPALIVE`, `TCP_KEEPIDLE`, `TCP_KEEPCNT`, `TCP_KEEPINTVL`](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_keepalive)
- [TCP Nodelay (Nagle's Algorithm): `TCP_NODELAY`](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_nodelay)
- [TCP Transmission Timeout: `SO_RCVTIMEO`, `SO_SNDTIMEO`](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_transmission_timeout)
- [TCP Quick ACK (Disable Delayed ACKs, 禁用延迟确认)](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_quickack)
- [Fix *TIME-WAIT Assassination Hazards* (TIME-WAIT 暗杀), enable **`tcp_rfc1337`**](https://leven-cn.github.io/linux-cookbook/cookbook/admin/net/tcp_rfc1337)

### MongoDB

- [MongoDB: Overview](https://leven-cn.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_overview)
- Server
  - [MongoDB on Ubuntu](https://leven-cn.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_ubuntu)
  - [MongoDB TLS](https://leven-cn.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_tls)
- Client
  - CLI: **`mongosh`**: [MongoDB Usage](https://leven-cn.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_usage)
  - GUI: **Mongo Compass**
  - [Python API](https://www.mongodb.com/docs/drivers/python/)
    - Sync: [**`pymongo`**](https://www.mongodb.com/docs/drivers/pymongo/)
    - Async: [**`motor`**](https://www.mongodb.com/docs/drivers/motor/)

### Performance

- [Amdahl's Law](https://leven-cn.github.io/linux-cookbook/cookbook/admin/amdahl_law)

### Container (容器)

- [Docker: Basic Usage](https://leven-cn.github.io/linux-cookbook/cookbook/sys/docker_basic)

## DevOps

- [Git Cookbook](https://leven-cn.github.io/git-cookbook/)
- Python: [`pipenv`](https://leven-cn.github.io/python-cookbook/cookbook/build/pkg/pipenv)
  - [Project](https://leven-cn.github.io/python-cookbook/cookbook/build/project): `black`, `isort`, `mypy`, `pylint`
  - [Deploy with Docker](https://leven-cn.github.io/python-cookbook/cookbook/build/deploy/docker)

## Web

### HTTP

- [HTTP Basic](https://leven-cn.github.io/linux-cookbook/cookbook/web/http/http_basic)
- [HTTP Connection Management](https://leven-cn.github.io/linux-cookbook/cookbook/web/http/http_connection)
- [HTTP Cookie](https://leven-cn.github.io/linux-cookbook/cookbook/web/http/http_cookie)
- [HTTP Authentication: `WWW-Authenticate`, `Authorization`, `Proxy-Authenticate`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http/http_authentication)
- [HTTP Caching: `Cache-Control`, ~~`Expires`~~, `ETag`, `Vary`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http/http_caching)
- [HTTP Range Requests: `Range`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http/http_range)

#### HTTP Client

- [`curl`](https://leven-cn.github.io/linux-cookbook/cookbook/start/curl)
- [`httpie`](https://leven-cn.github.io/linux-cookbook/cookbook/web/httpie)
- `Postman` (GUI)

## Networking (网络)

- [Zero-Copy: `mmap()`, `sendfile()`, `TCP_CORK`](https://leven-cn.github.io/linux-cookbook/cookbook/net/zero_copy)

### TCP

- [TCP Slow Start (慢启动)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_slowstart)
- [TCP Selective ACK (SACK)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_sack)
- [TCP Fast Open (TFO)](https://leven-cn.github.io/linux-cookbook/cookbook/net/tcp_fastopen)

## Web2

### HTTP

- [Cross-Site Request Forgery (CSRF) (跨站请求伪造)](https://leven-cn.github.io/linux-cookbook/cookbook/web/csrf)

### MongoDB

- [MongoDB (Standalone) in Docker](https://leven-cn.github.io/linux-cookbook/cookbook/web/mongodb/mongodb_standalone_docker)

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

## Recommended Readings

<!-- markdownlint-disable line-length -->

- [LinuxCommmand.org](https://linuxcommand.org/)
- [The Linux Command Line, Fifth Internet Edition](https://linuxcommand.org/tlcl.php)
- [Filesystem Hierarchy Standard Specification Series](https://refspecs.linuxfoundation.org/fhs.shtml)
- [Manpages - Debian](https://manpages.debian.org/bookworm/manpages/index.html)
- [The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/index.html)
- Book: *UNIX and Linux System Administration Handbook, Fifth Edition* (2018)
- C Programming Language
  - Book: *The C Programming Language, Second Edition* (1989)
  - Book: *C: A Reference Manual, Fifth Edition* (2002)
  - Book: *The C Standard Library* (1992)
- Computer System, OS and System Development
  - Book: *Computer Systems: A Programmer's Perspective, Third Edition* (2016)
  - [Paper: *The UNIX Time-Sharing System*. (*Communications of The ACM*, 1974)](https://www.scs.stanford.edu/nyu/04fa/sched/readings/unix.pdf)
  - Book: [*Operating Systems: Three Easy Pieces* v1.00](https://pages.cs.wisc.edu/~remzi/OSTEP/)
  - Book: *Advanced Programming in the UNIX Environment, 3rd Edition.* (2013)
- URL
  - [URL Living Standard](https://url.spec.whatwg.org)
  - [RFC 3986 - Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986)
  - [`curl` Home](https://curl.se)
  - [cURL Cookbook](https://catonmat.net/cookbooks/curl)
- Book: *HTTP: The Definitive Guide* (2002)
- System Services
  - [MongoDB Documentation](https://www.mongodb.com/docs/)

<!-- markdownlint-enble line-length -->

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
