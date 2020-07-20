import pandas as pd

stocks = pd.read_excel('D:/python基础课程/pandas/ant-learn-pandas/datas/stocks/互联网公司股票.xlsx')

print(stocks.head())

print(stocks["公司"].unique())

# 公司股票代码到中文的映射，注意这里是小写
dict_company_names = {
    "bidu": "百度",
    "baba": "阿里巴巴",
    "iq": "爱奇艺",
    "jd": "京东"
}
# map用于Series值的转换
# 方法一：Series.map(dict)
stocks["公司中文1"] = stocks["公司"].str.lower().map(dict_company_names)
print(stocks.head())

# 方法2：Series.map(function)
stocks["公司中文2"] = stocks["公司"].map(lambda x: dict_company_names[x.lower()])
print(stocks.head())

# apply用于Series和DataFrame的转换
# Series.apply(function),function的参数是Series的每个值
stocks["公司中文3"] = stocks["公司"].apply(lambda x: dict_company_names[x.lower()])
print(stocks.head())

# DataFrame.apply(function),function的参数是对应轴的Series
stocks["公司中文4"] = stocks.apply(
    lambda x: dict_company_names[x["公司"].lower()],
    axis=1)

# applymap用于DataFrame所有值的转换
sub_df = stocks[['收盘', '开盘', '高', '低', '交易量']]

# 将这些数字取整数，应用于所有元素
sub_df.applymap(lambda x : int(x))

# 直接修改原df的这几列
stocks.loc[:, ['收盘', '开盘', '高', '低', '交易量']] = sub_df.applymap(lambda x : int(x))

print(stocks.head())