FROM postgres:9.6.5

ENV PGDATA=/usr/local/pgsql/data
ENV POSTGRES_PASSWORD=password1
ENV POSTGRES_USER=postgis
ENV POSTGRES_DB=postgis
ENV POSTGRES_INITDB_ARGS="-D $PGDATA --locale en_US.UTF-8 -E UTF8 --auth-local=trust --auth-host=password"

ENV POSTGIS_MAJOR 2.3
ENV POSTGIS_VERSION 2.3.3+dfsg-1.pgdg80+1

RUN apt-get update \
      && apt-get install -y --no-install-recommends \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts=$POSTGIS_VERSION \
           postgis=$POSTGIS_VERSION \
      && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /docker-entrypoint-initdb.d
COPY db_schema.sql /docker-entrypoint-initdb.d/db_schema.sql
