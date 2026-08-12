from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel):
    """Описание модели файла."""
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """Описание модели запроса на создание файла."""
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """Описание модели ответа создания файла."""
    file: FileSchema
