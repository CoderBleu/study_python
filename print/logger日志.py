'''
类：
'''
import logging
import sys

# 开启logging打印日志
LOG_FORMAT = "[%(asctime)s %(levelname)1.4s] %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=LOG_FORMAT)

name = 'hello world'
print("%s study Python!" % name)
print("{} study Python! And realy age is {}".format(name, 20))
# %s study Python!
logging.info("%s study Python!", name)
