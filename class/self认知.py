'''
特点：
self只有在类中定义实例方法的时候才有意义，在调用时候不必传入相应的参数，而是由解释器自动去解析、指向
self的名字是可以更改的，只是默认约定如此
self指的是类实例对象本身，相当于Java的this指向当前对象
'''
class People:

    name = 'hello world'

    def get_self(self):
        print('name is %s, address is %s'%('getSelf', self))
        return self

peo = People()
print(peo.get_self())
print(peo)
# True
print(id(peo) == id(peo.get_self()))

