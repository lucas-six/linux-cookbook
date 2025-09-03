# Setup Ubuntu

`24.04` LTS

```bash
lsb_release -a
```

## Start

```bash
hostnamectl set-hostname <hostname>

apt update
apt list --upgradable

apt install colordiff wget2
apt autoremove

ssh-keygen
#ssh-keygen -t rsa -b 4096 -C "<hostname>" -f "$PWD/.ssh/id_rsa" -N ""
```

## Disk Partition (XFS)

```bash
fdisk -l
apt install parted

parted /dev/vdb
> mklabel gpt
> mkpart primary 1 100%
> align-check optimal 1
> print
> quit

partprobe
fdisk -lu /dev/vdb
apt install xfsprogs
mkfs.xfs /dev/vdb1

blkid

`/etc/fstab`

mkdir /mnt/<point>
mount -a
```

## Python

### Install by `apt`

```bash
apt install build-essential cpp zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
    libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev uuid-dev
apt install python3
pip install -U pip
apt install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt update
apt autoremove
apt install python3.12 python3.12-dev
```

### Install from source code

```bash
cd /tmp
wget https://www.python.org/ftp/python/3.12.10/Python-3.12.10.tgz
tar xzf Python-3.12.10.tgz
cd python-3.12.10
./configure --prefix=/usr --enable-optimizations
# make -j$(cat /proc/cpuinfo | grep processor | uniq | wc -l)
make -j$(nproc)
make altinstall
```

### Configuration

```bash
# update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1
# update-alternatives --config python

pip3 install --upgrade pip argcomplete
activate-global-python-argcomplete
```

## `sysctl`

```conf
# /etc/sysctl.conf

vm.swappiness = 0
kernel.sysrq = 1

net.core.somaxconn = 4096
net.core.netdev_max_backlog = 4096
#net.ipv4.neigh.default.gc_stale_time = 60

# see details in https://help.aliyun.com/knowledge_detail/39428.html
net.ipv4.conf.all.rp_filter = 0
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.default.arp_announce = 2
net.ipv4.conf.lo.arp_announce = 2
net.ipv4.conf.all.arp_announce = 2

# see details in https://help.aliyun.com/knowledge_detail/41334.html
net.ipv4.tcp_max_syn_backlog = 4096
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_synack_retries = 2
#net.ipv4.tcp_retries1 = 3
#net.ipv4.tcp_retries2 = 5
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_max_tw_buckets = 32768
net.ipv4.tcp_syncookies = 1
; net.ipv4.tcp_fin_timeout = 3  # 60
; net.ipv4.tcp_tw_reuse = 1  # 0
; net.ipv4.tcp_tw_recycle = 1  # 0
; net.ipv4.tcp_keepalive_time = 60  # 7200

# net.ipv6.conf.all.disable_ipv6 = 1
# net.ipv6.conf.default.disable_ipv6 = 1
# net.ipv6.conf.lo.disable_ipv6 = 1
```

```bash
sysctl -p
```

## References

- [GNU Wget2 - GitLab](https://gitlab.com/gnuwget/wget2)
