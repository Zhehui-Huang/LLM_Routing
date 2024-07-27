import math
from itertools import permutations

# Locations of cities
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

# Calculate Euclidean distance between two cities
def calc_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a list of all distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calc_distance(cities[i], cities[j])

# Sort edges based on the distances
sorted_edges = sorted(distances.items(), key=lambda item: item[1])

# Function to check if all vertices are covered in a tour
def is_valid_tour(tour):
    return len(set(tour)) == len(cities)

# Function to find the Hamiltonian path using backtracking
def find_hamiltonian_path(bottleneck):
    for perm in permutations(cities.keys()):
        valid = True
        max_dist_in_tour = 0
        for i in range(len(perm) - 1):
            if distances[(perm[i], perm[i + 1])] > bottleneck:
                valid = False
                break
            max_dist_in_tour = max(max_dist_in_tour, distances[(perm[i], perm[i + 1])])
        if valid and distances[(perm[-1], perm[0])] <= bottleneck:
            max_dist_in_tour = max(max_dist_in_tour, distances[(perm[-1], perm[0])])
            return list(perm), perm[0], perm[-1], max_dist_in_tour
    return None

# Main algorithm
def bottleneck_tsp():
    # Iterate over sorted edges to incrementally consider higher bottlenecks
    for ci, dist in sorted_edges:
        path_info = find_hamiltonian_path(dist)
        if path_info:
            perm, start, end, max_dist = path_info
            if start == 0 and end == 0:
                total_dist = sum(distances[(perm[i], perm[i+1])] for i in range(len(perm)-1))
                total_dist += distances[(perm[-1], perm[0])]
                return {
                    "Tour": perm + (perm[0],),
                    "Total travel cost": total_dist,
                    "Maximum distance between consecutive cities": max_dist
                }

# Run the algorithm
result = bottleneck_tsp()
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel             cost']}")
print(f"Maximum distance between consecutive cities:  {result['Maximum distance between consecutive cities']}")