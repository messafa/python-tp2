import numpy as np

def create_transition_matrix(r):
    P = np.zeros((r+1, r+1))
    
    for i in range(r+1):
        for j in range(r+1):
            if i == j-1:  # Formula 1: p(i,i+1) = (r-i)^2/r^2
                P[i,j] = ((r-i)**2)/(r**2)
            elif i == j+1:  # Formula 2: p(i,i-1) = i^2/r^2
                P[i,j] = (i**2)/(r**2)
            elif i == j:  # Formula 3: p(i,i) = 2i(r-i)/r^2
                P[i,j] = (2*i*(r-i))/(r**2)
    
    return P

r = 3
P = create_transition_matrix(r)
print("Transition Matrix P:")
print(P)

print("\nRow sums (should all be close to 1):")
print(np.sum(P, axis=1))