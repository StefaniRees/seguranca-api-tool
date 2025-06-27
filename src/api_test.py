import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
    ]
)

BASE_URL = "https://reqres.in/api"

def get_posts(token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        response = requests.get(f"{BASE_URL}/users", headers=headers, timeout=5)
        logging.info(f"GET /users - Status: {response.status_code}")
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            try:
                logging.info(f"Resposta: {response.json()}")
            except ValueError:
                logging.info("Resposta JSON inválida")
        else:
            logging.info("Resposta não é JSON")
        return response
    except requests.RequestException as e:
        logging.error(f"Erro na requisição GET /users: {e}")
        return None

def login(email, password):
    try:
        response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password}, timeout=5)
        logging.info(f"POST /login - Status: {response.status_code}")
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            try:
                logging.info(f"Resposta: {response.json()}")
            except ValueError:
                logging.info("Resposta JSON inválida")
        else:
            logging.info("Resposta não é JSON")
        return response.json().get("token")
    except requests.RequestException as e:
        logging.error(f"Erro no login: {e}")
        return None

def check_cors():
    headers = {"Origin": "http://maliciosa.com"}
    try:
        response = requests.options(f"{BASE_URL}/users", headers=headers, timeout=5)
        logging.info(f"OPTIONS /users - Status: {response.status_code}")
        logging.info(f"Headers: {response.headers}")
        return response
    except requests.RequestException as e:
        logging.error(f"Erro na requisição OPTIONS para CORS: {e}")
        return None

def put_method_test():
    try:
        response = requests.put(f"{BASE_URL}/users", timeout=5)
        logging.info(f"PUT /users - Status: {response.status_code}")
        return response
    except requests.RequestException as e:
        logging.error(f"Erro na requisição PUT: {e}")
        return None
