# SSH Configuration

## Common

```conf
# ~/.ssh/config

# 启动压缩，默认no，选项-C
Compression no

# 连接超时重试次数，默认1
ConnectionAttempts 2

# 连接超时时间（秒），默认系统TCP超时时间
ConnectTimeout 3

# TCP长连接，默认开启
# 服务端：TCPKeepAlive yes
TCPKeepAlive yes

# 服务器心跳检测
# 服务端(/etc/ssh/sshd_config)：
#     ClientAliveCountMax 3
#     ClientAliveInterval 15
ServerAliveCountMax 3
ServerAliveInterval 15

# Specifies whether remote hosts are allowed to connect to local forwarded ports.
# Command line option: -g
# The default is "no".
GatewayPorts no

ExitOnForwardFailure yes
```

## Host

```plaintext
Host <alias-name>
    HostName <hostname-or-ip>
    Port 22
    User root
    IdentityFile ~/.ssh/<xxx>.pem
```

## PubKey

```bash
ssh-keygen -t rsa -b 4096 -C "<comment>"
```

## SSHD

```bash
mkdir ~/.ssh
chmod 0700 ~/.ssh
chmod 0400 ~/.ssh/authorized_keys
```
