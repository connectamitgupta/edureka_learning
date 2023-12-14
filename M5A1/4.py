'''Create csv file from the data below and read in pandas data frame
Phase 1 -Reading Data   Phase 2 –Describe the data  Describe the data on the unit price
Phase 3 –filter the data    Create new dataframe having columns 'name','net_price','date' and group all the
records according to name
Phase 4 –Plotting graph
Plot the graph after calculating total sales by each customer. Customer name should be
on x axis and total sales in y axis.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./M5A1/sample-salesv2.csv')
print(df.head())
print(df.describe())
### Phase 2  Describing data only on unit price
print(df['unit price'].describe())

### Phase 3  Data Filter
df_new=df.drop(['account_number','item_code','category','quantity','unit price'],axis=1)
print(df_new.head())  
# df['count']=df.groupby('Make')['Model'].transform('count')

### Phase 4  Chart Plot
df_new['tsales']=df_new.groupby(['name'])['net_price'].transform('sum')
print(df_new.head())
## removing duplicates from dataframe
df.drop_duplicates('name',inplace=True)
x=df_new['name']
y=df_new['tsales']
plt.bar(x,y)
plt.xlabel("Name of Customers")
plt.ylabel('Total Sales')
plt.title("Graph showing total purchsae made by respective customer")
plt.show()