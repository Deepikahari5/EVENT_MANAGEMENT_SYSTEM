from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    NotFoundException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException
)
from fastapi.exceptions import RequestValidationError


def sanitize(value):
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, dict):
        return {k: sanitize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [sanitize(i) for i in value]
    return value


async def not_found_exception_handler(
    request: Request,
    exc: NotFoundException
):
    return JSONResponse(
        status_code=404,
        content={"success": False, "message": exc.detail}
    )


async def bad_request_exception_handler(
    request: Request,
    exc: BadRequestException
):
    return JSONResponse(
        status_code=400,
        content={"success": False, "message": exc.detail}
    )


async def unauthorized_exception_handler(
    request: Request,
    exc: UnauthorizedException
):
    return JSONResponse(
        status_code=401,
        content={"success": False, "message": exc.detail}
    )


async def forbidden_exception_handler(
    request: Request,
    exc: ForbiddenException
):
    return JSONResponse(
        status_code=403,
        content={"success": False, "message": exc.detail}
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "errors": sanitize(exc.errors())
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={"success": False, "message": "Internal Server Error"}
    )