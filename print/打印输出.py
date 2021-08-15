'''
打印输出
'''

# format 格式化输出
rs = 123
print('rs={}'.format(rs))

print('rs={0}'.format(rs))

sum_func = lambda x,y,z,c: x*y*z*c
rs1 = sum_func(4,5,6,7)
print('rs1 = %d'%rs1)
print('rs1 = %d，study %s'%(rs1, 'Python'))
