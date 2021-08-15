'''
__new__中：请使用父类的new方法，不要使用对象本身的new方法，容易造成深度递归
子类重写了父类的方法，所以只输出子类的方法了
'''
class Person:

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self, weight):
        self.__weight = weight
        print('Person对象初始化方法，我会后执行')

    def __new__(cls, *args, **kwargs):
        print('Person对象new方法，我会先执行')
        # 请使用父类的new方法，不要使用对象本身的new方法，容易造成深度递归
        return object.__new__(cls)

class Male(Person):

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self):
        # 实例属性
        print('Male对象初始化方法，我会后执行')

    def __new__(cls, *args, **kwargs):
        print('Male对象new方法，我会先执行')
        return object.__new__(cls)

''' 
Person对象new方法，我会先执行
Person对象初始化方法，我会后执行
================ 【子类重写了父类的方法，所以只输出子类的方法了】
Male对象new方法，我会先执行
Male对象初始化方法，我会后执行
'''
p = Person(105)
print("================")
m = Male()
