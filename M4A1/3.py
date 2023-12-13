'''. Store the “Age” and “PhD” columns in one DataFrame and delete the data of all
people who don’t have a PhD from SalaryGender CSV file.
'''
# import numpy as np
import pandas as pd

x=pd.read_csv("./M4A1/SalaryGender.csv")
m=x[['Age','PhD']]
m=m[(m['PhD']==1)]
print('People who have PhD degree : ', m)
