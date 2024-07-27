import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Generate a distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate))];
# Function to compute total cost and max distance for a tour
def compute_tour_cost(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distances[(tour[i], tour[i + 1])]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Brute-force approach to find the best tour minimizing the maximal distance between consecutive cities
min_max_distance = float('inf')
best_tour = None
best_total_cost = 0

# Iterate over all permutations of cities excluding the depot
for perm in permutations(range(1, len(cities))):
    tour = [0] + list(perm) + [0]
    total_cost, max_distance = compute_tour_cost(tour)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_res_));
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")