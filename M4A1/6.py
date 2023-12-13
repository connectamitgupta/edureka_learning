'''Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements
greater than 5.
'''
import numpy as np
na1=np.array([[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]])
# na1=np.array([0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11])

print(na1)
na2=na1>5
print(na2)