import numpy as np
import random

# Define the cities and coordinates
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Generate distance matrix
def euclidean_distance(x, y):
    return np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def generate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

dist_matrix = generate_distance_matrix(list(coordinates.values()))

# Generate initial solution
def generate_initial_solution(n_cities=15, n_visit=10):
    tour = [0] + random.sample(list(range(1, n_cities)), n_visit-2) + [0]
    return tour

# Fitness evaluation
def compute_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Simple neighborhood swap function
def neighborhood_swap(tour):
    i1, i2 = sorted(random.sample(range(1, len(tour) - 2), 2))
    new_tour = tour[:]
    new_tour[i1], new_tour[i2] = tour[i2], tour[i1]
    return new_tour

def local_search(tour, dist_matrix):
    current_cost = compute_tour_cost(tour, dist_matrix)
    for _ in range(100):
        candidate_tour = neighborhood_swap(tour)
        candidate_cost = compute_tour_cost(candidate_tour, dist_matrix)
        if candidate_cost < current_cost:
            tour, current_cost = candidate_tour, candidate_cost
    return tour

# GVNS Algorithm
def gvns(k, dist_matrix, n_restarts=50):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(n_restarts):
        tour = generate_initial_solution(n_visit=k+1)
        tour = local_search(tour, dist_matrix)
        tour_cost = compute_tour_cost(tour, dist_matrix)
        
        if tour_cost < best_cost:
            best_tour, best_cost = tour, tour_cost
            
    return best_tour, best_cost

# Find a solution
best_tour, best_cost = gvns(9, dist_matrix)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))