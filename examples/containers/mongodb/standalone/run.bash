docker build -t leven1024/mongo:5.0 . || exit $?

docker network create ly-network 2> /dev/null
rm -rf docker-volumes
docker run \
    -d \
    --network ly-network \
    --network-alias mongodb \
    -p 27017:27017 \
    -v "$PWD/docker-volumes/data/db:/data/db" \
    -v "$PWD/docker-volumes/data/configdb:/data/configdb" \
    --name ly-mongodb \
    leven1024/mongo:5.0
