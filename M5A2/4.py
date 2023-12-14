'''4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.
In which range most of the invoice amounts are concentrated
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
# df=df[df['Year']==2011]

x=df['period']
y=df['month_total']

## Generating chart
# rng = np.random.RandomState(0)
# colors = rng.rand(100)
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# sizes = 1000 * rng.rand(100)

# plt.scatter(x,y,c=colors,s=sizes,alpha=0.3,cmap='viridis')
plt.scatter(x,y,c=colors)

# plt.xlabel("Period")
# plt.ylabel('Total Sales')
# plt.title("Graph showing total Sales made by each period in 2011")
plt.show()
plt.colorbar()
plt.savefig('./M5A2/4.png')