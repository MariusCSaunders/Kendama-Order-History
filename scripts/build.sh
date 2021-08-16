#!/bin/bash

set -e

#Build images
docker-compose build --parallel

#Push images
docker login -u ${DOCKERHUB_USR} -p ${DOCKERHUB_PSW}
docker-compose push
