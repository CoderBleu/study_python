'''
多继承
'''

class D:
    def eat(self):
        print('爸爸叫吃饭了')

class C(D):
    def eat(self):
        print('C儿子在吃饭')

    def play(self):
        print('C儿子吃完饭，还能快乐玩耍')

class B(D):
    def eat(self):
        print('B儿子在吃饭')

# 多继承,继承的顺序为 A-B-C-D
class A(B, C):
    pass

'''
广度优先遍历：
1、在执行eat方法时，会先找本对象a中是否包含，如果没有就向上查找B，如果B中有eat方法就返回。如果没有，就再去找父亲C，找到返回。
2、同理向上查找，直至超类object。没有就报错了【'A' object has no attribute 'eat1'】
'''
a = A()
# B儿子在吃饭
a.eat()
# C儿子吃完饭，还能快乐玩耍
a.play()
