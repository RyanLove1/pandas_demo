import pandas as pd

# 用户评分表
df_ratings = pd.read_csv(
    "D:/python基础课程/pandas/ant-learn-pandas/datas/movielens-1m/ratings.dat",
    sep="::",
    engine="python",
    names="UserID::MovieID::Rating::Timestamp".split("::")
)
print(df_ratings.head())

# 用户信息表
df_users = pd.read_csv(
    "D:/python基础课程/pandas/ant-learn-pandas/datas/movielens-1m/users.dat",
    sep="::",
    engine="python",
    names="UserID::Gender::Age::Occupation::Zip-code".split("::")
)
print(df_users.head())

# 电影详情表
df_movies = pd.read_csv(
    "D:/python基础课程/pandas/ant-learn-pandas/datas/movielens-1m/movies.dat",
    sep="::",
    engine="python",
    names="MovieID::Title::Genres".split("::")
)
print(df_movies.head())

# 评分表和用户表合并
df_ratings_users = pd.merge(
    df_ratings, df_users, left_on="UserID", right_on="UserID", how="inner"
)
print(df_ratings_users)

# 合并后的表与电影详情表合并
df_ratings_users_movies = pd.merge(
    df_ratings_users, df_movies, left_on="MovieID", right_on="MovieID", how="inner"
)
print(df_ratings_users_movies.head())

df_ratings_users_movies.to_excel("df_ratings_users_movies.xlsx", index=False)

# one-to-one 一对一关系的merge
left = pd.DataFrame({'sno': [11, 12, 13, 14],
                     'name': ['name_a', 'name_b', 'name_c', 'name_d']
                     })
print(left)

right = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'age': ['21', '22', '23', '24']
                      })
print(right)

# 一对一关系，结果中有4条
ret = pd.merge(left, right, on='sno')
print(ret)
'''
sno    name age
0   11  name_a  21
1   12  name_b  22
2   13  name_c  23
3   14  name_d  24
'''

# one-to-many 一对多关系的merge
# 注意：数据会被复制
right_two = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                          'grade': ['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']
                          })

# 数目以多的一边为准
ret2 = pd.merge(left, right_two, on='sno')
print(ret2)
'''
sno    name grade
0   11  name_a  语文88
1   11  name_a  数学90
2   11  name_a  英语75
3   12  name_b  语文66
4   12  name_b  数学55
5   13  name_c  英语29
'''

#  many-to-many 多对多关系的merge
left_two = pd.DataFrame({'sno': [11, 11, 12, 12, 12],
                         '爱好': ['篮球', '羽毛球', '乒乓球', '篮球', "足球"]
                         })
right_three = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                            'grade': ['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']
                            })
ret3 = pd.merge(left_two, right_three, on='sno')
print(ret3)

# 理解left join、right join、inner join、outer join的区别
# inner join，默认
# 左边和右边的key都有，才会出现在结果里
pd.merge(left, right, how='inner')

# left join
# 左边的都会出现在结果里，右边的如果无法匹配则为Null
pd.merge(left, right, how='left')

# right join
# 右边的都会出现在结果里，左边的如果无法匹配则为Null
pd.merge(left, right, how='right')

# outer join
# 左边、右边的都会出现在结果里，如果无法匹配则为Null
pd.merge(left, right, how='outer')

# 如果出现非Key的字段重名怎么办
# _left为左表同名字段后缀
pd.merge(left, right, on='key', suffixes=('_left', '_right'))