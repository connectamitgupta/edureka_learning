'''Create a 10x10 array with random values and find the minimum and maximum
values.
'''
import numpy as np
x = np.random.random((10, 10))
print(x)
print("Minmum value from array is :  ",x.min())
print("Maximum value from array is : ",x.max())