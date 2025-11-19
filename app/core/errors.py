from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR


class BadRequest(HTTPException):
    def __init__(self, detail="Неверный запрос"):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)


class NotFound(HTTPException):
    def __init__(self, detail="Не найдено"):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=detail)


class InternalError(HTTPException):
    def __init__(self, detail="Внутренняя ошибка сервера"):
        super().__init__(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
