# Linux Cookbook

<section align="center">
  <img src="https://lucas-stack.github.io/linux-cookbook/imgs/linux-logo.svg"
    alt="Linux Logo" width="250" height="250" style="text-align:center;" title="Linux Logo">
  <br><br>
  <p>
    <a href="https://github.com/lucas-stack/linux-cookbook/actions/workflows/lint.yml">
      <img src="https://github.com/lucas-stack/linux-cookbook/actions/workflows/lint.yml/badge.svg"
      alt="GitHub Actions - lint" style="max-width:100%;">
    </a>
    <a href="https://github.com/pre-commit/pre-commit">
      <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"
      alt="pre-commit" style="max-width:100%;">
    </a>
  </p>
  <p>Recipes for <code>Linux</code>.
  Hands-on system administration and development examples and guides for daily work.</p>
  <p><a href="https://lucas-stack.github.io/linux-cookbook/">https://lucas-stack.github.io/linux-cookbook/</a></p>
</section>

**Linux** (`/ˈlinʊks/` LEEN-uuks or `/ˈlɪnʊks/` LIN-uuks)
is a family of open-source *Unix-like operating systems* based on the Linux kernel,
an operating system kernel first released on *September 17, 1991*, by *Linus Torvalds*.

<!-- markdownlint-disable line-length -->

## Quick Start

- [Linux Distributions](https://lucas-stack.github.io/linux-cookbook/cookbook/start/linux_distributions)
- Setup: [Ubuntu](https://lucas-stack.github.io/linux-cookbook/cookbook/start/setup_ubuntu)
- [Basic Usage (GNU `coreutils`)](https://lucas-stack.github.io/linux-cookbook/cookbook/start/basic)
- I/O: File & Directory
  - [File & Directory: Access & Permission & Digest (GNU `coreutils`)](https://lucas-stack.github.io/linux-cookbook/cookbook/start/file_dir)
  - [Join Files: `join` (GNU `coreutils`)](https://lucas-stack.github.io/linux-cookbook/cookbook/start/join-files)
  - [Search Files: `find`](https://lucas-stack.github.io/linux-cookbook/cookbook/start/find)
  - [Search File Contents: `grep`](https://lucas-stack.github.io/linux-cookbook/cookbook/start/grep)
  - [Linux Filesystem Hierarchy Standard (FHS)](https://lucas-stack.github.io/linux-cookbook/cookbook/start/linux_fhs)
- [Date & Time: `date` (GNU `coreutils`)](https://lucas-stack.github.io/linux-cookbook/cookbook/start/coreutils_date)
- [Time Zone](https://lucas-stack.github.io/linux-cookbook/cookbook/start/tz)
- [Process Control](https://lucas-stack.github.io/linux-cookbook/cookbook/start/proc)
- [System Information (GNU `coreutils`)](https://lucas-stack.github.io/linux-cookbook/cookbook/start/coreutils_sysinfo)
- [Environment Variables](https://lucas-stack.github.io/linux-cookbook/cookbook/start/env)
- Diff: `diff`, `colordiff`
- [Archive & Compression: `tar`](https://lucas-stack.github.io/linux-cookbook/cookbook/start/archive)
- Network: `wget`, [GNU `wget2`](https://gitlab.com/gnuwget/wget2), [`curl`](https://lucas-stack.github.io/linux-cookbook/cookbook/start/curl)
- Scripts
  - [Bash Cookbook](https://lucas-stack.github.io/bash-cookbook/)
  - [Python Cookbook](https://lucas-stack.github.io/python-cookbook/)
- [OpenSSH](https://lucas-stack.github.io/linux-cookbook/cookbook/start/ssh)

## General Concepts

- [Data Type](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/data_type)
- [Character (字符)](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/char)
- [Character Encoding (字符编码)](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/char_encoding)
  - [ASCII](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/ascii)
  - [Unicode](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/unicode)
  - [UTF-8](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/utf_8)
  - [Mojibake](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/Mojibake)
- [String (字符串)](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/str)
- [End of Line (EOL): **CRLF**](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/eol_crlf)
- [Input/Output (I/O)](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/io)
- Time
  - [Computer Time](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/time)
  - [ISO 8601 Format](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/datetime_fmt_iso_8601)
  - [RFC 3339 Format](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/datetime_fmt_rfc_3339)
- [Compression Algorithms (压缩算法)](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/compression_algorithms)
- [Process](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/proc)
- [URL, URI, URN](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/uri_url_urn)
- [Endianness](https://lucas-stack.github.io/linux-cookbook/cookbook/general_concepts/endianness)

## System Programming (系统编程)

- [Standard I/O (standard C library): File](https://lucas-stack.github.io/linux-cookbook/cookbook/programming/stdio_file)
- [Standard I/O (standard C library): Directory](https://lucas-stack.github.io/linux-cookbook/cookbook/programming/stdio_dir)
- [UNIX I/O (system call)](https://lucas-stack.github.io/linux-cookbook/cookbook/programming/syscall_io)
- [File Metadata](https://lucas-stack.github.io/linux-cookbook/cookbook/programming/file_metadata)

## System Administration (系统管理)

- [Virtualization (虚拟化)](https://lucas-stack.github.io/linux-cookbook/cookbook/sys/virtualization)
- [Cloud Computing (云计算)](https://lucas-stack.github.io/linux-cookbook/cookbook/sys/cloud_computing)

### Network

- [TCP/UDP Reuse Port: `SO_REUSEPORT`](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/reuse_port)
- [TCP/UDP (Recv/Send) Buffer Size: `SO_RCVBUF`, `SO_SNDBUF`](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/buffer_size)
- [Zero-Copy: `mmap()`, `sendfile()`, `TCP_CORK`](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/zero_copy)

#### TCP

- TCP Connect Timeout (*handshaking timeout*)
  - [Client Side](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_connect_timeout_client)
  - [Server Side](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_connect_timeout_server)
- [TCP `listen()` Queue](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_listen_queue)
- [TCP Reuse Address: `SO_REUSEADDR`](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_reuse_address)
- [TCP Keep Alive: `SO_KEEPALIVE`, `TCP_KEEPIDLE`, `TCP_KEEPCNT`, `TCP_KEEPINTVL`](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_keepalive)
- [TCP Nodelay (Nagle's Algorithm): `TCP_NODELAY`](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_nodelay)
- [TCP Transmission Timeout: `SO_RCVTIMEO`, `SO_SNDTIMEO`](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_transmission_timeout)
- [TCP Quick ACK (Disable Delayed ACKs, 禁用延迟确认)](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_quickack)
- [Fix *TIME-WAIT Assassination Hazards* (TIME-WAIT 暗杀), enable **`tcp_rfc1337`**](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_rfc1337)
- [TCP Slow Start (慢启动)](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_slowstart)
- [TCP Fast Open (TFO)](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_fastopen)
- [TCP Selective ACK (SACK)](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/net/tcp_sack)

### MongoDB

- [MongoDB: Overview](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_overview)
- Server
  - [MongoDB on Ubuntu](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_ubuntu)
  - [MongoDB TLS](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_tls)
- Client
  - [CLI: `mongosh` Usage](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/mongodb/mongodb_usage)
  - GUI: **Mongo Compass**

### Redis

- [Redis Setup](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/redis/redis_setup)
- [CLI: `redis-cli` - Basic Usage](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/redis/redis_usage_basic)
- GUI
  - [**RedisInsight**](https://redis.com/redis-enterprise/redis-insight/) (Official)
  - ~~Redis Desktop Manager~~
  - *Another Redis Desktop Manager*

### PostgreSQL

- [PostgreSQL - Setup](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/postgresql/postgresql_setup)
- [CLI: `psql` - Usage](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/postgresql/postgresql_usage)
- GUI (Official): `pgadmin4`

### RabbitMQ

- [RabbitMQ Setup on Ubuntu / Debian](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/rabbitmq/rabbitmq_setup_ubuntu)

### EMQX

- [EMQX](https://www.emqx.io/zh)

### Performance

- [Amdahl's Law](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/amdahl_law)

### Container (容器)

- [Docker: Basic Usage](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/docker/docker_basic)
- [MongoDB (Standalone) in Docker](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/docker/mongodb_standalone)
- [PostgreSQL in Docker](https://lucas-stack.github.io/linux-cookbook/cookbook/admin/docker/postgresql)

## DevOps

- [Git Cookbook](https://lucas-stack.github.io/git-cookbook/)
- Python: [`pipenv`](https://lucas-stack.github.io/python-cookbook/cookbook/build/pkg/pipenv)
  - [Project](https://lucas-stack.github.io/python-cookbook/cookbook/build/project): `black`, `isort`, `mypy`, `pylint`
  - [Deploy with Docker](https://lucas-stack.github.io/python-cookbook/cookbook/build/deploy/docker)

## Web

- [Cross-Site Request Forgery (CSRF) (跨站请求伪造)](https://lucas-stack.github.io/linux-cookbook/cookbook/web/csrf)

### HTTP

- [HTTP Basic](https://lucas-stack.github.io/linux-cookbook/cookbook/web/http/http_basic)
- [HTTP Connection Management](https://lucas-stack.github.io/linux-cookbook/cookbook/web/http/http_connection)
- [HTTP Cookie](https://lucas-stack.github.io/linux-cookbook/cookbook/web/http/http_cookie)
- [HTTP Authentication: `WWW-Authenticate`, `Authorization`, `Proxy-Authenticate`](https://lucas-stack.github.io/linux-cookbook/cookbook/web/http/http_authentication)
- [HTTP Caching: `Cache-Control`, ~~`Expires`~~, `ETag`, `Vary`](https://lucas-stack.github.io/linux-cookbook/cookbook/web/http/http_caching)
- [HTTP Range Requests: `Range`](https://lucas-stack.github.io/linux-cookbook/cookbook/web/http/http_range)

#### HTTP Client

- [`curl`](https://lucas-stack.github.io/linux-cookbook/cookbook/start/curl)
- [`httpie`](https://lucas-stack.github.io/linux-cookbook/cookbook/web/httpie)
- `Postman` (GUI)

### Nginx

- [Nginx Installation](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/nginx_installation)
- [Nginx Configuration: Global](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/nginx_conf_global)
- [Nginx Configuration: vHost](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/nginx_conf_vhost)
- [Nginx Configuration: TCP Fast Open](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/fastopen)
- [Nginx Configuration: WebSocket](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/websocket)
- [Nginx Configuration: CSRF (跨站请求伪造)](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/csrf)
- [Nginx Configuration: XSS (跨站脚本攻击)](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/xss)
- [Nginx Configuration: `zstd`](https://lucas-stack.github.io/linux-cookbook/cookbook/web/nginx/zstd)

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
  - [C FAQs](https://c-faq.com)
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
  - [Redis Home](https://redis.io)
  - [Docker Home](https://www.docker.com)
  - [DockerHub Home](https://hub.docker.com)
  - [Nginx Documentation](https://nginx.org/en/docs/)
  - [PostgreSQL Home](https://www.postgresql.org/)
  - [RabbitMQ Home](https://www.rabbitmq.com/)
  - [MQTT Home](https://mqtt.org/)
    - [EMQ](https://emqtt.io) | [EMQX](https://www.emqx.io/zh)
    - [MQTT Guide](https://www.emqx.com/zh/mqtt-guide)

<!-- markdownlint-enable line-length -->
