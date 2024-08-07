# MongoDB on Ubuntu

## Installation

**NOTE**: **`XFS`** filesystem is strongly recommended with the `WiredTiger` storage engine.

```bash
apt install apt apt-utils apt-transport-https \
        python-apt-common python3-apt
apt install wget gnupg systemd

# for v4.4
# wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
# echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# for 5.0
# wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
# echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

# for 6.0
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# for 7.0
wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

apt update
apt install mongodb-org
```

## Configuration

```conf
# /etc/sysctl.d/30-mongodb.conf

vm.swappiness = 1
vm.overcommit_memory = 1
vm.zone_reclaim_mode = 0
vm.max_map_count = 262144
net.core.somaxconn = 40960
net.core.netdev_max_backlog = 40960
net.ipv4.tcp_max_syn_backlog = 40960
```

```bash
sysctl -p
systemctl restart procps.service
```

```conf
# /etc/security/limits.d/mongodb.conf

mongodb  soft  nofile  65535
mongodb  hard  nofile  65535
```

```yml
# /etc/mongod.conf

storage:
  dbPath: </var/lib/mongodb>
  journal:
    enabled: true
  wiredTiger:
    collectionConfig:
      blockCompressor: zstd
  #   engineConfig:
  #     cacheSizeGB: 2

systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log
  timeStampFormat: iso8601-utc

net:
  port: 27017
  bindIp: 127.0.0.1  # 0.0.0.0 for all, :: for IPv6
#  maxIncomingConnections: 65536

processManagement:
  timeZoneInfo: /usr/share/zoneinfo
```

```ini
# /etc/systemd/system/disable-transparent-huge-pages.service

[Unit]
Description=Disable Transparent Huge Pages (THP)
DefaultDependencies=no
After=sysinit.target local-fs.target
Before=mongod.service
[Service]
Type=oneshot
ExecStart=/bin/sh -c 'echo never | tee /sys/kernel/mm/transparent_hugepage/enabled > /dev/null'
[Install]
WantedBy=basic.target
```

```bash
apt install numactl
```

```ini
# /lib/systemd/system/mongod.service

ExecStart=/usr/bin/numactl --interleave=all /usr/bin/mongod --config /etc/mongod.conf
```

```bash
chown -R mongodb:mongodb </var/lib/mongodb>

systemctl daemon-reload

systemctl start disable-transparent-huge-pages
cat /sys/kernel/mm/transparent_hugepage/enabled  # never
systemctl enable disable-transparent-huge-pages

systemctl enable|disable mongod
systemctl start|stop|restart|status mongod
```

### Standaone Authentication

```yaml
# /etc/mongod.conf

security:
  authorization: enabled  # 启动认证
```

### Replica Set

```yaml
# /etc/mongod.conf

net:
  # bindIp: 0.0.0.0  # 单节点副本集
  bindIp: localhost,10.0.0.1,10.0.0.2

replication:
  replSetName: <replica-set-name>
```

```bash
mongosh

> rs.initiate()  # 单节点副本集

> rs.initiate( {
  _id : "<replica-set-name>",
  members: [
    { _id: 0, host: "<ip1>:27017" },
    { _id: 1, host: "<ip2>:27017" },
    { _id: 2, host: "<ip3>:27017" }
  ]
})
```

#### Keyfile Authentication

```bash
openssl rand -base64 756 > <key-name>.key
chown mongodb:mongodb <key-name>.key
chmod 0400 <key-name>.key
```

```yaml
# /etc/mongod.conf

security:
  keyFile: <path/to/keyfile.key>
```
