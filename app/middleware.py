"""API's middlewares declarations"""
import traceback
from fastapi import Request, Response
from .database.database import SessionLocal
from .utils.logger import logger


async def db_session_middleware(request: Request, call_next):
    """middleware for auto closing db connection"""
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


async def logger_requests_middleware(request: Request, call_next):
    """requests logger middleware"""
    # add some context data to {event} variable in the logger output formatter
    child_logger = logger.bind(client=request.client)
    # passing dict with main logger message structure for request
    child_logger.info(
        {
            "message": "New Request",
            "url": request.url.path,
            "method": request.method,
        }
    )
    try:
        return await call_next(request)
    except Exception as e:
        # needed to log app errors with loguru
        child_logger.error(traceback.format_exc())
        raise e
