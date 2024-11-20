import numpy as np

def transition_after_n_steps(matrix, n):
    # Raise the matrix to the power of n
    return np.linalg.matrix_power(matrix, n)

# Example
P = np.array([
    [2, 0.5],
    [3, 0.6]
])

n = 2  # Number of steps
result = transition_after_n_steps(P, n)
print(result)