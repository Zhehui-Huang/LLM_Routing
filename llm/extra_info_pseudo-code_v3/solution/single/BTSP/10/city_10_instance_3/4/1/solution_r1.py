import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Get all pairs of cities and distances
edges = []
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = calculate_distance(cities[i], cities[j])
        edges.append(((i, j), dist))
        edges.append(((j, i), dist))  # Since the graph is undirected

# Sort edges by distance
edges = sorted(edges, key=lambda x: x[1])

def is_hamiltonian_path_possible(max_edge_length):
    "Check if there is a Hamiltonian path in the graph limited by max_edge_length"
    included_edges = [e for e in edges if e[1] <= max_edge_length]
    adjacency_list = {i: [] for i in cities.keys()}
    for edge, _ in included_edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_dispatch[edge[1]].append(edge[0])

    # Attempt to find any permutation that is a valid Hamiltonian cycle
    for perm in permutations(range(1, len(cities))):
        perm = [0] + list(perm) + [0]
        valid = True
        for i in range(1, len(perm)):
            if perm[i] not in adjacency_list[perm[i-1]]:
                valid = False
                break
        if valid: 
            return True, perm
    return False, []

# Using binary search on sorted edges to find the minimum maximum edge length in a valid path
low, high = 0, len(edges) - 1
best_path = []
while low <= high:
    mid = (low + high) // 2
    possible, path = is_hamiltonian_path_possible(edges[mid][1])
    if possible:
        high = mid - 1
        best_path = path
    else:
        low = mid + 1

# Calculate the total cost and the maximum distance between consecutive cities in the tour
if best_path:
    max_distance = max(calculate_distance(cities[best_path[i]], cities[best_path[i + 1]]) for i in range(len(best_path) - 1))
    total_travel_cost = sum(calculate_distance(cities[best_path[i]], cities[best_path[i + 1]]) for i in range(len(best_path) - 1))
    
    # Printing required outputs
    print(f"Tour: {best_path}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No valid tour was found.")