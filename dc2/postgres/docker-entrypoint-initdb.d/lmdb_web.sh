#!/bin/env bash
psql -U postgres -c "CREATE USER $DB_USER PASSWORD '$DB_PASS'"
psql -U postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER"
# Be sure to change permissions on this file with:
# chmod a+rx postgres/docker-entrypoint-initdb.d/lmdb_web.sh
