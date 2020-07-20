import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

# 读取百度股票，并设置时间列为索引，类型为日期格式
df = pd.read_excel("D:/python基础课程/pandas/ant-learn-pandas/datas/stocks/baidu_stocks.xlsx",
                   index_col="datetime",
                   parse_dates=True
                   )
print(df.head())

# 按时间升序
df.sort_index(inplace=True)
print(df.head())

# 使用Pyecharts绘制折线图
# 折线图
line = Line()

# x轴
line.add_xaxis(df.index.tolist())

# 每个y轴
line.add_yaxis("开盘价", df["open"].round(2).tolist())
line.add_yaxis("收盘价", df["close"].round(2).tolist())

# 图表配置
line.set_global_opts(
    title_opts=opts.TitleOpts(title="百度股票2019年"),
    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
)

# 渲染数据，生成html
line.render()