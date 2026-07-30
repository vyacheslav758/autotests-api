import httpx

# данные для авторизации
auth_params = {
    "email": "test100@test.com",
    "password": "12345"
}

# Выполняем POST-запрос к эндпоинту
response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=auth_params)
# Код ответа
print(response.status_code)
login_response_data = response.json()
# Тело ответа
print(login_response_data)

# Формируем header
headers = {"Authorization": "Bearer " + login_response_data["token"]["accessToken"]}
# Выполняем GET-запрос к эндпоинту
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
# Код ответа
print(response.status_code)
# Тело ответа
print(response.json())
