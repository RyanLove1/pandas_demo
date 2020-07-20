import pandas as pd

fpath = 'D:/python基础课程/pandas/ant-learn-pandas/datas/ml-latest-small/ratings.csv'
# 使用pd.read_csv读取数据
ratings = pd.read_csv(fpath, engine='python')
# 查看前几行数据
ratings.head()
print(ratings.head())
# 查看数据的形状，返回(行数、列数)
a = ratings.shape
print(a)
# 查看列名列表
b = ratings.columns
print(b)
# 查看索引列
c = ratings.index
print(c)
# 查看每列的数据类型
d = ratings.dtypes
print(d)


import pymysql
conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456',
        database='my_db',
        charset='utf8'
    )

mysql_page = pd.read_sql("select * from student", con=conn)

print(mysql_page)