import pytest
import logging
from src.api_test import login, get_posts, check_cors, put_method_test

log = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def token_valido():
    return "token_valido123"

@pytest.fixture
def mock_get_posts(requests_mock):
    url = "https://reqres.in/api/users"

    def matcher_valido(request):
        return request.headers.get("Authorization") == f"Bearer token_valido123"

    def matcher_invalido(request):
        auth = request.headers.get("Authorization")
        return auth != f"Bearer token_valido123"

    requests_mock.get(
        url,
        status_code=200,
        json={"data": [{"id": 1, "name": "User 1"}]},
        headers={"Content-Type": "application/json"},
        additional_matcher=matcher_valido
    )
    requests_mock.get(
        url,
        status_code=401,
        json={"error": "Unauthorized"},
        headers={"Content-Type": "application/json"},
        additional_matcher=matcher_invalido
    )

@pytest.fixture
def mock_check_cors(requests_mock):
    url = "https://reqres.in/api/users"
    requests_mock.options(
        url,
        status_code=200,
        headers={"Access-Control-Allow-Origin": "*"}
    )

@pytest.fixture
def mock_put_method(requests_mock):
    url = "https://reqres.in/api/users"
    requests_mock.put(
        url,
        status_code=405,
        headers={"Content-Type": "application/json"}
    )  # Método PUT não permitido

def test_acesso_sem_token(mock_get_posts):
    r = get_posts(token=None)
    log.info(f"[test_acesso_sem_token] Status: {r.status_code}")
    assert r is not None
    assert r.status_code == 401

def test_acesso_token_invalido(mock_get_posts):
    r = get_posts(token="token_invalido")
    log.info(f"[test_acesso_token_invalido] Status: {r.status_code}")
    assert r is not None
    assert r.status_code == 401

def test_acesso_token_expirado(mock_get_posts):
    r = get_posts(token="token_expirado")
    log.info(f"[test_acesso_token_expirado] Status: {r.status_code}")
    assert r is not None
    assert r.status_code == 401

def test_acesso_token_valido(token_valido, mock_get_posts):
    r = get_posts(token=token_valido)
    log.info(f"[test_acesso_token_valido] Status: {r.status_code}, Response data keys: {list(r.json().keys())}")
    assert r is not None
    assert r.status_code == 200
    data = r.json()
    assert "data" in data

def test_header_content_type(token_valido, mock_get_posts):
    r = get_posts(token=token_valido)
    log.info(f"[test_header_content_type] Headers: {r.headers}")
    assert r is not None
    assert "Content-Type" in r.headers
    assert "application/json" in r.headers["Content-Type"]

def test_cors_header(mock_check_cors):
    r = check_cors()
    log.info(f"[test_cors_header] Headers: {r.headers}")
    assert r is not None
    assert "Access-Control-Allow-Origin" in r.headers

def test_metodo_put_proibido(mock_put_method):
    r = put_method_test()
    log.info(f"[test_metodo_put_proibido] Status: {r.status_code}")
    assert r is not None
    assert r.status_code in [403, 404, 405]
