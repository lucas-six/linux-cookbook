# Docker: Basic Usage

## Client

- Docker Desktop
- CLI
- DockerAPI

## Core Technologies

- namespace
- cgroups

## Basic Usage

```bash
docker [cmd] --help

docker run -i -t [--name <docker-name>] <image-name>:<image-tag>
docker run -d [--name <docker-name>] <image-name>:<image-tag>

docker start [-i] [-a] <container-id>
docker stop|kill <container-id>
docker rm [-f] <container-id>
docker ps

docker exec <container-id> <cmd>
docker attach <container-id>
```

### Images

```bash
docker images

docker pull|rmi <image-name>:<image-tag>

docker build -t <image-name>:<image-tag> <host-path>

docker run \
    -d \
    -w <container-working-path> \
    -p <host-port>:<container-port>[/[tcp|udp]] \
    -e <environment-variable-name>=<environment-variable-value> \
    [--name <docker-name>] <image-name>:<image-tag>

docker login -u <user-name>
docker push <user-name>/<image-name>:<image-tag>
```

### Persistent Storage: Volume

```bash
docker volume create <volume-name>

docker run -v [<host-path>|<volume-name>]:<container-path> <image-name>:<image-tag>
```

### Networking

```bash
docker network list
docker network create <network-name>

docker run --network <network-name> <image-name>:<image-tag>
```

### Build Images: `Dockerfile`

```dockerfile
# syntax=docker/dockerfile:1
FROM <image-name>:<image-tag>
LABEL org.opencontainers.image.authors="leven.cn@gmail.com"

RUN <shell-commands && ...>

VOLUME ["<persistent-data-container-path>", ...]
ENV <env_var>=<value>
WORKDIR <container-working-path>

COPY <host-file> <container-file>
CMD ["<command>", ...]

EXPOSE <container-port>[/udp]
```

Run:

```bash
cd <docker-working-path>
docker build -t <image-name>:<image-tag> .
docker scan <image-name>:<image-tag>

docker run \
    -d \
    -v <persistent-data-host-path=$PWD>:<persistent-data-container-path> \
    -p <host-port>:<container-port> \
    [--name <docker-name>] \
    <image-name>:<image-tag>
```

## References

- [Docker](https://www.docker.com)
