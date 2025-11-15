"""Logger instance and configuration"""
import logging
import sys

logger = logging.getLogger()

formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app.log")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]

logger.setLevel(logging.INFO)
