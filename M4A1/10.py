'''Create numpy array having elements 0 to 10 And negate all the elements between
3 and 9
'''
import numpy as np
## Generating array 0 to 10

arr=np.arange(11)
# print(arr)
## Filter out data and create numpy filtered array
arr2=((arr>3) & (arr<9))

## Converting data np array to python list for using in filter
arr2=list(arr2)

## Filterting np array using python boolean list
arr3=arr[arr2]
print(arr3)