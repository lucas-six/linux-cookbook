admin-linux
==================

Admin Linux

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

## User Guide

**STEP 1**: Install Git

```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git
```

**STEP 2**: Setup

```bash
git config --global user.name "Li Yun"              # replace with your name
git config --global user.email leven.cn@gmail.com   # replace with your email address

cd                                                  # choose your own path
git clone https://github.com/leven-cn/admin-linux.git

cd admin-linux
python admin.py setup
```

**STEP 3**: Build projects

```bash
python admin.py build
```
