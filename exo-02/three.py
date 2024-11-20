import numpy as np

def classify_markov_states(P):
    """
    Classify states in a Markov chain into recurrent and transient states.
    :param P: Transition matrix (numpy array)
    :return: Dictionary containing the classification of states
    """
    n = P.shape[0]
    print("zakarya",n)
    reachable = np.zeros((n, n), dtype=bool)

    # 1. Check reachability using repeated matrix multiplication
    power = np.eye(n)  # Identity matrix
    for _ in range(n):
        power = np.dot(power, P) 
        reachable = reachable | (power > 0) 

    # 2. Determine recurrent and transient states
    recurrent_states = []
    transient_states = []

    for i in range(n):
        if all(reachable[i, j] and reachable[j, i] for j in range(n) if reachable[i, j]):
            recurrent_states.append(i)
        else:
            transient_states.append(i)

    return {
        "Recurrent States": recurrent_states,
        "Transient States": transient_states,
    }

# Example transition matrix
P = np.array([
    [0.5, 0.5, 0.0],
    [0.2, 0.8, 0.0],
    [0.0, 0.3, 0.7]
])

# Call the function and classify the states
result = classify_markov_states(P)

print("États récurrents:", result["Recurrent States"])
print("États transitoires:", result["Transient States"])
