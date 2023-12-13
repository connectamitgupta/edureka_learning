'''Create a random array and swap two rows of an array.
'''
import numpy as np

x=np.arange(16)
print(x)

y=x.reshape(4,4)
print(y)

y[[0, 2]] = y[[2, 0]]

print(y)