'''Extract data from the given SalaryGender CSV file and store the data from each
column in a separate NumPy array'''

import numpy as np
import pandas as pd

x=pd.read_csv("./M4A1/SalaryGender.csv")
# print(type(x))
print(x.columns)
xcol=x.columns

for i in xcol:
    a=np.array(x[i])
    print(type(a))
    print(f"Date of {i} is:")
    print(a)