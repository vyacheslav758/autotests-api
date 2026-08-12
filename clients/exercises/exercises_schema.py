from pydantic import BaseModel, ConfigDict, Field


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий для курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    courseId: str  = Field(alias="courseId")


class ExerciseSchema(BaseModel):
    """Описание структуры задания."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """Описание структуры ответа на выгрузку всех заданий."""
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """Описание структуры ответа на выгрузку задания."""
    exercises: ExerciseSchema


class GetUpdateExerciseResponseSchema(BaseModel):
    """Описание структуры ответа на обновление существующего задания."""
    exercises: ExerciseSchema


class GetCreateExerciseResponseSchema(BaseModel):
    """Описание структуры ответа создание нового задания."""
    exercise: ExerciseSchema


class PostCreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса создания нового задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    min_score: int = Field(alias="minScore")
    max_score: int = Field(alias="maxScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class PatchUpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления существующего задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    min_score: int = Field(alias="minScore")
    max_score: int = Field(alias="maxScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
