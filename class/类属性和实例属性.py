import random

'''

1、可以被类对象和实例对象共同访问使用
2、类属性属于类所有，所有对象共享一份内存地址
3、实例属性只能由实例对象访问使用
4、修改类属性值需要用类 Class.类属性=值，如果是 obj.类属性值，结果只是新增实例属性
'''
class Person:

    id = random.randrange(1, 100, 10)

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self, weight):
        # 实例属性
        self.username = 'hello world'
        self.age = 20
        # 动态赋值
        self.weight = weight

    # 实例方法
    def study(self):
        print("study Python!")


'''
创建一个对象
每创建一个对象都要添加属性，显然很费事，所以我们可以采用上述的 __init__方法定义实例属性，在类实例化时就被执行
'''
obj = Person(110)
# 添加实例属性
obj.gender = 'Male'
print('obj.username:%s'%obj.username)
print('obj中：类属性id为%d，username is %s, __weight is %d'%(obj.id, obj.username, obj.weight))
# 此处本是想修改类属性值，其实只是增加了一个 实例属性为id的
obj.id = 'i change id value'
# obj中：类属性id为i change id value，username is hello world, __weight is 110
print('obj中：类属性id为%s，username is %s, __weight is %d'%(obj.id, obj.username, obj.weight))

obj = Person(120)
print('obj中：类属性id为%d，username is %s, __weight is %d'%(obj.id, obj.username, obj.weight))

print('类属性id为%d'%Person.id)
