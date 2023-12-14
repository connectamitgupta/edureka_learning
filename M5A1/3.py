'''Plot a pie-chart of the number of models released by every manufacturer,
recorded in the data provide. Also mention the name of the manufacture with
the largest releases
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('./M5A1/Cars2015.csv')
print(df.head())

# makers=df['Make'].unique()
# print(makers)

# makers_count=df.groupby(['Make','Model'])['Make'].count()
# makers_count=df.groupby(['Make'])['Make'].count()
# makers_count=df.groupby(['Make'])['Make'].transform('count')
## Count models by grouping make and get it into seperate column
df['count']=df.groupby('Make')['Model'].transform('count')
print(df)
## removing duplicates from dataframe
df.drop_duplicates('Make',inplace=True)

df.sort_values(by='count',ascending=False,inplace=True)

## Removing the columns that are not necessary
df = df.drop(['Type','LowPrice','HighPrice','Drive','CityMPG','HwyMPG','FuelCap','Length','Width','Wheelbase','Height','UTurn','Weight','Acc030','Acc060','QtrMile','PageNum','Size'], axis=1)


## Ploting chart
plt.figure(figsize=(40,20))

ax1 = plt.subplot(121, aspect='equal')

df.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%',startangle=0, shadow=False, labels=df['Make'], legend = False, fontsize=10, colors=['lime','greenyellow','chartreuse']) 

plt.show()