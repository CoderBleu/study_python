'''
多态条件
1、继承
2、子类重写父类方法
'''
'''
单继承：
默认继承超类，object
'''
class Animal(object):
    def eat(self):
        print('干饭了')

    @staticmethod
    def commonStaticSonClassMethod(obj):
        # 多态：调用的是父类静态方法，实际调用的确实子类对象的方法，
        obj.eat()

class dog(Animal):
    def eat(self):
        print('啃骨头')

class cat(Animal):
    def eat(self):
        print('偷鱼吃')

class_list = [dog(), cat()]

for item_class in class_list:
    Animal.commonStaticSonClassMethod(item_class)