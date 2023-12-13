import pandas as pd
# import Customer as new
import re
df1=pd.read_csv(r'.\6\FairDealCustomerData.csv')
df1['name']
# for i in df1:
    # print(i['name'])

df1['title'] = df1['name'].str.extract('(\w+\.) ')
df1['firstname'] = df1['name'].str.extract('(?:\w+\.\s)?(\w+)')
# df1['middlename'] = df1['name'].str.extract('(?:\w+\.\s)?(?:\w+\s)(\w+)(?:\s[\w-]+)$')
df1['lastname'] = df1['name'].str.extract('([\w\-]+)$')

print (df1.head(5))

class Error(Exception):
    pass

class CustomerNotAllowedException(Error):
    pass


while True:
    try:
        pass
    except ValueError:
        pass
    except CustomerNotAllowedException:
        pass
print("Congratulations! You agreeed to us!")