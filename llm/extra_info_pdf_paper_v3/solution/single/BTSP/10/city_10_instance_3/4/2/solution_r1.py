import math
from itertools import permutations

# Given city coordinates (index represents city number)
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all possible city visit orders (excluding the depot city, which is start and end)
city_indices = list(range(1, len(cities)))  # Exclude the depot 0 for permutation
all_tours = permutations(city_indices)

best_tour = None
min_max_distance = float('inf')
total_min_cost = float('inf')

# Evaluate each possible tour
for perm in all_tours:
    # Include the depot at start and end
    tour = [0] + list(perm) + [0]
    max_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    # Check if this permutation gives a better maximum segment distance
    if max_distance < min_max_distance:
        min_max_max_distance = max_distance
        total_min_cost = total_cost
        best_tour = tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_min_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")