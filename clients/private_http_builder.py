from httpx import Client
from typing import TypedDict

from clients.autentification.autentification_client import get_authentication_client, LoginRequestDict


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login_api(login_request).json()
    login_token = login_response['token']['accessToken']
    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации
        headers={"Authorization": f"Bearer {login_token}"}
    )