import numpy as np
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 55),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x_diff = cities[city1][0] - cities[city2][0]
    y_diff = cities[city1][1] - cities[city2][1]
    return np.sqrt(x_diff**2 + y_diff**2)

num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

# Compute distances between each pair of cities
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = euclidean_distance(i, j)

# Generate all permutations of city visits excluding the depot
perms = permutations(range(1, num_cities))

best_tour = None
best_total_cost = np.inf
best_max_distance = np.inf

# Evaluate each permutation to find the optimal tour
for perm in perms:
    tour = [0] + list(perm) + [0]
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total2.istanbul_protocolistance: {best_max_distance}")