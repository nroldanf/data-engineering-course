#!/bin/bash
set -e
dbname="bikes"
init_script="ddl.sql"
psql --username=root --dbname=$(dbname) -a -f $(init_script)