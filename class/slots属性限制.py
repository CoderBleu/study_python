'''
作用：
1、限制要添加的实例属性
2、节省内存空间
'''

class Student:
    __slots__ = ('name', 'age', '__dict__')

    def __str__(self):
        return '{}...{}'.format(self.name, self.age)

stu = Student()

stu.name = 'hello world'
stu.age = 18
print(stu)
# 若未开启slots，则所有可以用的属性都将存储到这，缺点占用过多的内存空间 {'name': 'hello world', 'age': 18}
# 若已开启slots，则打印为空 {}
print(stu.__dict__)
# 报错：AttributeError: 'Student' object has no attribute 'weight'
# print(stu.weight)


'''
在继承关系中的使用：__slots
子类未声明 __slots__时，那么是不会继承父类的__slots，此时子类是可以随意的属性添加与赋值
子类声明 __slots__时，继承父类的 __slots__，也就是子类__slots__的范围是 其自身
'''
class MaleStudent:
    __slots__ = ('name', 'height', 'age')
    pass

m = MaleStudent()
m.name = 'study Python'
m.age = 20
m.height = 1.8
print(m.name, m.age)