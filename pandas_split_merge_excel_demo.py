import pandas as pd
import os

df_source = pd.read_excel(
    "D:/python基础课程/pandas/ant-learn-pandas/course_datas/c15_excel_split_merge/crazyant_blog_articles_source.xlsx")

print(df_source.head(5))

if not os.path.exists("splits_dir"):
    os.mkdir("splits_dir")

res = df_source.index
print(res)

# 获取行数
total_row_count = df_source.shape[0]
print(total_row_count)

# 使用df.iloc方法，将一个大的dataframe，拆分成多个小dataframe
# 这个大excel，会拆分给这几个人
user_names = ["xiao_shuai", "xiao_wang", "xiao_ming", "xiao_lei", "xiao_bo", "xiao_hong"]
# 每个人的任务数目
split_size = total_row_count // len(user_names)
if total_row_count % len(user_names) != 0:
    split_size += 1

# 拆分成多个dataframe
df_subs = list()
for idx, user_names in enumerate(user_names):
    # iloc开始索引
    begin = idx*split_size
    # 结束索引
    end = begin+split_size
    # 拆分
    df_sub = df_source.iloc[begin:end]
    df_subs.append((idx, user_names, df_sub))

# 将每个dataframe存入excel
for idx, user_names, df_sub in df_subs:
    file_name = f"splits_dir/crazyant_blog_articles_{idx}_{user_names}.xlsx"
    df_sub.to_excel(file_name, index=False)


# 使用pd.concat进行df批量合并
# 遍历文件夹，得到要合并的Excel名称列表
excel_names = list()
for excel_name in os.listdir("splits_dir"):
    excel_names.append(excel_name)

# 分别读取到dataframe
df_list = list()
for excel_name in excel_names:
    excel_path = f"splits_dir/{excel_name}"
    df_split = pd.read_excel(excel_path)
    # 得到username
    username = excel_name.replace("crazyant_blog_articles_", "").replace(".xlsx", "")[2:]
    # 给每一个df添加1列
    df_split["username"] = username

    df_list.append(df_split)

# 使用pd.concat进行合并
df_merged = pd.concat(df_list)

print(df_merged.head(5))

# 将合并后的dataframe输出到excel
df_merged.to_excel(f"splits_dir/merged_data.xlsx", index=False)