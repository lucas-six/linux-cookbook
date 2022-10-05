# Run PgAdmin4 in Docker
docker run \
    -d \
    -p 5433:80 \
    -e PGADMIN_DEFAULT_PASSWORD=123456 \
    -e PGADMIN_DEFAULT_EMAIL=ly@test.com \
    --name pgadmin4 dpage/pgadmin4
