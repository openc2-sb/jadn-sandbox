#!/bin/bash 

set -e

if [ "$#" -ne 2 ]
then
  echo "Version arguments not supplied, see docker_push.py"
  exit 1
fi

prev_version=$1
echo "prev docker version: $prev_version"

new_version=$2
echo "new docker version: $new_version"

# GUI Build
cd client
yarn
yarn build

# Container
PREV_IMG="screambunn/jadn_sandbox:$prev_version"
NEW_IMG="screambunn/jadn_sandbox:$new_version"
IMG_LATEST="screambunn/jadn_sandbox:latest"

# Sync Built GUI Files
cd ../
rsync -avz --delete ./client/build/* ./server/webApp/static/
cp ./server/webApp/static/index.html ./server/webApp/templates/index.html

# Stop and remove previous image
cd ./server
if [ "$(docker ps -aq --filter "name=$PREV_IMG")" != "" ]; then
  docker stop $PREV_IMG && docker rm -fv $PREV_IMG
fi

docker images -q $PREV_IMG 2>&1 >/dev/null
if [ $? -eq 1 ]; then
  docker rmi $PREV_IMG
fi


# Ensure docker buildx is available
if ! docker buildx version > /dev/null 2>&1; then
  echo "Docker buildx is not installed or not available. Please install Docker buildx."
  exit 1
fi

docker login
# Build and push multi-platform image (linux/amd64 and linux/arm64)
if ! docker buildx rm jadn-multiplatform-builder 2>/dev/null; then
  echo "Warning: buildx builder 'jadn-multiplatform-builder' not found or could not be removed. Continuing..."
fi
docker buildx create --use --platform=linux/amd64,linux/arm64 --name jadn-multiplatform-builder
docker buildx build --platform linux/arm64,linux/amd64 -f ./server/Dockerfile -t $NEW_IMG --push .

{
  docker buildx build --platform linux/arm64,linux/amd64 -f ./server/Dockerfile -t $IMG_LATEST --push .
} || {
  exit $1
}

echo "Docker images pushed: $NEW_IMG and $IMG_LATEST"