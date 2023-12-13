'''Find:
1. The number of men with a PhD
2. The number of women with a PhD'''


import numpy as np
import pandas as pd

x=pd.read_csv("./M4A1/SalaryGender.csv")
# print(x.query('Gender'=='1' and 'PhD'=='1'))
# a=x.query('Gender'=='1' and 'PhD'=='1')
# a=x.query('Gender'==0 & 'PhD'==1)
# x.info()
m=x[(x['Gender']==1) & (x['PhD']==1)]
w=x[(x['Gender']==0) & (x['PhD']==1)]
# print(p.count())
# # print(p.count())
# print("Man with Phd degree:   ",m.count())
# print("WoMan with Phd degree: ",w.count())

print("Man with Phd degree:   ",m.shape[0])
print("WoMan with Phd degree: ",w.shape[0])