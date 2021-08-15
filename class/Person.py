'''
类：
'''
import logging
import sys

class Person:
    # 类属性
    username = 'hello world'

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self):
        # 实例属性
        self.age = 20

    # 实例方法
    def study(self, name=username):
        print("%s study Python!" % name)
        print("{} study Python! And realy age is {}".format(name, 20))

    def __str__(self):
        return 'username=' + self.username + ',age=' + str(self.age)


'''
创建一个对象
------
两者打印出来的内存地址都一样的
---
4381304016
...
18
===================>
<class 'int'>
4381304016
...
20
'''
obj = Person()
print(type(obj.age))
print(id(obj.age))
# 修改的是当前对象的age值
obj.age = 18
print(id(obj.username))
obj.tag = '标签'
print(id(obj.tag))
print(obj.age)

print("===================>")
print(obj.__str__())
print("===================>")

obj1 = Person()
print(type(obj1.age))
print(id(obj1.age))
print(id(obj1.username))
obj1.tag = '标签'
print(id(obj1.tag))
print(obj1.age)
