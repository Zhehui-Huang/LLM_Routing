import math
from itertools import permutations

# Coordinates of each city including the depot
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x_diff = cities[city1][0] - cities[city2][0]
    y_diff = cities[city1][1] - cities[city2][1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Evaluate a given tour: computes total cost and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

all_cities = list(cities.keys())
# Removing the starting and re-entrance to the depot to consider all permutations of cities only
city_indices_without_depot = all_cities[1:]

best_tour = None
best_btsp_max_dist = float('inf')
best_total_cost = float('inf')

# Check each permutation of the cities
for perm in permutations(city_indices_without_depot):
    current_tour = [0] + list(perm) + [0]
    current_total_cost, current_btsp_max_dist = evaluate_tour(current_tour)
    
    if current_btsp_max_dist < best_btsp_max_dist:
        best_btsp_max_dist = current_btsp_max_dist
        best_total_cost = current_total_cost
        best_tour = current_tour

# Outputting the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_btsp_max_dist, 2))