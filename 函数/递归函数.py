# 递归计算
def recursion_calculation(count):
    if count == 1:
        return 1
    else:
        return count * recursion_calculation(count - 1)

# recursion_calculation(5)
print('最终结果为：%d\n'%recursion_calculation(5))


# 获取路径下的文件，若是文件夹就继续向下递归
import os

def find_path_file(path):
    # 获取此路径下的文件/文件夹
    list_file = os.listdir(path)
    for file_item in list_file:
        complete_path = os.path.join(path, file_item)
        # 如果是文件夹
        if os.path.isdir(complete_path):
            print("文件夹名：" + complete_path)
            # 如果 return 的话初次函数调用的后续循环不会进行
            find_path_file(complete_path)
        else:
            # 打印文件全路径
            print('文件名：\t' + file_item)

# def main():
find_path_file('/Users/insta360/Desktop/工单')