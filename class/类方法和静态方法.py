import uuid

'''
静态方法主要来存放逻辑性的代码，本身和类已经实例对象多有交互，相当于 static final field
类方法属于类所有，相当于 static method
'''
class Student:

    stu_name = uuid.uuid4()

    # 标识这是一个类方法
    @classmethod
    def study(cls):
        return str(cls.stu_name) + '正在学习~'

print(Student.study())

import time
class TimeUtil:

    # 标识这是一个静态方法
    @staticmethod
    def get_current_time():
        # 时间格式化：2021:44:07/25/21
        return time.strftime('%Y:%M:%D')

print(TimeUtil.get_current_time())