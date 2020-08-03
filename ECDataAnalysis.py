'''分析数据相关性'''

import pandas as pd

#导入数据
data = pd.read_excel(r'F:\python_work\ECDataAnalysis\001.xlsx',sheet_name = 'sheet1')
print(data)

#相关系数矩阵计算
a = list(data.columns[4:])
print(data[a].corr())

data1 = data.copy()
data1 =data1.drop(['学号','班级','姓名','性别','类别'],axis = 1)
print(data1)
#计算各科成绩与总分score的相关系数
a1 = pd.DataFrame(data1.corr()['score'].abs())
print(a1)
bins = [0,0.3,0.8,1.1]
label = ['低度相关','中度相关','高度相关']
a1['相关程度'] = pd.cut(a1['score'],bins,right = False,labels = label)
print(a1)

'''
相关系数|r|
0<=|r|<0.3    :低度相关
0.3<=|r|<0.8  :中度相关
0.8<=|r|<=1   :高度相关

'''