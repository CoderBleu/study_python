'''
类：
'''

class Person:
    # 类属性

    # 初始化类的属性，在实例化时被执行，可以理解为构造器
    def __init__(self, weight):
        # 实例属性
        self.username = 'hello world'
        print('username address is %s'%id(self.username))
        self.age = 20
        # 动态赋值
        self.weight = weight

    # def __init__(self, __weight, hobby):
    #     # 实例属性
    #     self.username = 'hello world'
    #     self.age = 20
    #     # 动态赋值
    #     self.__weight = __weight
    #     self.hobby = hobby

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
obj.height = 1.8
print(obj.username, obj.age, obj.gender, obj.height, obj.weight)

obj1 = Person(120)
# 添加实例属性
obj1.gender = 'Fmale'
obj1.height = 1.8
print(obj1.username, obj1.age, obj1.gender, obj1.height, obj1.weight)
