import pandas as pd

df = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv", encoding="utf8", engine="python")

print(df.head(5))

df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype("int32")
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype("int32")

print(df.head())

# 一下子提取所有数字列统计结果
res1 = df.describe()
print(res1)
'''        bWendu      yWendu         aqi    aqiLevel
count  365.000000  365.000000  365.000000  365.000000
mean    18.665753    8.358904   82.183562    2.090411
std     11.858046   11.755053   51.936159    1.029798
min     -5.000000  -12.000000   21.000000    1.000000
25%      8.000000   -3.000000   46.000000    1.000000
50%     21.000000    8.000000   69.000000    2.000000
75%     29.000000   19.000000  104.000000    3.000000
max     38.000000   27.000000  387.000000    6.000000
'''
# 查看单个Series的数据
res2 = df["bWendu"].mean()  # 平均值
print(res2)

df["bWendu"].max()
df["bWendu"].min()

# 唯一性去重
res3 = df["fengxiang"].unique()
print(res3)
'''['东北风' '北风' '西北风' '西南风' '南风' '东南风' '东风' '西风']'''

# 按值计算
res4 = df["fengxiang"].value_counts()
print(res4)
'''南风     92
西南风    64
北风     54
西北风    51
东南风    46
东北风    38
东风     14
西风      6'''

# 协方差矩阵：
res5 = df.cov()
print(res5)

# 相关系数矩阵
res6 = df.corr()
print(res6)

# 单独查看空气质量和最高温度的相关系数
res7 = df["aqi"].corr(df["bWendu"])
print(res7)

# 空气质量和温差的相关系数
res8 = df["aqi"].corr(df["bWendu"]-df["yWendu"])
print(res8)

