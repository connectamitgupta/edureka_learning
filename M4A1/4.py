'''Calculate the total number of people who have a PhD degree from SalaryGender
CSV file
'''

import pandas as pd

x=pd.read_csv("./M4A1/SalaryGender.csv")
m=x[(x['PhD']==1)]
print("Total no. of people who have PhD Degrees: ",m.shape[0])