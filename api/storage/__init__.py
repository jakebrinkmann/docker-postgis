import os

from . import config
from . import postgis as db

cfg_file = os.getenv('DB_CONFIG_PATH', './config.ini')
cfg = config.read(cfg_file, 'db')

def ingest(cols, data, table='mypointdata'):
    conn = db.new(**cfg)
    db.insert(conn, table, cols, data)

def intersect(cols, geojson, table='mypointdata'):
    conn = db.new(**cfg)
    return db.geojson(conn, table=table, columns=cols, geojson=geojson)
