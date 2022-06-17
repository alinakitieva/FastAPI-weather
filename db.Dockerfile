FROM postgres:12.2

COPY bin/db-init.sh /docker-entrypoint-initdb.d/
