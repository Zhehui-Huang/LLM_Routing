import math
from itertools import permutations

# Define the cities with their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Create a dictionary to hold the distances
distances = {}
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Function to calculate the maximum and total distance of a tour
def evaluate_tour(tour):
    max_distance = 0
    total_distance = 0
    for k in range(len(tour)-1):
        dist = distances[(tour[k], tour[k+1])]
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Test all permutations of the cities (excluding the starting city 0)
min_bottleneck = float('inf')
best_tour = None

for perm in permutations(range(1, n)):
    tour = [0] + list(perm) + [0]
    _, max_dist = evaluate_tour(tour)
    if max_dist < min_bottleneck:
        min_bottleneck = max_dist
        best_tour = tour

# Calculating the final total and maximum distances for the best tour
total_cost, max_distance = evaluate_tour(best_tour)

# Output the best tour, total travel cost and the bottleneck distance
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))