#!/bin/bash


rsync -r docker-compose.yaml nginx docker-manager:

ssh docker-manager << EOF
    sudo usermod -aG docker $USER
    export DATABASE_URI=${DATABASE_URI}
    export MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
    docker stack deploy --compose-file docker-compose.yaml kendama-order
EOF