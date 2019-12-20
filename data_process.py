import pandas as pd
import numpy as nps
import matplotlib.pyplot as plt
import  seaborn as sns

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
#pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50



churn = pd.read_csv('churn.csv',encoding='utf-8')#是否丢失
custcall = pd.read_csv('custcall.csv')#电话记录
custinfo =  pd.read_csv('custinfo.csv')#客户信息
tariff = pd.read_csv('tariff.csv')#套餐信息

#print(churn)
#print(custcall)
#print(custinfo)
#print(tariff)
#按照id合并电话
custcall_merge = custcall.groupby(custcall['Customer_ID'],as_index=False).sum()

#print(churn['Customer_ID'])
#print(custcall_merge)
#print(custcall_merge['Customer_ID'])

#找出没有电话记录的标号
subtraction = list(set(churn['Customer_ID']).difference(set(custcall_merge['Customer_ID'])))#在前不在后
print(subtraction)
#在churn里面剔除没有电话记录的标号
print(churn[churn['Customer_ID']=='K244390'])
#churn_delnone = churn.drop
#异常值检测
