import pytest_django
from api.models import ConnectionDB
from decouple import config

host = config('DB_HOST')
port = config('DB_PORT', cast=int)
client = ConnectionDB(host, port)

def test_connection():
    db = client.connection()
    assert db.name == 'molica'