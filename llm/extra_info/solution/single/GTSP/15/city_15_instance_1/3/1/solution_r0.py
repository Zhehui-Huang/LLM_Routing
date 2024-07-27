import math
from itertools import product

# Define the coordinates of each city including the depot
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define the city groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance between any two cities
def distance(city_a_id, city_b_id):
    city_a = cities[city_a_id]
    city_b = cities[city_b_id]
    d = math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)
    return d

# Function to compute the travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Generate all combination tours that visit each group once
all_combinations = product(*groups)
best_tour = None
best_cost = float('inf')

# Find the tour with the minimum distance
for group_choice in all_combinations:
    tour = [0] + list(group_choice) + [0]
    current_cost = calculate_tour_cost(tour)
    if current_cost < best_cost:
        best_tour = tour
        best_cost = current_cost

# Output the best tour and its cost
output_tour = f"Tour: {best_tour}"
output_cost = f"Total travel cost: {best_cost}"