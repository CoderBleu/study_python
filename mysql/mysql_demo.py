from pymysql import *

connection = connect(host='127.0.0.1', user='root', password='root',
                     database='blue', charset='utf-8', autocommit=False)
# autocommit=True, 如果插入数据,是否自动提交? 和conn.commit()功能一致。
# 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
try:
    cursor = connection.cursor()
    insert_sql = '''
        INSERT INTO tb_student(username, grade) values ('Lauy', '二年级')
    '''
    cursor.execute(insert_sql)  # 插入
    connection.commit()

    cursor.execute('SELECT * FROM tb_student')  # 查询
    # 移动游标指针到最后,获取所有的查询结果
    result = cursor.fetchall()
    # 返回执行sql语句影响的行数
    print(cursor.rowcount)
    # 关闭游标
    cursor.close()
    # 关闭连接
    connection.close()
    # 输出查询结果
    for student in result:
        print(student)
except Exception as e:
    print(e)
