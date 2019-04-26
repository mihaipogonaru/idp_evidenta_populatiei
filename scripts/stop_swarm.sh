#!/bin/bash

docker stack rm idp_evp
docker swarm leave --force
