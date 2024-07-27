import math
import itertools

# Given cities with their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances(cities):
    """Calculates a distance matrix."""
    n = len(cities)
    distances = {}
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_heaist = euclidean_distance(cities[i], cities[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist
    return distances

def find_hamiltonian_path(cities, max_dist):
    """ Check for Hamiltonian path that meets the maximum distance condition."""
    n = len(cities)
    perms = itertools.permutations(range(1, n))  # All permutations of the cities except the depot
    for perm in perms:
        route = [0] + list(perm) + [0]
        valid = True
        max_edge = 0
        previous_city = 0
        for city in route[1:]:
            dist = distances[(previous_city, city)]
            if dist > max_dist:
                valid = False
                break
            max_edge = max(max_edge, dist)
            previous_city = city
        if valid:
            return route, max_edge
    return None

# Compute distances between all pairs of cities
distances = calculate_distances(cities)

# Get all unique distances and sort them
unique_distances = sorted(set(distances.values()))

# Bottleneck TSP Algorithm
for c_i in unique_distances:
    result = find_hamiltonian_path(cities, c_i)
    if result:
        tour, max_edge = result
        break

# Calculate the total travel cost of the tour
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge}")