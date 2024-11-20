import numpy as np

# Function to calculate the stationary distribution vector
def stationary_distribution(P):
    """
    Calculate the stationary distribution vector for a transition matrix
    :param P: Transition matrix (numpy array)
    :return: Stationary distribution vector
    """
    n = P.shape[0]
    # Solve the equation: (P' - I)π = 0 with the condition that the sum of probabilities = 1
    A = P.T - np.eye(n)
    A[-1, :] = 1  # Add the condition that the sum = 1
    b = np.zeros(n)
    b[-1] = 1
    return np.linalg.solve(A, b)

# Function to calculate the expected first passage time
def first_passage_time(P, target):
    """
    Calculate the expected first passage time to a specific state
    :param P: Transition matrix (numpy array)
    :param target: Target state
    :return: List of first passage times for each state
    """
    n = P.shape[0]
    M = np.zeros(n)  # First passage times
    for i in range(n):
        if i != target:
            M[i] = 1 + sum(P[i, j] * M[j] for j in range(n) if j != target)
    return M

# Example: Transition matrix
P = np.array([
    [0.5, 0.5, 0.0],
    [0.2, 0.8, 0.0],
    [0.0, 0.3, 0.7]
])

# 1. Calculate the stationary distribution vector
stationary_vector = stationary_distribution(P)
print("Stationary distribution vector:", stationary_vector)

# 2. Calculate the first passage times
target_state = 2  # Target state
first_passage_times = first_passage_time(P, target_state)
print(f"First passage times to state {target_state}:", first_passage_times)
