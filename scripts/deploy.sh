#!/bin/bash

rsync -r docker-compose.yaml nginx docker-manager:
ssh docker-manager << EOF
    docker stack deploy --compose-file docker-compose.yaml kendama-order
EOF