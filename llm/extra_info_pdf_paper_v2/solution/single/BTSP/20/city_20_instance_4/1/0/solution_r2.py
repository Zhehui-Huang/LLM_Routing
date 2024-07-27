import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to compute the Euclidean distances
def compute_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            dist = euclidean(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

# Function to find the bottleneck Hamiltonian cycle using brute-force
def find_bottleneck_hamiltonian_cycle(distances):
    best_tour = None
    min_max_distance = float('inf')
    num_cities = len(distances)
    
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_edge_cost = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if max_edge cost < min max_distance:
            min_max_distance = max_edge_cost
            best tour = tour
    
    total_travel_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    return best_tour, total_travel_cost, min_max_distance

# Compute distances
distances = compute_distances(cities)

# Find the best tour with the minimum bottleneck
tour, total_cost, max_distance = find_bottleneck_hamiltonian_cycle(distances)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")