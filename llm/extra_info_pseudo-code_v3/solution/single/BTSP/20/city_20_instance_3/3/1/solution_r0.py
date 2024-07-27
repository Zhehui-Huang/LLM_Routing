import math
from itertools import permutations

# Coordinates of the cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all distances and create a sorted edge list
n = len(coordinates)
distances = {}
edges = []

for i in range(n):
    for j in range(i + 1, n):
        d = calc_distance(coordinates[i], coordinates[j])
        distances[(i, j)] = d
        distances[(j, i)] = d
        edges.append((d, i, j))

# Sort edges by distance
edges.sort()

# Find Hamiltonian path using a heuristic method (here, simple backtracking)
def valid_tour(cities, max_dist):
    # Generate all permutations of cities, starting and ending with the depot (0)
    for perm in permutations(cities[1:]):
        tour = [0] + list(perm) + [0]
        max_edge_length = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        if max_edge_length <= max_dist:
            return tour, max_edge_length
    return None, None

# Attempt to construct the Hamiltonian circuit
best_tour = None
min_max_dist = float('inf')

for dist, u, v in edges:
    # Try with current max edge length
    tour, max_edge_length = valid_tour(list(range(n)), dist)
    if tour is not None:
        best_tour = tour
        min_max_dist = max_edge_length
        break

if best_tour is not None:
    # Calculate total travel cost of the best tour
    total_cost = sum(distances[(best_tour[i], best_tour[i+1])] for i in range(len(best_tour) - 1))
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {min_max_dist:.2f}")
else:
    print("Failed to find a suitable Hamiltonian cycle.")