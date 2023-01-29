import pytest
import requests


@pytest.mark.http
def test_first_request():
    req = requests.get('https://api.github.com/zen')
    print(f"Text is {req.text}")


@pytest.mark.http
def test_second_request():
    req = requests.get('https://api.github.com/users/defunkt')
    body = req.json()

    assert body['name'] == "Chris Wanstrath"
    assert req.status_code == 200
    assert req.headers['Server'] == "GitHub.com"


@pytest.mark.http
def test_status_code_request():
    req = requests.get('https://api.github.com/users/sergii_butenko')

    assert req.status_code == 404
