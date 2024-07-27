import math
import itertools

# City coordinates:
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 78)
}

# Euclidean distance calculation:
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.hypot(x2 - x1, y2 - y1)

# Generating distance matrix:
n_cities = len(cities)
distance_matrix = [[0 if i == j else distance(cities[i], cities[j]) for j in range(n_cities)] for i in range(n_cities)]

# Solution search (brute-force here, feasible because number of cities is small enough):
best_bottleneck = float('inf')
best_tour = None

# Iterate over all permutations of the cities (excluding the starting city 0)
for perm in itertools.permutations(range(1, n_cities)):
    tour = [0] + list(perm) + [0]
    local_bottleneck = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    if local_bottleneck < best_bottleneck:
        best_bottleneck = local_bottleneck
        best_tour = tour

# Calculate the total travel cost
total_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))

# Outputs:
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {best_bottleneck}")