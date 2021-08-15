import logging

# 开启logging打印日志
import sys

LOG_FORMAT = "[%(asctime)s %(levelname)1.4s] %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=LOG_FORMAT)

class TooLongMyException(Exception):
    def __init__(self, len):
        self.len = len

    def __str__(self):
        return '您输入的姓名数据长度是' + str(self.len) + '超过了长度'

input = input()

try:
    if len(input) > 5:
        raise TooLongMyException(len(input))
    else:
        print('您输入的数据为：' + input)
except TooLongMyException as e:
    # logging.error(e)
    logging.error('捕获自定义异常啦', e)
    pass