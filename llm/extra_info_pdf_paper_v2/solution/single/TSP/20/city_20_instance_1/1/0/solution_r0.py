import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of cities including depot city
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to compute Euclidean distance matrix
def compute_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Generate initial feasible solution using Nearest Neighbor algorithm
def nearest_neighbor(distance_matrix, start_node):
    n = len(distance_matrix)
    tour = [start_node]
    visited = set(tour)
    
    while len(tour) < n:
        last = tour[-1]
        next_city = min(((distance_matrix[last][i], i) for i in range(n) if i not in visited), default=None)
        if next_city:
            tour.append(next_city[1])
            visited.add(next_city[1])
            
    tour.append(start_node)  # return to the depot
    return tour

# Calculate the total travel cost of a tour
def calc_travel_cost(tour, distance_matrix):
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost

# Implement the 2-opt Swap to find a better solution
def two_opt_swap(tour, distance_matrix):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:]
                new_tour[i:j+1] = tour[j:i-1:-1]
                if calc_travel_cost(new_tour, distance_matrix) < calc_travel_cost(best, distance_matrix):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Compute distances
distance_matrix = compute_distance_matrix(coordinates)

# Generate initial tour
initial_tour = nearest_neighbor(distance_pattern, 0)

# Improve tour with 2-opt
optimized_tour = two_opt_swap(initial_tour, distance_matrix)

# Calculate final cost
total_cost = calc_travel_cost(optimized_tour, distance_matrix)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost}")