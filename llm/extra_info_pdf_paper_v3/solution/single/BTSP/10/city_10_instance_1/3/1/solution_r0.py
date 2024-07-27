import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (53, 68), 
    1: (75, 11), 
    2: (91, 95), 
    3: (22, 80), 
    4: (18, 63), 
    5: (54, 91), 
    6: (70, 14), 
    7: (97, 44), 
    8: (17, 69), 
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate all pairwise city distances
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = distance(i, j)

# Simple function to evaluate a given tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = distance(tour[i], tour[i + 1])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Find the tour that minimizes the maximum distance between consecutive cities (naive approach)
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for perm in permutations(range(1, num_cities)):  # Generate all permutations of city indices except the depot
    tour = [0] + list(perm) + [0]
    total_cost, max_distance = evaluate_tour(tour)
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_total_cost = total_cost
        best_tour = tour

# Output the results according to the format requirements
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))