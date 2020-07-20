import pandas as pd

# 学生成绩表
df_grade = pd.read_excel("D:/python基础课程/pandas/ant-learn-pandas/course_datas/c23_excel_vlookup/学生成绩表.xlsx")
print(df_grade.head())

# 学生信息表
df_sinfo = pd.read_excel("D:/python基础课程/pandas/ant-learn-pandas/course_datas/c23_excel_vlookup/学生信息表.xlsx")
print(df_sinfo.head())

# 实现两个表的关联
# 之筛选学生信息表的少量的列
df_sinfo = df_sinfo[["学号", "姓名", "性别"]]
print(df_sinfo.head())

# 合并两个表
df_merge = pd.merge(left=df_grade, right=df_sinfo, left_on="学号", right_on="学号")
print(df_merge)

# 调整列的顺序
# 将columns变成python的列表形式
new_columns = df_merge.columns.tolist()
print(new_columns)
'''
['班级', '学号', '语文成绩', '数学成绩', '英语成绩', '姓名', '性别']
'''

# 按逆序insert，会将"姓名"，"性别"放到"学号"的后面
for name in ["姓名", "性别"][::-1]:
    new_columns.remove(name)
    new_columns.insert(new_columns.index("学号")+1, name)

print(new_columns)
'''
['班级', '学号', '姓名', '性别', '语文成绩', '数学成绩', '英语成绩']
'''

df_merge = df_merge.reindex(columns=new_columns)
df_merge.head()

# 输出最终的Excel文件
df_merge.to_excel("合并后的数据表.xlsx", index=False)




