'''
匿名函数，lambada表达式
'''

result = lambda a, b, c: a * b * c
print(result(12, 34, 2))

# 类似于三元表达式
age = 15
print('每天学习' if age > 18 else '偶尔学习')

funcTest = lambda x, y: x if x > y else y
print(funcTest(2, 12))

# 直接调用函数
rs = (lambda x, y: x if x > y else y)(16, 12)
print(rs)

# ** 幂运算
rs1 = lambda x: (x ** 2) + 890
print(rs1(10))
