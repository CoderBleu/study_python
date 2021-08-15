'''
单例模式
'''
class Person:

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        # 单例模式，线程不安全的
        if not hasattr(cls, '_instance'):
             cls._instance = object.__new__(cls)
        return cls._instance

p1 = Person()
p2 = Person()
print(id(p1))
print(id(p2))