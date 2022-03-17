#!/bin/bash
set -e
psql --username=root --dbname=bikes -a -f SQL/ddl.sql