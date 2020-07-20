import pandas as pd

import warnings

# 通过警告过滤器进行控制是否发出警告消息
warnings.filterwarnings('ignore')

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],
                    'E': ['E0', 'E1', 'E2', 'E3']
                    })

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7'],
                    'F': ['F4', 'F5', 'F6', 'F7']
                    })

# 默认的concat，参数为axis=0、join=outer、ignore_index=False
res = pd.concat([df1, df2])
print(res)
'''
A   B   C   D    E    F
0  A0  B0  C0  D0   E0  NaN
1  A1  B1  C1  D1   E1  NaN
2  A2  B2  C2  D2   E2  NaN
3  A3  B3  C3  D3   E3  NaN
0  A4  B4  C4  D4  NaN   F4
1  A5  B5  C5  D5  NaN   F5
2  A6  B6  C6  D6  NaN   F6
3  A7  B7  C7  D7  NaN   F7
'''
# 使用ignore_index=True可以忽略原来的索引
pd.concat([df1, df2], ignore_index=True)

# 使用join=inner过滤掉不匹配的列
res2 = pd.concat([df1, df2], ignore_index=True, join="inner")
print(res2)
'''
A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
'''

# 添加一列Series
s1 = pd.Series(list(range(4)), name="F")
res3 = pd.concat([df1, s1], axis=1)
print(res3)
'''
A   B   C   D   E  F
0  A0  B0  C0  D0  E0  0
1  A1  B1  C1  D1  E1  1
2  A2  B2  C2  D2  E2  2
3  A3  B3  C3  D3  E3  3
'''

# 添加多列Series
s2 = df1.apply(lambda x: x["A"] + "_GG", axis=1)
print(s2)
'''
0    A0_GG
1    A1_GG
2    A2_GG
3    A3_GG
'''
# 指定s2列名
s2.name = "G"
res4 = pd.concat([df1, s1, s2], axis=1)
print(res4)
'''
A   B   C   D   E  F      G
0  A0  B0  C0  D0  E0  0  A0_GG
1  A1  B1  C1  D1  E1  1  A1_GG
2  A2  B2  C2  D2  E2  2  A2_GG
3  A3  B3  C3  D3  E3  3  A3_GG
'''

# 列表可以只有Series
res5 = pd.concat([s1, s2], axis=1)
print(res5)
'''
F      G
0  0  A0_GG
1  1  A1_GG
2  2  A2_GG
3  3  A3_GG
'''

# 列表是可以混合顺序的
pd.concat([s1, df1, s2], axis=1)

# 使用DataFrame.append按行合并数据
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))

# 给1个dataframe添加另一个dataframe
# 忽略原来的索引ignore_index=True
res6 = df1.append(df2, ignore_index=True)
print(res6)
'''
A  B
0  1  2
1  3  4
2  5  6
3  7  8
'''

# 可以一行一行的给DataFrame添加数据
# 一个空的df
df = pd.DataFrame(columns=['A'])

# 低性能版
for i in range(5):
    # 注意这里每次都在复制
    df = df.append({'A': i}, ignore_index=True)

# 性能较好版
# 第一个入参是一个列表，避免了多次复制
pd.concat(
    [pd.DataFrame([i], columns=['A']) for i in range(5)],
    ignore_index=True
)
