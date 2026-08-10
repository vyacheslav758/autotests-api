from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий для курса.
    """
    courseId: str


class Exercise(TypedDict):
    """Описание структуры задания."""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """Описание структуры ответа на выгрузку всех заданий."""
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """Описание структуры ответа на выгрузку задания."""
    exercises: Exercise


class GetUpdateExerciseResponseDict(TypedDict):
    """Описание структуры ответа на обновление существующего задания."""
    exercises: Exercise


class GetCreateExerciseResponseDict(TypedDict):
    """Описание структуры ответа создание нового задания."""
    exercises: Exercise


class PostCreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса создания нового задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class PatchUpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления существующего задания.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """Метод получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """Метод получение получение информации о задании по exercise_id.
        :param exercise_id: идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: PostCreateExerciseRequestDict) -> Response:
        """Метод для создание задания.
        :param request: Словарь  title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: PatchUpdateExerciseRequestDict) -> Response:
        """Метод для обновления данных задания.
        :param exercise_id: идентификатор задания
        :param request: Словарь  title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Метод для удаление задания.
        :param exercise_id: идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: PostCreateExerciseRequestDict) -> GetCreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str,
                        request: PatchUpdateExerciseRequestDict) -> GetUpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()


def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
