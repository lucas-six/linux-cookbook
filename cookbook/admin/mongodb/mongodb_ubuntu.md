# MongoDB on Ubuntu

## Installation

**NOTE**: **`XFS`** filesystem is strongly recommended with the `WiredTiger` storage engine.

- [Install MongoDB Community Edition on Ubuntu](https://www.mongodb.com/zh-cn/docs/manual/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu)

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
sysctl --system
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
apt install -y numactl
```

```ini
# /lib/systemd/system/mongod.service

ExecStart=/usr/bin/numactl --interleave=all /usr/bin/mongod --config /etc/mongod.conf
```

```ini
# /etc/logrotate.d/mongodb

/var/log/mongodb/*.log {
        daily
        missingok
        rotate 30
        compress
        delaycompress
        notifempty
        create 640 mongodb adm
        sharedscripts
        postrotate
                kill -SIGUSR1 $(systemctl show --property MainPID --value mongod)
        endscript
}
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
openssl rand -base64 756 > mongodb.key
chown mongodb:mongodb mongodb.key
chmod 0400 mongodb.key
```

```yaml
# /etc/mongod.conf

security:
  keyFile: <path/to/keyfile.key>
```
