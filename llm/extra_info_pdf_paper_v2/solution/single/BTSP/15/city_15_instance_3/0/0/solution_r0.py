import math
import itertools

# City coordinates:
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Euclidean distance calculation:
def distance(point1, point2):
    return math.hypot(point2[0] - point1[0], point2[1] - point1[1])

# Generate distance matrix:
num_cities = len(cities)
dist_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = distance(cities[i], cities[j])

# Find the BTSP using brute force with permutation (feasible for 15 cities due to constrain to the pills):
min_bottleneck = float('inf')
best_tour = None

for perm in itertools.permutations(range(1, num_cities)):
    tour = [0] + list(perm) + [0]
    max_edge_cost = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    if max_edge_cost < min_bottleneck:
        min_bottleneck = max_edge_cost
        best_tour = tour

# Compute the total travel cost of the tour:
total_cost = sum(dist_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

# Return the results:
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {min_bottleneck}")