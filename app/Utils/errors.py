# utils/errors.py
from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from Entities.error_entity import APIError

def raise_api_error(
    code: str,
    error: str,
    detail: str,
    status: int = HTTP_500_INTERNAL_SERVER_ERROR
):
    api_error = APIError(code=code, error=error, detail=detail, status=status)
    raise HTTPException(status_code=status, detail=api_error.dict())
