import pandas as pd

df = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv", engine='python',
                 encoding='utf-8')
print(df.head())

# 直接赋值的方法
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

print(df.head())

# 计算温差
# 注意，df["bWendu"]其实是一个Series，后面的减法返回的是Series
df.loc[:, "wencha"] = df["bWendu"] - df["yWendu"]
print(df.head())


# df.apply方法
def get_wendu_type(x):
    if x["bWendu"] > 33:
        return '高温'
    if x["yWendu"] < -10:
        return '低温'
    return '常温'


# 注意需要设置axis==1，这是series的index是columns
df.loc[:, "wendu_type"] = df.apply(get_wendu_type, axis=1)
# 查看温度类型的计数
s1 = df["wendu_type"].value_counts()
print(s1)

# df.assign方法
# 可以同时添加多个新的列
df.assign(
    # 新增的列名
    yWendu_huashi=lambda x: x["yWendu"] * 9 / 5 + 32,
    # 摄氏度转华氏度
    bWendu_huashi=lambda x: x["bWendu"] * 9 / 5 + 32
)

# 按条件选择分组分别赋值
# 先创建空列（这是第一种创建新列的方法）
df['wencha_type'] = ''

df.loc[df["bWendu"] - df["yWendu"] > 10, "wencha_type"] = "温差大"

df.loc[df["bWendu"] - df["yWendu"] <= 10, "wencha_type"] = "温差正常"

s2 = df["wencha_type"].value_counts()
print(s2)
