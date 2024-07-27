import random
import numpy as np

# Given city coordinates
coordinates = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
               (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
               (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Calculate distance matrix
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j])
                    for j in range(len(coordinates))] for i in range(len(coordinates))]

def generate_initial_solution(V, k=8):
    return [0] + random.sample(V[1:], k - 1) + [0]

def shake(S):
    S_prime = S[1:-1]
    random.shuffle(S_prime)
    return [S[0]] + S_prime + [S[-1]]

def vnd(S):
    k = len(S) - 2
    for i in range(1, k):
        for j in range(i + 1, k + 1):
            new_S = S[:]
            new_S[i], new_S[j] = S[j], S[i]
            if fitness(new_S) < fitness(S):
                S = new_S
    return S

def fitness(S):
    return sum(distance_matrix[S[i]][S[i + 1]] for i in range(len(S) - 1))

def gvns(V, Nrst=1000):
    best_solution = generate_initial_solution(V)
    best_cost = fitness(best_solution)
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        while True:
            S_prime = shake(S)
            S_double_prime = vnd(S_prime)
            if fitness(S_double_prime) < fitness(S):
                S = S_double_prime
            else:
                break
        
        current_cost = fitness(S)
        if current_cost < best_cost:
            best_solution = S
            best_cost = current_cost
            
    return best_solution, best_cost

# Execute the GVNS
V = list(range(15))
best_solution, best_cost = gvns(V)

# Print results
print("Tour:", best_solution)
print("Total travel cost:", best_cost)