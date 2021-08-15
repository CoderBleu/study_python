'''
单继承：
默认继承超类，object
'''
class Animal(object):
    def eat(self):
        print('干饭了')

    def sing(self):
        print('唱歌了')

class dog(Animal):
    def eat(self):
        print('啃骨头')

class cat(Animal):
    def eat(self):
        print('偷鱼吃')

dog = dog()
dog.eat()