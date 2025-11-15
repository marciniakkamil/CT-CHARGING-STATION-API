"""Main Application"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.database.db_initializer import DBInitializer
from .database.database import engine, Base
from .routers import (
    main,
    charging_station_types,
    charging_stations,
    connectors,
    users,
    auth,
)
from .middleware import logger_requests_middleware, db_session_middleware
from .utils.logger import logger


@asynccontextmanager
async def lifespan(main_app: FastAPI):
    """create database tables and add functions and triggers"""
    # todo: learn and try to use Alembic later
    logger.info("App startup: Creating tables")
    Base.metadata.create_all(bind=engine)

    logger.info("App startup: Creating DB functions and triggers")
    DBInitializer.create_functions_and_triggers()

    logger.info("App startup: Filling DB with the sample data")
    DBInitializer.create_sample_data()
    yield
    # clean up


app = FastAPI(title="Charging Station - backend API", lifespan=lifespan)
app.add_middleware(BaseHTTPMiddleware, dispatch=logger_requests_middleware)
app.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)

# API Routes
app.include_router(main.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(charging_station_types.router)
app.include_router(charging_stations.router)
app.include_router(connectors.router)
