# SSH

**SSH** = **Secure Shell**

## Client

### PubKey

```bash
# ED25519: 椭圆曲线算法 (by default)
ssh-keygen -t ed25519 -C "<comment>" -N ""

# RSA-4096
ssh-keygen -t rsa -b 4096 -C "<comment>" -N ""
```

### Client Configuration

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

######
## Host
######

Host <alias-name>
    HostName <hostname-or-ip>
    Port 22
    User <username>
    IdentityFile ~/.ssh/<private-key>


######
## 远程服务本地转发
##
## Local Port Forwarding, 本地端口转发
## 选项 -L (-NfCq)
##
## Usage:
##     ssh [-N] <host-alias>
##
## Server (/etc/ssh/sshd_config):
##     GatewayPorts yes
######

Host <alias-name>
    HostName <hostname-or-ip>
    Port 22
    User <username>
    IdentityFile ~/.ssh/<private-key>
    LocalForward localhost:<local-port> <server-host>:<server-port>


######
## 内网穿透 (本地服务远程转发)
##
## 远程端口转发: ssh [-f] -Ng -R <remote-port>:localhost:<local-port> <user>@<remote-host>
## Usage: ssh [-Ng] web
######

Host <alias-name>
    HostName <hostname-or-ip>
    Port 22
    User <username>
    IdentityFile ~/.ssh/<private-key>
    GatewayPorts yes
    RemoteForward <remote-port> <server-host>:<server-port>


######
## 跳板机 (Agent Forwarding, 代理转发)
##
## Server (/etc/ssh/sshd_config):
##     AllowAgentForwarding yes
######

Host <alias-name-pattern>
    Port 22
    User <username>
    IdentityFile ~/.ssh/<private-key>
    ProxyCommand ssh <host-alias-name> -W %h:%p
```

### Jumper

```bash
eval $(ssh-agent)
ssh-add <key>
ssh -A <jumper>

ssh <target>
```

## Server

```bash
mkdir ~/.ssh
chmod 0700 ~/.ssh
chmod 0400 ~/.ssh/authorized_keys
```

### Server Configuration

```conf
# /etc/ssh/sshd_config

ClientAliveCountMax 3
ClientAliveInterval 15

# Local Port Forwarding
#GatewayPorts yes

# Agent Forwarding
AllowAgentForwaring yes
```

## References

- [**OpenSSH** Home](https://www.openssh.com/)
