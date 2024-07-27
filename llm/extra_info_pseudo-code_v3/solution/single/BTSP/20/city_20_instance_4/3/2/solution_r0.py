import math
from itertools import permutations

# Cities Coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Creating a list of all distances
edge_list = []
for i in range(len(cities)):
    for j in range(i+1, len(cities)):
        dist = distance(cities[i], cities[j])
        edge_list.append((i, j, dist))
        edge_list.append((j, i, dist))  # include reverse since undirected

# Sort edges by distance
edge_list.sort(key=lambda x: x[2])

# Helper function to find Hamiltonian cycles
def find_hamiltonian_path(max_distance):
    edges = {(u, v) for u, v, d in edge_list if d <= max_distance}
    # Check all permutations, this is computationally expensive
    for perm in permutations(range(1, len(cities))):
        path = [0] + list(perm) + [0]
        if all((path[i], path[i+1]) in edges for i in range(len(path)-1)):
            return path
    return None

# Main logic to find the optimal Bottleneck path
def bottleneck_tsp():
    for dist in sorted(set(dist for _, _, dist in edge_list)):
        path = find_hamiltonian_path(dist)
        if path:
            total_cost = sum(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
            max_distance = max(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
            return path, total_cost, max_distance

# Compute the optimal tour
tour, total_travel_cost, max_consecutive_distance = bottleneck_tsp()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_hppcost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")