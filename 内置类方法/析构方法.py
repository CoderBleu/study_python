class Animal:
    def __init__(self, name):
        self.name = name
        print('这是构造初始化方法')

    '''
    析构方法：
    主要的应用就是来操作对象的释放，一旦释放完毕，对象便不能再使用
    当在某个作用域下面，没有被使用[引用]的情况下，解析器会自动的调用此函数，来释放此对象所占的内存空间
    '''
    def __del__(self):
        print('%s 这个对象被彻底清理了，内存空间也释放了'%self.name)

dog = Animal('哈士奇')
print(dog.name)
# 手动的去清理删除对象 [name 'dog' is not defined]
# del dog
# print(dog) # 对象已被清理，会报错
input('程序等待中，请输入......')

'''
输出示例：

这是构造初始化方法
哈士奇
程序等待中，请输入......1
哈士奇 这个对象被彻底清理了，内存空间也释放了
'''