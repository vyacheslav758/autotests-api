from __future__ import annotations
from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания нового пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """Метод создания нового пользователя.

        :param request Словарь email, password, lastName, fistName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
