import logging
import sys

# 开启logging打印日志
import sys

LOG_FORMAT = "[%(asctime)s %(levelname)1.4s] %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=LOG_FORMAT)


try:
     i = 1 / 0
except Exception as e:
    logging.error('运算时异常', e)
finally:
    logging.info('异常学习')

print(dir(Exception))