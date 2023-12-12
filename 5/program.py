import pandas as pd
import os
# import .\5\Customer
# print(os.getcwd())
# import numpy as np
x=pd.read_csv(r".\5\bank-data.csv")
# xdf=pd.DataFrame(x)
minage=x['age'].min()
maxage=x['age'].max()
# print(x['job'].unique())
listjob=x['job'].unique()

print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                     Program to check customer valid or not                            
-----------------------------------------------------------------------------------
      press END to terminate''')

def custvalidate(job,age):
    if job=="END":
        pass
        # break
    if ((job not in listjob) and (age not in range(minage,maxage))):
        print("Cutomer is not eligible")
        print(f"Age for eligible between:{minage} and {maxage} and valid professions: {listjob}")
    else:
        print("Customer is eligible.")
        
while True:
    x=input("Enter customer profession: ")
    if x=="END":
        # pass
        print("Terminating program...Thanks for fair usage")
        break
    y=input("Enter customer age: ")
    custvalidate(x,y)