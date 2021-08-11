#!/bin/bash

set -e

#Install dependencies 
bash scripts/setup.sh

#Run unit tests 
bash scripts/test.sh

#Build and push docker images 
bash scripts/build.sh

#Configure hosts for deployment
bash scripts/config.sh

#Deploy stack manager 
bash scripts/deploy.sh