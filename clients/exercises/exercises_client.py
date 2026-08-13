from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, PostCreateExerciseRequestSchema, \
    PatchUpdateExerciseRequestSchema, GetExercisesResponseSchema, GetCreateExerciseResponseSchema, \
    GetUpdateExerciseResponseSchema

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """Метод получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """Метод получение получение информации о задании по exercise_id.
        :param exercise_id: идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: PostCreateExerciseRequestSchema) -> Response:
        """Метод для создание задания.
        :param request: Словарь  title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: PatchUpdateExerciseRequestSchema) -> Response:
        """Метод для обновления данных задания.
        :param exercise_id: идентификатор задания
        :param request: Словарь  title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Метод для удаление задания.
        :param exercise_id: идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: PostCreateExerciseRequestSchema) -> GetCreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        print("Hello ", response.json())
        return GetCreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str,
                        request: PatchUpdateExerciseRequestSchema) -> GetUpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return GetUpdateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
