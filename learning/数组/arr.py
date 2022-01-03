from array import *

# arrayName = array(typecode, [Initializers])
# typecode是用于定义数组将保存的值类型的代码。
# 一些常用的typecodes使用如下:
# b表示大小为1字节的有符号整数   -128-127
# B表示大小为1字节的无符号整数
# c表示大小为1字节的字符
# i表示大小为2个字节的带符号整数
# I表示大小为2个字节的无符号整数
# f表示大小为4字节的浮点
# d表示大小为8个字节的浮点
arrayName = array('b', [1, 2, 3])
print(arrayName.typecode)
print(arrayName.index(1))
print(arrayName.itemsize)
print(arrayName.buffer_info())
print(arrayName.count(1))
arrayName.remove(1)
print(arrayName)
print(arrayName.pop(0))
print(arrayName)
arrayName.insert(1,10)
print(arrayName)
arrayName.append(20)
print(arrayName)
arrayName.extend(range(10))
print(arrayName)
lt = list(range(5))
arrayName.fromlist(lt)
print(arrayName)
arrayName.reverse()
print(arrayName)
