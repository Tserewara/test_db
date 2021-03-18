FROM postgres:13.2-alpine

ARG POSTGRES_PASSWORD

ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

EXPOSE 5432

COPY init.sql /docker-entrypoint-initdb.d/https://github.com/Tserewara/test_db
