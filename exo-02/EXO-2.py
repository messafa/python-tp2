import numpy as np

def is_valid_transition(P):
    print("\nRow sums (should all be close to 1):")
    vect = np.sum(P, axis=1)
    
    for i in range(len(vect)):
        if vect[i] != 1: 
            return False
    
    return True

def transition_after_n_steps(matrix, n):
    # Raise the matrix to the power of n
    return np.linalg.matrix_power(matrix, n)

size = int(input('Enter the size the matrix: '))
P = np.zeros((size, size))
for i in range(size):
    print('new row: ')
    for j in range(size):
        value = input('Enter matrix value: ')
        P[i][j] = value

if(is_valid_transition(P)):
    print('matrix is valid\n now will go to the second part:')
    n = int(input('Enter the number of steps: '))  # Number of steps
    result = transition_after_n_steps(P, n)
    print(result)
else:
    print('matrix is not valid')

