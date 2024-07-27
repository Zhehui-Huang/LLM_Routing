import math
from itertools import permutations

# Define the cities
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
def calculate_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Generate all possible tours from city 0 and back to city 0
def generate_tours():
    city_indices = list(cities.keys())
    city_indices.remove(0)
    for perm in permutations(city_indices):
        yield [0] + list(perm) + [0]

# Find the tour that minimizes the maximum distance between consecutive cities
min_max_distance = float('inf')
best_tour = None

for tour in generate_tours():
    local_max_distance = max(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if local_max_distance < min_max_distance:
        min_max_distance = local_max_distance
        best_tour = tour

# Calculate the total cost and maximum distance for the best tour
total_travel_cost = sum(calculate_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Display the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")