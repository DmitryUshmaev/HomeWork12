import logging

logger_mine = logging.getLogger("logger")
handler = logging.FileHandler(filename="main_logging.log", mode='w', encoding='utf-8')
formatter = logging.Formatter(fmt="->>> [%(levelname)s] : [%(asctime)s : %(message)s")
handler.setFormatter(formatter)
logger_mine.addHandler(handler)