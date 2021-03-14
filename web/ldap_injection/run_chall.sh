#!/bin/sh

docker-compose up --detach --build && echo 'Challenge is available at http://challs.dvc.tf:8080' || echo 'Challenge failed to run ... Are you in docker group ?'
