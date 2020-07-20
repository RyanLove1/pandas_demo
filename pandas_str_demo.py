import pandas as pd

df = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv", encoding="utf8",
                 engine="python")

print(df.head(5))

# 字符串替换函数
res = df["bWendu"].str.replace("℃", "")
print(res)

# 判断是不是数字
df["bWendu"].str.isnumeric()

# 使用str的startswith、contains等得到bool的Series可以做条件查询
condition = df["ymd"].str.startswith("2018-03")
print(condition)

print(df[condition].head())

'''需要多次str处理的链式操作
怎样提取201803这样的数字月份？
1、先将日期2018-03-31替换成20180331的形式
2、提取月份字符串201803'''

# 直接将"-"替换成""
res3 = df["ymd"].str.replace("-", "")
print(res3)

# 每次调用函数，都返回一个新Series，所以必须再.str
res4 = df["ymd"].str.replace("-", "").str.slice(0, 6)
print(res4)

# slice就是切片语法，可以直接用
res5 = df["ymd"].str.replace("-", "").str[0:6]


# 使用正则表达式的处理
def get_nianyueri(x):
    year, month, day = x["ymd"].split("-")
    return f"{year}年{month}月{day}日"


res6 = df["中文日期"] = df.apply(get_nianyueri, axis=1)
print(res6)

# 将日月年去除
# 方法一
res7 = df["中文日期"].str.replace("年", "").str.replace("月", "").str.replace("日", "")
print(res7)

# Series.str默认就开启了正则表达式模式
# 方法2：正则表达式替换
res8 = df["中文日期"].str.replace("[年月日]", "")
print(res8)