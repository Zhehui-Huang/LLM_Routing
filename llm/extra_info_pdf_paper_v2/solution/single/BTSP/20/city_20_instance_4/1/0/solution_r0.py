import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 
    18: (64, 72), 19: (14, 89)
}

# Compute Euclidean distances between each pair of cities
def compute_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean(cities[i], cities[j])
    return distances

# Brute-force approximation to find a minimal bottleneck Hamiltonian cycle
def find_bottleneck_hamiltonian_cycle(distances):
    num_cities = distances.shape[0]
    min_bottleneck = float('inf')
    optimal_tour = None
    
    for perm in permutations(range(1, num_cities)):
        cycle = [0] + list(perm) + [0]
        max_edge_cost = max(distances[cycle[i]][cycle[i+1]] for i in range(len(cycle) - 1))
        
        if max_edge_cost < min_bottleneck:
            min_bottleneck = max_edge_cost
            optimal_tour = cycle
    
    total_cost = sum(distances[optimal_tour[i]][optal_tour[i+1]] for i in range(len(optimal_tour) - 1))
    return optimal_tour, total_cost, min_bottleneck

# Main function to solve BTSP
def solve_BTSP(cities):
    distances = compute_distances(cities)
    tour, total_cost, max_distance = find_bottleneck_hamiltonian_cycle(distances)
    return tour, total_cost, max_distance

# Solve the BTSP and print results
tour, total_cost, max_distance = solve_BTSP(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")