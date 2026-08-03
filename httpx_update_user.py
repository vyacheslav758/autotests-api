import httpx

from tools.fakers import get_random_email

random_email = get_random_email()

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_response.json()
assert create_response.status_code == 200

# Проходим авторизацию и получаем токен
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
assert create_response.status_code == 200
login_response_data = login_response.json()
print("Login data", login_response_data)
get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

# Изменяем почту пользователя на новую уникальную
update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
update_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=get_user_headers, json=update_user_payload
)
assert create_response.status_code == 200
print(update_response.json())
