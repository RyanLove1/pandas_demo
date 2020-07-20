import pandas as pd

# 读取excel的时候，忽略前几个空行
studf = pd.read_excel("D:/python基础课程/pandas/ant-learn-pandas/datas/student_excel/student_excel.xlsx",
                      skiprows=2)  # 忽略前两行

print(studf.head())

# 检测空值
print(studf.isnull())
''' Unnamed: 0     姓名     科目     分数
0         True  False  False  False
1         True   True  False  False
2         True   True  False  False
3         True   True   True   True
4         True  False  False  False
5         True   True  False   True
6         True   True  False  False
7         True   True   True   True
8         True  False  False  False
9         True   True  False  False
10        True   True  False  False'''

# 检测分数这一列空值
print(studf["分数"].isnull())

# 检测不为空
print(studf["分数"].notnull())

# 筛选没有空分数的所有行
res = studf.loc[studf["分数"].notnull(), :]
print(res)

# 删除掉全是空值的列
# True则修改当前df，否则返回新的df
studf.dropna(axis="columns", how='all', inplace=True)
print(studf)

# 删除掉全是空值的行
studf.dropna(axis="index", how='all', inplace=True)
print(studf)

# 将分数列为空的填充为0分
res3 = studf.fillna({"分数": 0})
print(res3)

# 等同于
studf.loc[:, '分数'] = studf['分数'].fillna(0)
print(studf)

# 将姓名的缺失值填充
# 使用前面的有效值填充，用ffill：forward fill
studf.loc[:, '姓名'] = studf['姓名'].fillna(method="ffill")
print(studf)

# 将清洗好的excel保存
# index=False表示去除索引列
studf.to_excel("student_excel_clean.xlsx", index=False)