docker network create ly-devel 2> /dev/null
docker run \
    -d \
    --network ly-devel --network-alias postgresql \
    --platform "linux/amd64" \
    -e POSTGRES_PASSWORD=123456 \
    -v ly-postgresql-data:/var/lib/postgresql/data \
    -v "$PWD/postgresql.conf":/etc/postgresql/postgresql.conf \
    --name ly-postgresql postgres:14 \
    postgres -c 'config_file=/etc/postgresql/postgresql.conf'
