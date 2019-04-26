#!/bin/bash

docker volume rm idp_evidenta_populatiei_idp_evp_db-data
docker network rm idp_evidenta_populatiei_default idp_evp_default idp_evp_frontend idp_evp_admin
