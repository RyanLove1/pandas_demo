import pandas as pd
from sqlalchemy import create_engine

engin = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/rabbit_test?charset=utf8")

sql = '''select * from student'''

# 查询结果
df = pd.read_sql_query(sql, engin)
print(df)

# 新建pandas中DataFrame
data = {
    'id': [17, 18, 19],
    "name": ["yanxu", "shuaishuai", "xiaolong"],
    "age": [20, 22, 23],
    "class_id": [1, 2, 3]
}
df = pd.DataFrame(data)

# 将新建的DataFrame储存为mysql中的数据表，index=True储存index列
# if_exists:
# 1.fail:如果表存在，啥也不做
# 2.replace:如果表存在，删了表，再建立一个新表，把数据插入
# 3.append:如果表存在，把数据插入，如果表不存在创建一个表！！
df.to_sql("student", engin, index=False, if_exists="append")
# 或者这种形式
# pd.io.sql.to_sql(df, "student", con=engin, index=False, if_exists="append")
print(df)
