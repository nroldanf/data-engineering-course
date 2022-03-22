#!/bin/bash
set -e
dbname="tripdata"
init_script="ddl.sql"
hostname="my_host"
psql --username=root --dbname=$(dbname) -a -f $(init_script)