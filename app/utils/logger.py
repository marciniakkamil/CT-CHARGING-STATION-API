"""Logger instance and configuration"""
import sys
from loguru import logger

logger.remove()
logger.add(
    sys.stdout,
    format=(
        "{time: YYYY-MM-DD HH:mm:ss zz} "
        "[<level>{level}</level>][{extra}]: <level>{message}</level>"
    ),
)
logger.add(
    "app.log",
    format=(
        "{time: YYYY-MM-DD HH:mm:ss zz} "
        "[<level>{level}</level>][{extra}]: <level>{message}</level>"
    ),
)
