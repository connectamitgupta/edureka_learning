'''2. Plot Total Sales Per Month for Year 2011 as Bar Chart. Is Bar Chart Better to
visualize than Simple Plot?
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('./M5A2/BigMartSalesData.csv')

print(df.head())

print(df.keys())
df['month_total']=df.groupby(['Year','Month'])['Amount'].transform('sum')
# df_new['tsales']=df_new.groupby(['name'])['net_price'].transform('sum')
print(df)
# df.to_csv('test.csv')
## removing duplicate
df.drop_duplicates(['Year','Month'],inplace=True)
print(df)
## Adding Period Columns by concatenating Year and Month
df['period']=df['Year'].astype(str)+"-"+df['Month'].astype(str)

## Filter for Year 2011
df=df[df['Year']==2011]

x=df['period']
y=df['month_total']

## Generating chart
plt.bar(x,y)
plt.xlabel("Period")
plt.ylabel('Total Sales')
plt.title("Graph showing total Sales made by each period in 2011")
plt.show()
plt.savefig('./M5A2/2.png')