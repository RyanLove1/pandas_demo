import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
print(df)

'''
A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11'''

# 单列drop，就是删除某一列
# 代表的就是删除某列
res = df.drop("A", axis=1)
print(res)

'''
B   C   D
0  1   2   3
1  5   6   7
2  9  10  11'''

# 单行drop，就是删除某一行
res2 = df.drop(1, axis=0)
print(res2)

# 按axis=0/index执行mean聚合操作
res3 = df.mean(axis=0)
print(res3)
'''
A    4.0
B    5.0
C    6.0
D    7.0
'''
# 注意：指定了按哪个axis，就是这个axis要动起来(类似被for遍历)，其它的axis保持不动

# 按axis=1/columns执行mean聚合操作
# axis=1 or axis=columns
res4 = df.mean(axis=1)
print(res4)
'''
0    1.5
1    5.5
2    9.5
'''


def get_sum_value(x):
    return x["A"] + x["B"] + x["C"] + x["D"]


res5 = df["sum_value"] = df.apply(get_sum_value, axis=1)
print(res5)
'''
0     6
1    22
2    38
'''