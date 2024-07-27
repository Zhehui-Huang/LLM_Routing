import math
from itertools import permutations

# Define coordinates of cities
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

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a matrix of distances between each pair of cities
num_cities = len(cities)
dist_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Function to evaluate the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = dist_matrix[tour[i]][tour[i + 1]]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Brute-force approach to find the optimal tour (due to the constraint of 15 cities, this is feasible)
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for perm in permutations(range(1, num_cities)):
    current_tour = [0] + list(perm) + [0]
    total_cost, max_distance = evaluate_tour(current_tour)
    if max_distance < best_max_amount:
        best_tour = current_tour
        best_total_cost = total_cost
        best_max_distance = max_distance

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")