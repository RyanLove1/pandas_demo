import pandas as pd

df_train = pd.read_csv("D:/python基础课程/pandas/ant-learn-pandas/datas/titanic/titanic_train.csv",
                   engine="python")
print(df_train.head())
'''
   PassengerId  Survived  Pclass    ...        Fare Cabin  Embarked
0            1         0       3    ...      7.2500   NaN         S
1            2         1       1    ...     71.2833   C85         C
2            3         1       3    ...      7.9250   NaN         S
3            4         1       1    ...     53.1000  C123         S
4            5         0       3    ...      8.0500   NaN         S
'''
# 其中，Survived==1代表这个人活下来了、==0代表没活下来；其他的都是这个人的信息和当时的仓位、票务情况
# 我们只挑选两列，作为预测需要的特征
feature_cols = ['Pclass', 'Parch']
X = df_train.loc[:, feature_cols]
print(X.head())

# 单独提取是否存活的列，作为预测的目标
y = df_train.Survived
print(y.head())

# 训练模型
from sklearn.linear_model import LogisticRegression
# 创建模型对象
logreg = LogisticRegression()

# 实现模型训练
logreg.fit(X, y)

print(logreg.score(X, y))
'''0.6879910213243546'''

# 对于未知数据使用模型
# 找一个历史数据中不存在的数据,(按照这两列去重)
res = X.drop_duplicates().sort_values(by=["Pclass", "Parch"])
print(res)
'''
     Pclass  Parch
1         1      0
54        1      1
27        1      2
438       1      4
9         2      0
98        2      1
43        2      2
437       2      3
0         3      0
7         3      1
8         3      2
86        3      3
167       3      4
13        3      5
678       3      6
'''
# 发现2，4是没有的
# 预测这个数据是否存活
res1 = logreg.predict([[2, 4]])
print(res1)
'''[1],表示存活'''
# # 预测这个数据存活的概率
res2 = logreg.predict_proba([[2, 4]])
print(res2)
'''
[[0.35053893 0.64946107]]
代表存活的概率是0.64946107，死亡的概率是0.35053893
'''


