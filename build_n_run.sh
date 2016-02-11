#!/bin/sh
docker build .
IMAGE_ID="$(docker images -q | head -n 1)"
CONTAINER_ID="$(docker run -d -p 8080:8080 -v $(pwd):/code $IMAGE_ID)"
echo "running container id is $CONTAINER_ID"
