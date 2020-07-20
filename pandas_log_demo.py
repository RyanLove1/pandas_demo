import pandas as pd
import numpy as np
import os

# 让输出不会被截断
pd.set_option('display.max_colwidth', -1)

from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Line

# 读取整个目录，将所有的文件合并到一个dataframe
data_dir = "./crazyant/blog_access_log/"

df_list = []

# error_bad_lines=False表示遇到错误行继续
for fname in os.listdir(f"{data_dir}"):
    df_list.append(pd.read_csv(f"{data_dir}/{fname}", sep=" ", header=None, error_bad_lines=False))
# 多个文件合并一起读取
df = pd.concat(df_list)
print(df.head())

# 复制的原因是后期对df修改的时候不会报错
df = df[[0, 3, 6, 9]].copy()

# 设置列名
df.columns = ["ip", "stime", "status", "client"]
print(df.head())

# 统计spider的比例(新增一列，先将client一列变小写，然后判断是否包含spider，返回的是True或False)
df["is_spider"] = df["client"].str.lower().str.contains("spider")
print(df.head())

# 查看这一列的次数
df_spider = df["is_spider"].value_counts()
print(df_spider)
'''
False    46641
True     3637 
'''

# 画柱状图
# 要求x轴都是字符串
bar = (
    Bar()
        .add_xaxis([str(x) for x in df_spider.index])
        .add_yaxis("是否Spider", df_spider.values.tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title="爬虫访问量占比"))
)
bar.render(path="柱状图.html")

# 访问状态码的数量对比
# 分组后，看每个状态码的数量
df_status = df.groupby("status").size()
print(df_status)
'''
status
200    41924
201    3432 
206    70   
301    2364 
302    23   
304    19   
400    20   
403    92   
404    1474 
405    12   
444    846  
500    1    
504    1  
'''

# 将以上数据变成列表套元组
res2 = list(zip(df_status.index, df_status))
print(res2)
'''
[(200, 41924), (201, 3432), (206, 70), (301, 2364), (302, 23), (304, 19), (400, 20)]
'''

# 画饼形图
pie = (
    Pie()
        .add("状态码比例", res2)
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)
# b代表标签，c代表数量
pie.render(path="状态码饼形图.html")

# 实现按小时、按天粒度的流量统计
# 时间格式是[02/Dec/2019:22:40:27
df["stime"] = pd.to_datetime(df["stime"].str[1:], format="%d/%b/%Y:%H:%M:%S")

# 设置时间为索引
df.set_index("stime", inplace=True)
# 升序
df.sort_index(inplace=True)

# 按小时统计
# df_pvuv = df.resample("H")["ip"].agg(pv=np.size, uv=pd.Series.nunique)

# 按每6个小时统计
# df_pvuv = df.resample("6H")["ip"].agg(pv=np.size, uv=pd.Series.nunique)

# 按天统计
df_pvuv = df.resample("D")["ip"].agg({"pv": np.size, "uv": pd.Series.nunique})

df_pvuv.head()

# 画折线图
line = (
    Line()
        .add_xaxis(df_pvuv.index.tolist())
        .add_yaxis("PV", df_pvuv["pv"].tolist())
        .add_yaxis("UV", df_pvuv["uv"].tolist())
        .set_global_opts(
        title_opts=opts.TitleOpts(title="PVUV数据对比"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
    )
)
line.render(path="折线图.html")
