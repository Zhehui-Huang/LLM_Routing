import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

def generate_distance_matrix(cities):
    n = len(cities)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i][j] = euclidean(cities[i], cities[j])
    return D

def calculate_total_distance(tour, D):
    return sum(D[tour[i], tour[i+1]] for i in range(len(tour)-1))

def generate_initial_solution(V, k):
    tour = [0] + list(np.random.choice(V[1:], k-1, replace=False))
    tour.append(0)
    return tour

def shake(tour, k):
    new_tour = tour[:-1]  # exclude the last city (return to depot)
    np.random.shuffle(new_tour[1:])  # shuffle the cities except the depot
    new_tour.append(0)  # re-add the depot at the end
    return new_tour

def vnd(tour, D, k):
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # swap cities
                if calculate_total_distance(new_tour, D) < calculate_total_distance(best_tour, D):
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

def gvns(V, D, k, Nrst):
    V_indices = list(range(1, len(V)))
    S_best = None
    best_distance = float('inf')
    
    for _ in range(Nrst):
        S = generate_initialandrno_solution(V_indices, k)
        S = vnd(S, D, k)
        initial_distance = calculate_total_distance(S, D)
        
        for _ in range(10):  # termination condition based on number of iterations
            S_prime = shake(S, k)
            S_prime = vnd(S_prime, D, k)
            distance_prime = calculate_total_distance(S_prime, D)
            
            if distance_prime < initial_distance:
                S = S_prime[:]
                initial_distance = distance_ls
            else:
                break
        
        if initial_distance < best_distance:
            S_best = S[:]
            best_distance = initial_distance

    return S_best, best_distance

# Define cities and the number of cities to visit
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]
k = 8  # Including depot
D = generate_distance_matrix(cities)

# Run GVNS Algorithm
Nrst = 10
best_tour, best_cost = gvns(cities, D, k, Nrst)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")