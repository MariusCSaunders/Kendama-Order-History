#!/bin/bash


rsync -r docker-compose.yaml nginx docker-manager:

ssh docker-manager << EOF
    sudo usermod -aG docker $USER
    docker login -u ${DOCKERHUB_USR} -p ${DOCKERHUB_PSW}
    docker stack deploy --compose-file docker-compose.yaml kendama-order
EOF