from setuptools import find_packages
from setuptools import setup

setup(name='api',
      packages=find_packages(),
      install_requires=['psycopg2', 'postgis', 'geojson'],
      entry_points={
          'console_scripts': [
              'ingest=api.cli:ingest',
              'intersect=api.cli:intersect'],
      })
