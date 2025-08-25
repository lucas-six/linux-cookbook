# PostgreSQL - Setup

## Basic Concepts

- Relational Database Management System, **RDBMS** (关系型数据库管理系统)
- Structured Query Language, **SQL** (结构化查询语言)
- **ACID**: Atomicity(原子性), Consistency(一致性), Isolation(隔离性), Durability(持久性)
- **Transaction** (事务)

## Installation

See [Download PostgreSQL](https://www.postgresql.org/download/).

## Configuration

```conf
# /etc/postgresql/16/main/postgresql.conf

listen_addresses = '*'  # 'localhost' by default, '*' for all
#port = 5432
max_connections = 100  # 100 by default
password_encryption = scram-sha-256  # md5 or scram-sha-256

shared_buffers = 256MB  # 1/4 or 1/2 of physical RAM

work_mem = 16MB  # 1/16 of shared_buffers
max_wal_size = 1GB  # 1/2 of shared_buffers, but not less than 1GB

client_encoding = 'UTF8'
#default_transaction_isolation = 'read committed'
#timezone = 'Etc/UTC'
```

```ini
# /etc/postgresql/16/main/pg_hba.conf

# Unix domain socket, 'peer' by default
local   all             all                                     trust

# IPv4
host    all             all             127.0.0.1/32            scram-sha-256
host    all             lucas           0.0.0.0/0               scram-sha-256

# IPv6
host    all             all             ::1/128                 scram-sha-256
```

```bash
systemctl enable|disable postgresql@16
systemctl start|stop|restart|status postgresql@16
```

```bash
su - postgres
psql

# list users
> \du

# set password for superuser 'postgres'.
> ALTER USER postgres WITH PASSWORD 'PASSWORD';

# quit
> \q
```
