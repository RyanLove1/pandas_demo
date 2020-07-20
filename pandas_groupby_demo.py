import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
# 单个列groupby，查询所有数据列的统计
res = df.groupby('A').sum()
print(res)
'''
            C         D
A                      
bar  0.824350 -0.648460
foo -2.336797  1.051068
'''

# 多个列groupby，查询所有数据列的统计
res2 = df.groupby(["A", "B"]).mean()
print(res2)
'''
                  C         D
A   B                        
bar one    0.178278  1.291439
    three -1.802238 -0.349516
    two    0.077436 -0.133885
foo one    0.612781 -0.222823
    three  0.346936 -1.194908
    two   -0.201423  0.414962
'''

res3 = df.groupby(['A','B'], as_index=False).mean()
print(res3)
'''
     A      B         C         D
0  bar    one -1.120294 -0.374252
1  bar  three -1.468270 -0.520066
2  bar    two -0.654800  0.841732
3  foo    one -0.094773 -1.547075
4  foo  three -2.190413  0.421233
5  foo    two -0.933326 -0.778788
'''

# 同时查看多种数据统计
res4 = df.groupby('A').agg([np.sum, np.mean, np.std])
print(res4)
'''
            C                             D                    
          sum      mean       std       sum      mean       std
A                                                              
bar  0.085034  0.028345  0.893999  0.736753  0.245584  1.329135
foo  0.969839  0.193968  0.753646 -1.305077 -0.261015  0.866502
'''

# 查看单列的结果数据统计
# 方法1：预过滤，性能更好
res5 = df.groupby('A')['C'].agg([np.sum, np.mean, np.std])
print(res5)
'''
          sum      mean       std
A                                
bar -0.177244 -0.059081  0.714634
foo -0.242403 -0.048481  0.811584
'''

# 方法2
res6 = df.groupby('A').agg([np.sum, np.mean, np.std])['C']

# 不同列使用不同的聚合函数
res7 = df.groupby('A').agg({"C":np.sum, "D":np.mean})
print(res7)
'''
            C         D
A                      
bar  1.809787  0.441989
foo  2.049895  0.798035
'''

# 实例分组探索天气数据
df_tq = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv", engine='python',
                 encoding='utf-8')
print(df_tq.head())
# 替换掉温度的后缀℃
df_tq.loc[:, "bWendu"] = df_tq["bWendu"].str.replace("℃", "").astype('int32')
df_tq.loc[:, "yWendu"] = df_tq["yWendu"].str.replace("℃", "").astype('int32')
print(df_tq.head())

# 新增一列为月份
df_tq['month'] = df_tq['ymd'].str[:7]

# 查看每个月的最高温度
data = df_tq.groupby("month")["bWendu"].max()
print(data)

# 查看每个月的最高温度、最低温度、平均空气质量指数
group_data = df_tq.groupby('month').agg({"bWendu":np.max, "yWendu":np.min, "aqi":np.mean})
print(group_data)