import random

'''
函数属性：
1、通过property方法直接访问私有属性
    - 本来__weight是类私有属性，然后通过property后可以直接访问，但是还是会经过定义的get_weight和set_weight方法
2、通过装饰器修饰[注解]
    - @property 装饰器修饰，提供一个get方法
    - @age.setter 提供age字段的set方法
    - @age注解的字段名和函数名需要匹配
'''


class Person:

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self, weight):
        # 实例属性
        self.username = 'hello world'
        self.__age = 20
        # 加 __ 表示此为私有化属性
        self.__weight = weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    # 装饰器修饰，提供一个get方法
    @property
    def age(self):
        return self.__age

    # 标识age的set方法, 注意函数名为age，别错了
    @age.setter
    def age(self, age):
        self.__age = age

    # 这种方式就不能被set，只提供访问__weight方法
    # weight = property(get_weight)
    # 定义一个类属性，可以直接通过访问属性的形式去访问私有的属性
    weight = property(get_weight, set_weight)


obj = Person(110)
# 110
print(obj.get_weight())
# 本来__weight是类私有属性，然后通过property后可以直接访问，但是还是会经过定义的get_weight和set_weight方法
obj.weight = 10
# 10
print(obj.get_weight())
obj.set_weight(23)
# 23
print(obj.weight)

# 装饰器=================
print(obj.age)
obj.age = 18
print(obj.age)