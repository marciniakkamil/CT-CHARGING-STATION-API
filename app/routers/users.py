"""Users routes"""
from typing import Annotated
from fastapi import APIRouter, Depends

from ..auth.auth import User, get_current_active_user

router = APIRouter(tags=["Users"])


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """Get current logged in users data"""
    return current_user
