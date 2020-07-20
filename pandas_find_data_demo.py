import pandas as pd

df = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv", engine='python',
                 encoding='utf-8')
print(df.head())

# 设定索引日期，方便日期筛选
df.set_index('ymd', inplace=True)
print(df.index)

# 替换掉温度后缀℃
df.loc[:, 'bWendu'] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, 'yWendu'] = df["yWendu"].str.replace("℃", "").astype('int32')

# 查看每一列的类型
print(df.dtypes)

print(df.head())

# 使用单个label值查询数据
# 得到单个值（2018-01-03最高温度）
res = df.loc["2018-01-03", "bWendu"]
print(res)

# 得到一个Series（2018-01-03最高温度和最低温度）
ret = df.loc["2018-01-03", ["bWendu", "yWendu"]]
print(ret)

# 使用值列表批量查询
# 得到Series
s1 = df.loc[['2018-01-03', '2018-01-04', '2018-01-05'], 'bWendu']
print(s1)

# 得到DataFrame
s2 = df.loc[['2018-01-03', '2018-01-04', '2018-01-05'], ['bWendu', 'yWendu']]

# 使用数值区间进行范围查询
# 行index按区间
s3 = df.loc['2018-01-03':'2018-01-05', 'bWendu']
print(s3)

# 列index按区间
s4 = df.loc['2018-01-03', 'bWendu':'fengxiang']
print(s4)

# 行和列都按区间查询
s5 = df.loc['2018-01-03':'2018-01-05', 'bWendu':'fengxiang']
print(s5)

# 使用条件表达式查询
# 简单条件查询，最低温度低于-10度的列表
s6 = df.loc[df["yWendu"] < -10, :]
print(s6)

# 复杂条件查询，查一下我心中的完美天气
# 查询最高温度小于30度，并且最低温度大于15度，并且是晴天，并且天气为优的数据
s7 = df.loc[(df["bWendu"] <= 30) & (df["yWendu"] >= 15) & (df["tianqi"] == '晴') & (df["aqiLevel"] == 1), :]
print(s7)

# 调用函数查询
# 直接写lambda表达式
s8 = df.loc[lambda df: (df["bWendu"] <= 30) & (df["yWendu"] >= 15), :]
print(s8)


# 编写自己的函数，查询9月份，空气质量好的数据
def query_my_data(df):
    return df.index.str.startswith("2018-09") & (df["aqiLevel"] == 1)


s9 = df.loc[query_my_data, :]
print(s9)
