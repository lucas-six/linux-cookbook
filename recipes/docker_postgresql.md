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

## Run

```bash
docker network create <network-name> 2> /dev/null
docker run \
    -d \
    --network <network-name> --network-alias postgresql \
    --platform "linux/amd64" \
    -e POSTGRES_PASSWORD=<password> \
    -v <x>-postgresql-data:/var/lib/postgresql/data \
    -v "$PWD/<x>-postgresql.conf":/etc/postgresql/postgresql.conf \
    --name <x>-postgresql postgres:14 \
    postgres -c 'config_file=/etc/postgresql/postgresql.conf'
```

## References

- [Docker Hub: MongoDB](https://hub.docker.com/_/mongo)
