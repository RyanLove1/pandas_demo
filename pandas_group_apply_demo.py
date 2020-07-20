import pandas as pd

# 用户评分表
df_ratings = pd.read_csv(
    "D:/python基础课程/pandas/ant-learn-pandas/datas/movielens-1m/ratings.dat",
    sep="::",
    engine="python",
    names="UserID::MovieID::Rating::Timestamp".split("::")
)
print(df_ratings.head())


# 用户对电影评分的归一化
# 实现按照用户ID分组，然后对其中一列归一化
def ratings_norm(df):
    """
    @param df：每个用户分组的dataframe
    """
    min_value = df["Rating"].min()
    max_value = df["Rating"].max()
    df["Rating_norm"] = df["Rating"].apply(
        lambda x: (x - min_value) / (max_value - min_value))
    return df


ratings = df_ratings.groupby("UserID").apply(ratings_norm)
res = ratings[ratings["UserID"] == 1].head()
print(res)

# 获取2018年每个月温度最高的2天数据
df = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv", engine='python',
                 encoding='utf-8')
print(df.head())
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
# 新增一列为月份
df['month'] = df['ymd'].str[:7]


def getWenduTopN(df, topn):
    """
    这里的df，是每个月份分组group的df
    """
    # 根据最高温度排序，取日期和温度，默认是升序，所以取最后两个
    return df.sort_values(by="bWendu")[["ymd", "bWendu"]][-topn:]


# 根据月份分组
res2 = df.groupby("month").apply(getWenduTopN, topn=2).head()
print(res2)
