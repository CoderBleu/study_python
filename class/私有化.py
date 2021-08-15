import random

'''
私有化属性：
1、私有化的 实例属性，不能再被外部直接访问，可以在本类中使用修改
2、在属性名前加 __ 就可以变成私有化了
'''
class Person:

    id = random.randrange(1, 100, 10)

    tag_ = '后面单下划线，避免属性名与Python关键字冲突'

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self, weight):
        # 实例属性
        self.username = 'hello world'
        self.age = 20
        # 加 __ 表示此为私有化属性
        self.__weight = weight

    def __set_id(self):
        self.id = '我是私有化方法'
        return self.id

    # 只能允许本身或者子类访问，不能同步from ** import * 导入
    def _protected_method(self):
        print('我是受保护的方法')

    def __magic__(self):
        print('魔法方法，一般是Python自有的')

    # 实例方法
    def get_person(self):
        print('我在对象内部先调用了:' + self.__set_id())
        return '{}的年龄是{}，体重{}'.format(self.username, self.age, self.__weight)


obj = Person(110)

print(obj.get_person())
# AttributeError: 'Person' object has no attribute '__weight'
# print(obj.__weight)
