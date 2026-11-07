import requests
import pytest

URL = "https://jsonplaceholder.typicode.com/users/"
r = requests

@pytest.mark.parametrize("u, n", [('1', 'Leanne Graham'), ('2', 'Ervin Howell'), ('3', 'Clementine Bauch')])
def test_status_name(u, n):
    r1 = r.get(URL+u)
    assert r1.status_code == 200
    assert r1.json()['name'] == n

def test_usr_9999():
    r2 = r.get(URL+'9999')
    assert r2.status_code == 404
    assert r2.json() == {}

def test_address_city():
    r1 = r.get(URL+'1')
    adr = r1.json()['address']
    assert adr['city'] == 'Gwenborough'

def test_user_count():
    assert len(r.get(URL).json()) == 10