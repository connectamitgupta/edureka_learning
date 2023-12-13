'''Create a random matrix and Compute a matrix rank.'''

import numpy as np

def create_random_matrix(m, n):
  """Creates a random matrix of size m x n."""
  return np.random.randint(0, 10, size=(m, n))

def compute_matrix_rank(A):
  """Computes the rank of a matrix A."""
  return np.linalg.matrix_rank(A)

# Create a random matrix
A = create_random_matrix(3, 4)
print(A)
# Compute the rank of the matrix
rank = compute_matrix_rank(A)

# Print the rank of the matrix
print(rank)