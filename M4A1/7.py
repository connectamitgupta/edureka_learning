'''Create a numpy array having NaN (Not a Number) and print it.
array([ NaN, 1., 2., NaN, 3., 4., 5.])
Print the same array omitting all elements which are nan
'''
import numpy as np
p=np.array([ np.nan, 1., 2., np.nan, 3., 4., 5.])
# print(p[np.isnan(p)])

print(p[np.logical_not(np.isnan(p))])