CREATE DATABASE template_postgis;
UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template_postgis';

CREATE EXTENSION IF NOT EXISTS postgis;

-- CREATE DATABASE demo;
-- \connect demo

create table MYPOINTDATA (id serial primary key,
                          NAME varchar(50),
                          LONGITUDE decimal(7,4),
                          LATITUDE decimal(7,4),
                          geom geometry(point, 4326),
                          modified timestamp without time zone);

CREATE OR REPLACE Function update_geom() RETURNS TRIGGER AS $$
    BEGIN 
      NEW.geom := ST_SetSRID(ST_Makepoint(NEW.LONGITUDE,NEW.LATITUDE),4326) where NEW.geom isnull;
	  NEW.modified := now();
      RETURN NEW;
    END;
    $$ LANGUAGE 'plpgsql';

CREATE TRIGGER geom_trigger BEFORE INSERT OR UPDATE ON MYPOINTDATA FOR EACH ROW EXECUTE PROCEDURE update_geom();
