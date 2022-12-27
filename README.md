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

## Web

- [URL, URI, URN](https://leven-cn.github.io/linux-cookbook/cookbook/web/uri_url_urn)

### HTTP

- [HTTP Basic](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_basic)
- [HTTP Authentication](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_authentication)
- [HTTP Caching](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_caching)
- [HTTP Range Requests: `Range`](https://leven-cn.github.io/linux-cookbook/cookbook/web/http_range)
- HTTP Client
  - [`curl`](https://leven-cn.github.io/linux-cookbook/cookbook/web/curl)
  - [`httpie`](https://leven-cn.github.io/linux-cookbook/cookbook/web/httpie)
  - `Postman`

## Recipes

- [Setup Ubuntu](https://leven-cn.github.io/linux-cookbook/recipes/ubuntu_setup)
- [Docker Basic Usage](https://leven-cn.github.io/linux-cookbook/recipes/docker_basic)
- [Docker: PostgreSQL](https://leven-cn.github.io/linux-cookbook/recipes/docker_postgresql)

## More Details

- [Virtualization (虚拟化)](https://leven-cn.github.io/linux-cookbook/more/virtualization)

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
