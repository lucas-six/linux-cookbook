# MongoDB on Ubuntu

## Installation

**NOTE**: **`XFS`** filesystem is strongly recommended with the `WiredTiger` storage engine.

```bash
apt install apt apt-utils python-apt-common python3-apt wget gnupg systemd

# for v4.4
# wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
# echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# for 5.0
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

apt update
apt install mongodb-org
```

## Configuration

```conf
# /etc/sysctl.d/30-mongodb.conf

vm.swappiness = 0
vm.overcommit_memory = 1
net.core.somaxconn = 4096
net.core.netdev_max_backlog = 4096
net.ipv4.tcp_max_syn_backlog = 4096
```

```bash
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
  # wiredTiger:
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

```bash
chown -R mongodb:mongodb </var/lib/mongodb>

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
  bindIp: localhost,10.0.0.1,10.0.0.2

replication:
  replSetName: <replica-set-name>
```

```bash
mongosh

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
openssl rand -base64 756 > <key>.key
chmod 0400 <key>.key
```

```yaml
# /etc/mongod.conf

security:
  keyFile: <path/to/keyfile.key>
```

## Initialization

```bash
mongosh

# Super Admin (Standalone)
> db.createUser(
{
  user: "<super_admin_name>",
  pwd: passwordPrompt(),
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" }
  ]
})

# Super Admin (Replica Set)
> db.createUser(
{
  user: "<super_admin_name>",
  pwd: passwordPrompt(),
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" },
    { role: "clusterAdmin", db: "admin" }
  ]
})

# DB Owner
> db.createUser(
{
  user: "<db_owner_name>",
  pwd: passwordPrompt(),
  roles: [
    { role: "dbOwner", db: "<db_name>" }
  ]
})
```

## Client Usage

### Standalone URL

```url
mongodb://<user>:<pwd>@<ip>:<port=27017>/<db_name>?authMechanism=SCRAM-SHA-256&connectTimeoutMS=3500
```

### Replica Set URL

```url
mongodb://<user>:<pwd>@<ip1>:<port=27017>,<ip2>:<port=27017>,<ip3>:<port=27017>/<db_name>?replicaSet=<rs-name>&authMechanism=SCRAM-SHA-256&maxPoolSize=4096&connectTimeoutMS=3500
```
