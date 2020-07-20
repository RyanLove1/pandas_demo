import pandas as pd
import numpy as np

s1 = pd.Series([1, "a", 5.3, 7])
# 左侧为索引，右侧为数据
print(s1)

# 获取索引
print(s1.index)

# 获取数据
print(s1.values)

# 创建一个具有标签索引的Series
s2 = pd.Series([1, 'a', 5.2, 7], index=['d', 'b', 'a', 'c'])

# 使用python字典创建Series
sdata = {'Ohio': 35000, 'Texas': 72000, 'Oregon': 16000, 'Utah': 5000}
s3 = pd.Series(sdata)
print(s3)

# 根据索引标签查询数据
print(s2['a'])

# 获取多个值
print(s2[["a", "b"]])

# 根据多个字典序列创建dataframe
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}
df = pd.DataFrame(data)
print(df)

# 查看每一列得类型
print(df.dtypes)

# 查看列名
print(df.columns)

# 查看索引
print(df.index)

'''
从DataFrame中查询出Series
如果只查询一行、一列，返回的是pd.Series
如果查询多行、多列，返回的是pd.DataFrame
'''

print(df["year"])

# 查询多列，结果是一个pd.DataFrame
print(df[["year", "pop"]])

# 查询一行，结果是pd.Series
print(df.loc[1])  # 超出行数会报错

# 查询多行，结果是pd.DataFrame
print(df.loc[1:3])