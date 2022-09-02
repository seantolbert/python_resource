# # # standard logging format

# import logging
# # logging.basicConfig(level=logging.DEBUG,
# #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# # # adding your own name to the logger
# # # log helper
# # logger = logging.getLogger(__name__)
# # logger.info('hello from the helper')

# logger = logging.getLogger(__name__)

# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # set the level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# # add handler to the logger
# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warning')
# logger.error('this is an error')

# import logging, traceback

# try:
#     a = [1, 2, 3]
#     b = a[4]
# except IndexError as e:
#     # exc_info tells the terminal to show you where the error occurred as well
#     logging.error(e, exc_info=True)

# # maybe we do not know what kind of error to prepare for
# try:
#     a = [1, 2, 3]
#     b = a[4]
# except:
#     logging.error("the error is %s", traceback.format_exc())

import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.py', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('hello world')