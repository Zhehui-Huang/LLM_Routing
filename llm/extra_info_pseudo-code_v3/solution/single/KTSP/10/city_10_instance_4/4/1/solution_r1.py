import numpy as np
import random

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(V):
    tour = [0] + random.sample(V[1:], 7)
    tour.append(0)
    return tour

def shake(tour, k):
    n = len(tour)
    for _ in range(k):
        i, j = np.random.randint(1, n - 1, size=2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def vnd(tour, distance_matrix):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j - i == 1:
                    continue
                new_tour = tour[:]
                new_tour[i:j] = tour[i:j][::-1]
                if calculate_total_distance(new_tour, distance_matrix) < calculate_total_temperature(tour, distance_matrix):
                    tour = new_tour
                    improvement = True
    return tour

def gvns(k, V, distance_matrix, Nrst):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        S_cost = calculate_total_distance(S, distance_matrix)
        
        for _ in range(100):  # fixed number of iterations for shaking and VND loops
            S_prime = shake(S.copy(), k)
            S_double_prime = vnd(S_prime, distance_matrix)
            S_double_prime_cost = calculate_total_distance(S_double_prime, distance_matrix)
            
            if S_double_prime_cost < S_cost:
                S = S_double_prime
                S_cost = S_double_prime_cost
                if S_cost < best_cost:
                    best_tour = S
                    best_cost = S_cost
    return best_tour, best_cost

# Coordinates of the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Create a distance matrix
V = list(cities.keys())
distance_matrix = np.zeros((len(V), len(V)))

for i in V:
    for j in V:
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Executing the GVNS algorithm
best_tour, best_cost = gvns(2, V, distance_matrix, 100)  # using 2 for shaking, 100 restarts

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))