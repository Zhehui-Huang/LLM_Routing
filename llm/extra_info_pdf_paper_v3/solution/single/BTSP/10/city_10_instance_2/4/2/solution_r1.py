import itertools
from math import sqrt

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all permutations of cities excluding the depot city
city_indices = list(cities.keys())
city_indices.remove(0)  # Exclude the depot city for initial permutations 

# Iterate over permutations to find the tour minimizing the maximum distance between consecutive cities
best_max_distance = float('inf')
best_tour = None

for permutation in itertools.permutations(city_indices):
    current_tour = [0] + list(permutation) + [0]
    max_dist = max(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
    if max_dist < best_max_distance:
        best_max_distance = max_dist
        best_tour = current_tour

# Calculate total travel cost
total_cost = sum(euclidean_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Output the tour, total travel cost, and maximum distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")