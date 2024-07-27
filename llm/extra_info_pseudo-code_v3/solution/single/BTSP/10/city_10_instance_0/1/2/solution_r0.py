import itertools
import math

# Coordinates of each city with 0 being the depot city
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute all edges between cities with associated distances
edges = {}
for (ci, xi), (cj, xj) in itertools.combinations(cities.items(), 2):
    dist = euclidean_distance(xi, xj)
    edges[(ci, cj)] = dist
    edges[(cj, ci)] = dist

# Function to calculate bottleneck value of the path
def max_edge_in_path(path):
    max_edge = max(edges[(path[i], path[i+1])] for i in range(len(path) - 1))
    return max_edge

# Function to calculate total distance of the path
def total_distance(path):
    total = sum(edges[(path[i], path[i+1])] for i in range(len(path) - 1))
    return total

# Brute-force calculation of the minimal bottleneck Hamiltonian cycle starting from the depot
best_max_edge = float('inf')
best_path = None

# Consider all permutations of cities except the depot (city 0)
for perm in itertools.permutations(range(1, len(cities))):
    path = [0] + list(perm) + [0]  # creating a cycle back to the depot
    current_max_edge = max_edge_in_path(path)
    
    if current_max_edge < best_max_edge:
        best_max_edge = current_max_edge
        best_path = path

# If a best tour is found, calculate its properties
if best_path:
    best_total_distance = total：
    distance(best_path)
    print(f"Tour: {best_path}")
    print(f"Total travel cost: {best_total_distance}")
    print(f"Maximum distance between consecutive cities: {best_max_e}")
else:
    print("Failed to find a viable tour.")