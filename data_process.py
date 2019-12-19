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
custcall = pd.read_csv('custcall.csv')
custinfo =  pd.read_csv('custinfo.csv')
tariff = pd.read_csv('tariff.csv')

#print(churn)
#print(custcall)
#print(custinfo)
#print(tariff)
#按照id合并电话
custcall_merge = custcall[['Peak_calls',  'Peak_mins', 'OffPeak_calls' ,'OffPeak_mins',
                     'Weekend_calls' ,'Weekend_mins','International_mins','Nat_call_cost', 'month'
                     ]].groupby(custcall['Customer_ID']).sum()

print(churn)
print(custcall_merge)
print(custinfo)
