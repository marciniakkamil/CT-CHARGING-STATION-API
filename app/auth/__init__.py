"""Auth functionality used in the app.

Temporary used approach from the official FastAPI documentation.
"""

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext # type: ignore
from ..config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algoritm
ACCESS_TOKEN_EXPIRE_SECONDS = settings.access_token_exp_seconds

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
