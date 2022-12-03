# Docker: PostgreSQL

## Configuartion

```bash
docker run -i --rm postgres:14 cat /usr/share/postgresql/postgresql.conf.sample > <x>-postgresql.conf
```

```ini
# postgresql.conf

listen_addresses = '*'
max_connections  = 200
shared_buffers = 256MB
```

## Run Server

```bash
docker network create <network-name> 2> /dev/null
docker run \
    -d \
    --network <network-name> --network-alias postgresql \
    --platform "linux/amd64" \
    -p <host-port=5432>:<container-port=5432> \
    [-e POSTGRES_USER=<user=postgres>] \
    [-e POSTGRES_DB=<db=postgres>] \
    -e POSTGRES_PASSWORD=<password> \
    -v <x>-postgresql-data:/var/lib/postgresql/data \
    -v "$PWD/<x>-postgresql.conf":/etc/postgresql/postgresql.conf \
    --name <x>-postgresql postgres:14 \
    postgres -c 'config_file=/etc/postgresql/postgresql.conf'
```

## Run Client (CLI)

```bash
psql postgresql://<user>:<password>@localhost:<container-port>/<db>
```

## Run Client (PgAdmin4)

```bash
docker run \
    -d \
    -p 5433:80 \
    [-v "/path/to/certificate.cert:/certs/server.cert"] \
    [-v "/path/to/certificate.key:/certs/server.key"] \
    -e PGADMIN_DEFAULT_PASSWORD=123456 \
    -e PGADMIN_DEFAULT_EMAIL=<email> \
    [-e "PGADMIN_ENABLE_TLS=True" ]\
    --name pgadmin4 dpage/pgadmin4
```

NOTE: host = `host.docker.internal`

## References

- [Docker Hub: PostgreSQL](https://hub.docker.com/_/postgres)
- [Docker Hub: dpage/pgadmin4](https://hub.docker.com/r/dpage/pgadmin4)
