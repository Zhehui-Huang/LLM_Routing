from math import sqrt
from itertools import combinations, permutations

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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of four cities (excluding the depot 0)
city_indices = list(cities.keys())[1:]  # get [1, 2, 3, ..., 9]
combinations_of_cities = list(combinations(city_indices, 4))

# Find the shortest tour through combinations
shortest_tour = None
min_cost = float('inf')

# Go through each combination
for combination in combinations_of_cities:
    # Compose the current route including the depot
    current_combination = tuple([0]) + combination
    # Check all permutations of chosen cities to determine the shortest path
    for perm in permutations(current_combination[1:]):
        tour = tuple([0]) + perm + tuple([0])  # Make it a round trip
        total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if total_cost < min_cost:
            min_cost = total_cost
            shortest_tour = tour

# Output results
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {min_cost:.2f}")