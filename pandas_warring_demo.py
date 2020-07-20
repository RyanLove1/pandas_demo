import pandas as pd

df = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv", encoding="utf8", engine="python")

print(df.head(5))

df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype("int32")
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype("int32")

print(df.head())

# 只选出3月份的数据用于分析
condition = df["ymd"].str.startswith("2018-03")

# 设置温差
df[condition]["wen_cha"] = df["bWendu"]-df["yWendu"]

# 查看是否修改成功
print(df[condition].head())

# 以上会报SettingWithCopyWarning

# 解决方法1
# 将get+set的两步操作，改成set的一步操作
df.loc[condition, "wen_cha"] = df["bWendu"]-df["yWendu"]
print(df[condition].head())

# 解决方法2
# 如果需要预筛选数据做后续的处理分析，使用copy复制dataframe
df_month3 = df[condition].copy()
print(df_month3.head())

df_month3["wen_cha"] = df["bWendu"]-df["yWendu"]
print(df_month3.head())

'''总之，pandas不允许先筛选子dataframe，再进行修改写入
要么使用.loc实现一个步骤直接修改源dataframe
要么先复制一个子dataframe再一个步骤执行修改'''