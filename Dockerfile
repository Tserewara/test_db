FROM postgres:13.2-alpine

EXPOSE 5432

COPY init.sql /docker-entrypoint-initdb.d/

