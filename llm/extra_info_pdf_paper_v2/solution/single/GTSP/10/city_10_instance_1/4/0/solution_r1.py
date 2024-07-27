import math
from itertools import product

# City coordinates
cities = {
    0: (53, 68),  # Depot
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

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute distances between all pairs including the depot
distances = {}
for city_a in cities:
    for city_b in cities:
        if city_a != city_b:
            distances[(city_a, city_b)] = euclidean_distance(city_a, city_b)

# Function to compute the total distance of a given tour
def compute_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[(tour[i], tour[i+1])]
    return total_distance

# Brute-force search to find the best tour
best_tour = None
best_distance = float('inf')

# Generate all possible tours by choosing one city from each group
for cities_combination in product(*groups):
    # Create the tour starting and ending at the depot
    current_tour = [0] + list(cities_combination) + [0]
    # Calculate the total distance of this tour
    current_distance = compute_tour_distance(current_tour)
    # Check if this tour is better than the current best
    if current_distance < best_distance:
        best_distance = current_distance
        best_tour = current_tour

# Output the best tour and the corresponding travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))