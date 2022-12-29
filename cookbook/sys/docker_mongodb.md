# Docker: MongoDB

## Build Image

```dockerfile
# syntax=docker/dockerfile:1
FROM mongo:5.0

VOLUME [ "/data/db" ]
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=123456

EXPOSE 27017
```

```bash
docker build -t leven1024/mongo:5.0 .
```

## Run Container

```bash
docker network create ly-devel 2> /dev/null
docker volume create ly-mongodb-data
# docker run -i --rm mongo:5.0 cat /etc/mongod.conf.orig > ly-mongodb.conf
docker run \
    -d \
    --network ly-network \
    --network-alias mongodb \
    -p 27017:27017 \
    -v ly-mongodb-data:/data/db \
    --name ly-mongodb \
    leven1024/mongo:5.0
```
