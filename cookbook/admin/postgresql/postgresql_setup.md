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

#listen_addresses = 'localhost'  # '*' for all
#port = 5432
max_connections = 4096
password_encryption = scram-sha-256  # md5 or scram-sha-256

shared_buffers = 256MB  # 128MB

client_encoding = 'UTF8'
#default_transaction_isolation = 'read committed'
#timezone = 'Etc/UTC'
```

```ini
# /etc/postgresql/16/main/pg_hba.conf

host all all 127.0.0.1/32 scram-sha-256

host all all all　　       scram-sha-256
```

```bash
systemctl enable|disable postgresql
systemctl start|stop|restart|status postgresql
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
