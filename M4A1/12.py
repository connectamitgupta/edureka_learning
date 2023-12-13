'''Create a four dimensions array get sum over the last two axis at once.
'''
import numpy as np
a = np.random.random((3, 3, 3, 3))
print(a)
print(a.sum(axis=0))