from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """Описание модели курса."""
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    previewFile: FileSchema  # Вложенная структура файла
    estimated_time: str = Field(alias="estimatedTime")
    createdByUser: UserSchema  # Вложенная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """Описание модели запроса на получение списка курсов."""
    userId: str


class CreateCourseRequestSchema(BaseModel):
    """Описание модели запроса на создание курса."""
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


# Добавили описание структуры ответа на создание курса
class CreateCourseResponseSchema(BaseModel):
    """Описание модели ответа создания курса."""
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """Описание модели запроса на обновление курса."""
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
