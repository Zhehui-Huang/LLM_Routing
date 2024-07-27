import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all pairwise distances
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

def calculate_costs(path):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(path)):
        dist = distances[path[i-1]][path[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return_to_depot = distances[path[-1]][path[0]]
    total_cost += return_to_depot
    if return_to_depot > max_distance:
        max_distance = return_to_depot
    return total_cost, max_distance

# Explore all permutations and find the optimal path
min_max_distance = float('inf')
best_tour = []
best_total_cost = 0

for perm in permutations(range(1, num_cities)):
    tour = [0] + list(perm) + [0]
    total_cost, max_distance = calculate_costs(tour)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {min_max_distance}")