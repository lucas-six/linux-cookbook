# Setup Ubuntu

`20.04` LTS

## Start

```bash
hostnamectl set-hostname <hostname>

apt update
apt install apt apt-utils apt-transport-https
apt install coreutils sudo bash vim openssh-server colordiff tar gzip bzip2 wget curl git \
    systemd cron tzdata python3 ca-certificates procps psmisc htop \
    binutils make openssl rsync lsof make gcc
apt autoremove
systemctl restart sshd cron

ssh-keygen -t rsa -b 4096 -C "<hostname>" -f "$PWD/.ssh/id_rsa" -N ""
```

## Disk Partition (XFS)

```bash
fdisk -l
apt install parted
parted /dev/vdb
mklabel gpt
mkpart primary 1 100%
align-check optimal 1
print
quit
partprobe
fdisk -lu /dev/vdb
apt install xfsprogs
mkfs.xfs /dev/vdb1

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
apt install python3.9 python3.9-dev
```

### Install from source code

```bash
cd /tmp
wget https://www.python.org/ftp/python/3.10.9/Python-3.10.9.tgz
tar xzf Python-3.10.9.tgz
cd python-3.10.9
./configure --prefix=/usr --enable-optimizations
make -j$(cat /proc/cpuinfo | grep processor | uniq | wc -l)
make altinstall
```

### Configuration

```bash
# update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
# update-alternatives --config python

pip3 install --upgrade pip pipx pipenv argcomplete
activate-global-python-argcomplete
```

```conf
# /etc/pip.conf

[global]
#index-url = https://pypi.douban.com/simple
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host = mirrors.aliyun.com

[list]
format = columns
```
