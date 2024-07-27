import numpy as np
from itertools import permutations

# Define the city positions
cities = [
    (16, 90),  # City 0 - Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

def euclidean_distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5

# Create a matrix of distances
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Sort edges by their weight
edges = [(i, j, distances[i][j]) for i in range(n) for j in range(n) if i != j]
edges.sort(key=lambda x: x[2])

# Check for Hamiltonian path by trying permutations (Brute force approach)
def is_valid_tour(order):
    return order[0] == 0 and order[-1] == 0

def find_hamiltonian_cycle(max_dist):
    for order in permutations(range(n)):
        if not is_valid_tour(order):
            continue
        max_edge = max(distances[order[i]][order[i+1]] for i in range(n-1))
        if max_edge <= max_dist:
            return order
    return None

# Find the minimum bottleneck value
for idx, edge in enumerate(edges):
    max_distance = edge[2]
    tour = find_hamiltonian_cycle(max_distance)
    if tour is not None:
        break

# Calculate total path cost and max edge in the best tour
max_edge_cost = max(distances[tour[i]][tour[i + 1]] for i in range(n - 1))
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(n - 1))

print("Tour:", list(tour))
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_cost)