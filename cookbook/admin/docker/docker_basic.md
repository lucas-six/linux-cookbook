# Docker: Basic Usage

## Installation

- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

## Basic Usage

```bash
docker images
docker pull <image-name>:<image-tag>
docker rmi <image-name>:<image-tag>

docker ps -a
docker run -it [--name <container-name>] [--env-file <environment-file-path>] <image-name>:<image-tag>
docker run \
    -d \
    -w <container-working-path> \
    --network=host \
    -p <host-port>:<container-port>[/[tcp|udp]] \
    -e <environment-variable-name>=<environment-variable-value> \
    [--env-file <environment-file-path>] \
    [--name <container-name>] <image-name>:<image-tag>

docker logs -f <container-name-or-container-id>

docker start [-i] [-a] <container-id>
docker stop|kill <container-id>
docker rm [-f] <container-id>

docker <cmd> --help
```

## Build

`Dockerfile`:

```dockerfile
# syntax=docker/dockerfile:1
FROM <image-name>:<image-tag>
LABEL org.opencontainers.image.authors="lucassix.lee@gmail.com"

RUN <shell-commands && ...>

VOLUME ["<persistent-data-container-path>", ...]
ENV <env_var>=<value> ...
WORKDIR <container-working-path>

COPY [--from=<image-name>:<image-tag>OR<image-alias>] [--chown=<user>:<group>] <source-file> ... <destination-file>
CMD ["<command>", ...]

EXPOSE <container-port>[/udp]
```

```bash
cd <docker-working-path>
docker build [-f <dockerfile-path=Dockerfile>] -t <image-name>:<image-tag> .
docker scan <image-name>:<image-tag>

docker run \
    -d \
    -v <persistent-data-host-path=$PWD>:<persistent-data-container-path> \
    -p <host-port>:<container-port> \
    [--name <container-name>] \
    [--env-file <environment-file-path>] \
    <image-name>:<image-tag>
```

## Publish Images

```bash
docker build -t <image-name>:<image-tag> <host-path>
docker login -u <user-name>
docker push <user-name>/<image-name>:<image-tag>

# Rename
docker tag docker/<old-image-name> <user-name>/<new-image-name>
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

## Others

```bash
docker exec <container-id> <cmd>
docker attach <container-id>
```

## References

- [Docker Home](https://www.docker.com)
- [Docker Documentation](https://docs.docker.com)
