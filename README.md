# db-postgres-postgis 

PostGIS brings all of the awesomeness of GDAL (proj4/geos) into a PostgreSQL DB

## Core Stack

* PostgreSQL 9.6 :elephant:
* PostGIS 2.3 :globe_with_meridians:
* Python 3.6 (datbase API)

## Running

Initialize the Postgres/PostGIS database service:
```bash
docker-compose -f setup/docker-compose.yml up --build
```

Build this project image:
```bash
docker build -t postgis-points .
```

Ingest some point data into the database:
```bash
cat data/targets.dat | docker run -i --rm postgis-points ingest
```

**NOTE**: There are stored procedures which convert Latitude/Longitude into the 
internal PostGIS `Geom` spatial index type

Query the data using GeoJSON polygons:
```bash
cat data/USA.geojson | docker run -i --rm intersect
```

## References

* https://postgis.net/docs/using_postgis_dbmanagement.html
* https://github.com/appropriate/docker-postgis
* https://live.osgeo.org/en/quickstart/postgis_quickstart.html
* https://github.com/yohanboniface/python-postgis

