import sys
import logging

logger = logging.getLogger(__name__)
formatter =logging.Formatter(
    fmt ="%(asctime)s - %(name)s- %(levelname)s - %(message)s", datefmt = "%Y-%m-%d %H:%M:%S"
)

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app.log")

stream_handler.setFormatter(fmt=formatter)
file_handler.setFormatter(fmt=formatter)

logger.handlers = [stream_handler,file_handler]

logger.setLevel(level = logging.INFO)
# logging = logging.getLogger(__name__)
# logger.addHandler(hdlr = handler)