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
  Hands-on command/script examples, snippets and guides for daily work.</p>
  <p><a href="https://leven-cn.github.io/linux-cookbook/">https://leven-cn.github.io/linux-cookbook/</a></p>
</section>

<!-- markdownlint-disable line-length -->

## Recipes

## More Details

<!-- markdownlint-enable line-length -->

## STEP 0

**STEP 1**: Install [VirtualBox](http://www.virtualbox.org/) and **Guest Additions**.

**STEP 2**: Create virtual machine on VirtualBox VM.

**STEP 3**: Set VirtualBox Share (VirtualBox 4.0+)

**STEP 4**: Install Linux (Server) on VirtualBox VM.

**STEP 4**: Setup share directory on Linux (Server) guest.

```bash
sudo gpasswd -a <user> vboxsf
```

**STEP 5**: Re-Login Linux (Server).

The auto-mounted directory is mounted to `/media/sf_<share-dir>`.

For convenience, you could create a symbolic link in your home directory.

```bash
ln -s /media/sf_<share-dir> ~/.
```

**STEP 6**: Configure *NAT* + *Host-Only* network mode.

```bash
# On Linux (Server) guest
echo "" >> /etc/network/interfaces
echo "auto eth1" >> /etc/network/interfaces
echo "iface eth1 inet dhcp" >> /etc/network/interfaces
```

## User Guide

```bash
python3 admin.py setup|quick-setup
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
