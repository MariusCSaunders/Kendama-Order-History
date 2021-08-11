#!/bin/bash

docker-compose build --parallel && \
#!/bin/bash

set -e

#Build images
docker-compose build --parrallel

#Push images
docker login -u ${DOCKERHUB} -p ${DOCKERHUB}
docker-compose push