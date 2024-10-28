import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('api_logger')
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('api.log', maxBytes=10000000, backupCount=1)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

