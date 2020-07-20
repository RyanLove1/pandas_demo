import pandas as pd

fpath = "D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath, engine="python", encoding="utf8")
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())

# 将日期列转换成pandas的日期
df.set_index(pd.to_datetime(df["ymd"]), inplace=True)
print(df.head())

# DatetimeIndex是Timestamp的列表形式
print(df.index[0])

# DatetimeIndex查询
# 筛选固定的某一天
res = df.loc['2018-01-05']
print(res)
'''
ymd          2018-01-05
bWendu                3
yWendu               -6
tianqi             多云~晴
fengxiang           西北风
fengli             1-2级
aqi                  50
aqiInfo               优
aqiLevel              1
'''

# 日期区间
res2 = df.loc['2018-01-05':'2018-01-10']
print(res2)

# 按月份前缀筛选
res3 = df.loc['2018-03']

# 按月份前缀筛选
res4 = df.loc["2018-07":"2018-09"].index

# 按年份前缀筛选
res5 = df.loc["2018"].head()

# 获取周、月、季度
# 周数字列表
res6 = df.index.week

# 月数字列表
res7 = df.index.month

# 季度数字列表
res8 = df.index.quarter

# 统计每周、每月、每个季度的最高温度
res9 = df.groupby(df.index.week)["bWendu"].max().head()
print(res9)
'''
ymd
1    3
2    6
3    7
4   -1
5    4
'''
# 统计每个月的数据
res10 = df.groupby(df.index.month)["bWendu"].max()

# 统计每个季度的数据
res11 = df.groupby(df.index.quarter)["bWendu"].max

# 缺失时间索引的填充
df = pd.DataFrame({
    "pdate": ["2019-12-01", "2019-12-02", "2019-12-04", "2019-12-05"],
    "pv": [100, 200, 400, 500],
    "uv": [10, 20, 40, 50],
})
print(df)

# 方法1：使用pandas.reindex方法
# 设置索引
df_date = df.set_index("pdate")
# 将df的索引设置为日期索引
df_date = df_date.set_index(pd.to_datetime(df_date.index))

print(df_date)

# 使用pandas.reindex填充缺失的索引
# 生成完整的日期序列
pdates = pd.date_range(start="2019-12-01", end="2019-12-05")
print(pdates)
'''
DatetimeIndex(['2019-12-01', '2019-12-02', '2019-12-03', '2019-12-04',
               '2019-12-05'],
              dtype='datetime64[ns]', freq='D')
'''

# 填充缺失索引，并填充默认值
df_date_new = df_date.reindex(pdates, fill_value=0)
print(df_date_new)

# 方法2：使用pandas.resample方法
# 先将索引变成日期索引
df_new2 = df.set_index(pd.to_datetime(df["pdate"])).drop("pdate", axis=1)
# 使用dataframe的resample的方法按照天重采样
# 由于采样会让区间变成一个值，所以需要指定mean等采样值的设定方法
df_new2 = df_new2.resample("D").mean().fillna(0)
print(df_new2)
'''
              pv    uv
pdate                  
2019-12-01  100.0  10.0
2019-12-02  200.0  20.0
2019-12-03    0.0   0.0
2019-12-04  400.0  40.0
2019-12-05  500.0  50.0
'''

# resample的使用方式（2D每隔两天，pv/uv是两天得平均值）
res12 = df_new2.resample("2D").mean()
print(res12)
'''
               pv    uv
pdate                  
2019-12-01  150.0  15.0
2019-12-03  200.0  20.0
2019-12-05  500.0  50.0
'''