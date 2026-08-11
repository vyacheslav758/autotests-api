from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Модель пользователя."""
    id: str
    email: EmailStr = Field(default="user@example.com")
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Модель для создания пользователя."""

    email: EmailStr = Field(default="user@example.com")
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Модель ответа о создании пользователя."""
    user: UserSchema

