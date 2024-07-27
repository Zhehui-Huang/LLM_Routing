import math
from itertools import permutations

# City coordinates
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

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c2][0] - cities[c1][0])**2 + (cities[c2][1] - cities[c1][1])**2)

# Generate all possible tours starting and ending at the depot (city 0)
num_cities = len(cities)
all_tours = permutations(range(1, num_cities))  # Generate permutations of cities 1 to 9

# Evaluate all tours to find the one with the minimum longest edge
min_max_distance = float('inf')
best_tour = None
for tour in all_tours:
    full_tour = [0] + list(tour) + [0]
    max_distance_in_tour = max(euclidean_distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
    if max_distance_in_tour < min_max_distance:
        min_max_distance = max_distance_in_tour
        best_tour = full_tour

# Calculate total travel cost of the best tour
total_travel_cost = sum(euclidean_distance(best_tour[i], best_tour[i + 1]) for i in range(len(best_tour) - 1))

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))