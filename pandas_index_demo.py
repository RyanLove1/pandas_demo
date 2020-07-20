from timeit import timeit

import pandas as pd


df = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/ml-latest-small/ratings.csv", encoding="utf8",
                 engine="python")

print(df.head(5))

# 查看数量
print(df.count())

# 使用index查询数据
# drop==False，让索引列还保持在column, True代表删除userID这一列
df.set_index("userId", inplace=True, drop=False)
print(df.head())

# 使用colum的condition查询方法
res = df.loc[df["userId"] == 500].head()
print(res)

# 使用index进行查询
res2 = df.loc[500].head()
print(res2)

# 完全随机的顺序查询
# 将数据随机打散
from sklearn.utils import shuffle

df_shuffle = shuffle(df)
print(df_shuffle.head())

# 判断索引是否是递增的
res3 = df_shuffle.index.is_monotonic_increasing
print(res3)

# 判断索引是否是唯一的
res4 = df_shuffle.index.is_unique
print(res4)

# 计时，查询id==500数据性能
# 要在ipython下才可以使用。（所以说Jupyter Notebook当然是可以用的，pycharm里的python环境也是jupyter Notebook的）
# %timeit df_shuffle.loc[500]

# 使用index能自动对齐数据
s1 = pd.Series([1,2,3], index=list("abc"))
s2 = pd.Series([2,3,4], index=list("bcd"))
print(s1 + s2)
'''
a    NaN
b    4.0
c    6.0
d    NaN
'''

'''
使用index更多更强大的数据结构支持
很多强大的索引数据结构

CategoricalIndex，基于分类数据的Index，提升性能；
MultiIndex，多维索引，用于groupby多维聚合后结果等；
DatetimeIndex，时间类型索引，强大的日期和时间的方法支持；
'''