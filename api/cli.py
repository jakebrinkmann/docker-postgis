import sys

import api.storage as storage

def ingest(data=None):
    if data is None:
        data = sys.stdin.readlines()
    cols, d = data[0].split(), data[1:]
    storage.ingest(cols, d)

def intersect(cols=('Name',), geojson=None):
    if geojson is None:
        geojson = sys.stdin.read()
    return storage.intersect(cols, geojson)
