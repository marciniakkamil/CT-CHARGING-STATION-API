"""Main app routes"""
from fastapi import APIRouter

router = APIRouter(tags=["Main"])


@router.get("/")
def main():
    """Main path of the API"""
    return {"message": "Welcome to Charging Station - backend API!"}


@router.get("/healthcheck")
def root():
    """Healthcheck endpoint"""
    return {"message": "Charging Station - backend API is running!"}
