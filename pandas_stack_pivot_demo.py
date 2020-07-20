import pandas as pd
import numpy as np

df = pd.read_csv(
    "D:/python基础课程/pandas/ant-learn-pandas/datas/movielens-1m/ratings.dat",
    header=None,
    names="UserID::MovieID::Rating::Timestamp".split("::"),
    sep="::",
    engine="python"
)

print(df.head())

# 将时间戳转换成时间格式
df["pdate"] = pd.to_datetime(df["Timestamp"], unit='s')
print(df.head())
'''
   UserID  MovieID  Rating  Timestamp               pdate
0       1     1193       5  978300760 2000-12-31 22:12:40
1       1      661       3  978302109 2000-12-31 22:35:09
2       1      914       3  978301968 2000-12-31 22:32:48
3       1     3408       4  978300275 2000-12-31 22:04:35
4       1     2355       5  978824291 2001-01-06 23:38:11
'''

# 实现数据统计(按照月份和评分分组)
df_group = df.groupby([df["pdate"].dt.month, "Rating"])["UserID"]
df_test = df_group.agg(np.size)
print(df_test.head())

