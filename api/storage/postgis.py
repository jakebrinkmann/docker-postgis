import datetime

import psycopg2
import psycopg2.extras
from postgis.psycopg import register

from api import logger


def new(host=None, port=None, user=None, password=None, database=None):
    db = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
    register(db)
    return db

def commit(conn, sql, values):
    cursor = conn.cursor()
    query = cursor.mogrify(sql, values)
    logger.debug(query)
    cursor.execute(query)
    conn.commit()

def fetch(conn, sql, values):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = cursor.mogrify(sql, values)
    logger.debug(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows[:]

def insert(conn, table, columns, values, dups=True):
    on_conflict = 'ON CONFLICT DO NOTHING' if dups else ''
    sql = ('INSERT INTO ' + table + '(' + ', '.join(columns) + ') VALUES (' +
           ','.join(['%s'] * len(columns)) + ') ' + on_conflict)
    commit(conn, sql, values)

def geojson(conn, table, columns, geojson):
    sql = ('SELECT (ST_X(geom), ST_Y(geom), ' + ', '.join(columns) + ') FROM ' + table + ' WHERE ' +
           'ST_Within(geom, ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326))')
    return fetch(conn, sql, (geojson,))
