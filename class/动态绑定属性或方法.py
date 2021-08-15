'''
动态绑定属性 / 类方法
'''

import types

# 需要被绑定的实例方法
import uuid


def study(slef):
    print('我喜欢学习Python!')

@classmethod
def play(cls):
    print('我喜欢玩')

class Person:
    pass

p = Person()
# 动态绑定实例方法
p.study = types.MethodType(study, p)
p.study()

# 动态绑定类方法, 因为play方法单个参数self是默认的，不需要传参数
Person.play = play
Person.play()

# 动态绑定类属性
Person.id = uuid.uuid1()
print(Person.id)


