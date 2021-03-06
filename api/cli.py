import sys
import json

import api.storage as storage

def __parse__(stdin):
    return [(l[:35].strip(), float(l[35:50]), float(l[50:])) for l in stdin]

def ingest(data=None):
    if data is None:
        data = sys.stdin.read().splitlines()
    cols, data = data[0].split(), data[1:]
    data = __parse__(data)
    for d in data:
        storage.ingest(cols, d)

def intersect(cols=('Name',), geojson=None):
    if geojson is None:
        geojson = json.loads(sys.stdin.read())['features'][0]['geometry']
    results = storage.intersect(cols, json.dumps(geojson))
    print('\n'.join(results))
