from peewee import SqliteDatabase

SPOTIFY_CLIENT_ID = ''
SPOTIFY_CLIENT_SECRET = ''
# JUST the IP of the host. Use the default mopidy ports
MOPIDY_HOST = ''

"""
Configure a Provider and player in config_local.py!!!
Example:
PROVIDER = Spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
PLAYER = Mopidy(MOPIDY_HOST, PROVIDER)
"""

SITE_NAME = 'ISETunes'
SECRET_KEY = 'something long and random'
DEBUG = False
DB = SqliteDatabase('db.sql')
# Make sure to include the ldap:// protocol string
LDAP_HOST = ''
LDAP_BASE_DN = ''
LDAP_PORT = 389
LDAP_SSL = False
LDAP_FILTER = 'objectClass=User'
VOTES_TO_PLAY = 3
VOTES_TO_SKIP = 3
MAX_OPEN_REQUESTS = 5

try:
    from config_local import *
except ImportError:
    pass
