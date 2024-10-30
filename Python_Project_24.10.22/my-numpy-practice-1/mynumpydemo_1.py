import numpy as np

"""
A = np.arange(32).reshape(4, 1, 8)
B = np.arange(48).reshape(1, 6, 8)

print(A)
print(B)
"""

"""
square = np.array([
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1]
    ])
for i in range(4):
    assert square[:, i].sum() == 34 #numpy数组在轴之间使用逗号，分别对0，1，2，3列（for）的0，1，2，3行相加（:）
    assert square[i, :].sum() == 34 # : 表示遍历全部或剩余

assert square[:2, :2].sum() == 34 # 左上的象限
assert square[:2, 2:].sum() == 34 # 右上象限
assert square[:2, 2:].sum() == 34
assert square[2:, 2:].sum() == 34
"""

"""
numbers = np.linspace(5, 50, 24, dtype=int).reshape(4, -1) # 返回5到50范围内均匀分布的24个数字
mask = numbers % 4 == 0 # 创建掩码，判断是否为4的倍数
numbers[mask]# 用掩码对数组numbers进行索引
by_four = numbers[numbers % 4 ==0]# 传统方法
# 这两句都是返回bool值为True的元素
"""

"""
#转置数组
a = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])
b = a.T
c = a.transpose() #这两句都是行列转置
print(f'b={b}')
"""

"""
#排序
data = np.array([
    [7, 1, 4],
    [8, 6, 5],
    [1, 2, 3]
])
b = np.sort(data) # 省略axis参数会自动选择最内层的维度，即本例中的行进行排序
print(f'b = {b}')
c = np.sort(data, axis=None)# 全局排序
print(f'c = {c}')
d = np.sort(data, axis=0)# 对0轴即列轴排序
print(f'd = {d}')
"""

"""
# 连接
a = np.array([
    [4, 8],
    [6, 1]
])
b = np.array([
    [3, 5],
    [7, 2]
])
c = np.hstack((a, b))# 连接行，轴1
print(c)
d = np.vstack((b, a))# 连接列，轴0
e = np.concatenate((a, b))# 更通用的连接，可指定轴，默认为0轴，即纵向列轴
f = np.concatenate((a, b), axis=None)# 展开
"""

"""
#数值类型
a = np.array([1, 3, 5.5, 7.7, 9.2], dtype=np.single)#平台定义的单精度浮点数：通常为符号位，8位指数，23位尾数
b = np.array([1, 3, 5.5, 7.7, 9.2], dtype=np.uint8)#整数，范围从0-255

#字符串类型
names = np.array(['bob', 'amy', 'han'], dtype=str)# three 4-byte Unicode characters
names[2] = 'jamima'#将会阶段数值，使其变为U3的大小
print(names, names.itemsize)
"""

"""
#结构化数组
data = np.array([
    ("joe", 32, 6),
    ("mary", 15, 20),
    ("felipe", 80, 100),
    ("beyonce", 38, 9001)
], dtype=[("name", str, 10), ("age", int), ("power", int)])#对于dtype提供的是一个元组列表，name是10字符的Unicode字段
a = data[0]
b = data["name"]
c = data[data["power"] > 9000]["name"]#基于字段的掩码过滤和基于字段的选择的超强大组合
d = np.sort(data[data["age"] > 20], order="power")["name"]#掩码，还有基于order by 的排序
print(d)
"""












