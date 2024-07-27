import itertools
import math
from sys import maxsize

# Given cities coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Calculate distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = distance(cities[i], cities[j])

# Function to calculate the max edge in a path
def max_edge_in_path(path):
    max_edge = 0
    for k in range(len(path) - 1):
        max_edge = max(max_edge, dist_matrix[path[k]][path[k + 1]])
    return max_edge

# Function to calculate total cost of path
def total_cost_of_path(path):
    total_cost = 0
    for k in range(len(path) - 1):
        total_cost += dist_matrix[path[k]][path[k + 1]]
    return total_cost

# Using itertools to attempt generating a Hamiltonian cycle from the depot
def find_min_bottleneck_hamiltonian_cycle():
    min_bottleneck = maxsize
    best_path = None
    all_cities = list(range(1, n))
    
    for permutation in itertools.permutations(all_cities):
        path = [0] + list(permutation) + [0]
        current_bottleneck = max_edge_in_path(path)
        if current_bottleneck < min_bottleneck:
            min_bottleneck = current_bottleneck
            best_path = path

    return best_path, total_cost_of_path(best_path), min_bottleneck

# Using brute force approach to find a tour with minimal bottleneck length
best_path, total_cost, min_bottleneck = find_min_bottleneck_hamiltonian_cycle()

print(f"Tour: {best_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {min_bottleneck}")