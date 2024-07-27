import numpy as np
from scipy.spatial.distance import euclidean

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
    tour = [0] + list(np.random.choice(V, k-1, replace=False)) + [0]
    return tour

def shake(tour, k):
    middle = np.random.choice(tour[1:-1], size=k-2, replace=False)  # Select k-2 random cities
    new_tour = [0] + list(middle) + [0]
    return new_tour

def vnd(tour, D):
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                # Swap two cities
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if calculate_total_distance(new_tour, D) < calculate_total_distance(best_tour, D):
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

def gvns(V, D, k, Nrst):
    best_tour = None
    best_distance = float('inf')

    for _ in range(Nrst):
        S = generate_initial_solution(V, k)
        for _ in range(100):
            S_prime = shake(S, k)
            S_prime = vnd(S_prime, D)
            distance_prime = calculate_total_distance(S_prime, D)
            if distance_prime < best_distance:
                best_tour = S_prime[:]
                best_distance = distance_prime
                S = S_prime[:]
    return best_tour, best_distance

# Defining cities and distances
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
          (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
          (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]
k = 8  # Total including the depot
D = generate_distance_matrix(cities)

# Run the generalized VNS for k-TSP
Nrst = 10  # Number of restarts
tour, cost = gvns(range(1, 15), D, k, Nrst)

# Ensuring the depot (city 0) is included properly in the tour
tour = [0] + [city for city in tour if city != 0] + [0]
cost = calculate_total_distance(tour, D)

print("Tour:", tour)
print("Total travel cost: {:.2f}".format(cost))