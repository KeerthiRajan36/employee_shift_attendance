from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from fastapi.exceptions import RequestValidationError

from starlette.exceptions import HTTPException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException
    ):

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.detail
            }
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ):

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "errors": exc.errors()
            }
        )

    @app.exception_handler(Exception)
    async def common_exception(
        request: Request,
        exc: Exception
    ):

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(exc)
            }
        )