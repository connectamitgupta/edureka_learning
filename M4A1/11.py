'''Create a random array of 3 rows and 3 columns and sort it according to 1st column,
2nd column or 3rd column.
'''

import numpy as np
a = np.random.random((3, 3))
print(a)

a = a[a[:,2].argsort()] # First sort doesn't need to be stable.
a = a[a[:,1].argsort(kind='mergesort')]
a = a[a[:,0].argsort(kind='mergesort')]
print("New sorted array: ")
print(a)