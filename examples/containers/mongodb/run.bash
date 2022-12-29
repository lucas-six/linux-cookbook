docker network create ly-devel 2> /dev/null
docker volume create ly-mongodb-data
docker run \
    -d \
    --network ly-network \
    --network-alias mongodb \
    -p 27017:27017 \
    -v ly-mongodb-data:/data/db \
    --name ly-mongodb \
    leven1024/mongo:5.0
