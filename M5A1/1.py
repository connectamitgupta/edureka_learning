'''You are given a dataset, which is present in the LMS, containing the number of
hurricanes occurring in the United States along the coast of the Atlantic. Load the
data from the dataset into your program and plot a Bar Graph of the data, taking
the Year as the x-axis and the number of hurricanes occurring as the Y-axis.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=pd.read_csv("./M5A1/Hurricanes.csv")
print(a.head())
yearDf=a['Year']
hurrDf=a['Hurricanes']
# x=list(a.keys())
# y=list(a.values())
print(a.keys())
plt.bar(yearDf,hurrDf)
plt.xlabel("Years")
plt.ylabel("No. of Hurricanes")
plt.title("Bar Graph for No. of Hurricanes Year wise")
plt.grid(True)
plt.savefig('plot.png')
plt.show()