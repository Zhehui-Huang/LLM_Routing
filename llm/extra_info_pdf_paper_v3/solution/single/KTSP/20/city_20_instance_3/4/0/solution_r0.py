import numpy as np
from itertools import permutations

# Cities coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Distance calculation function
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(i, j)

# Find the best tour that includes exactly 13 cities (including depot city 0)
def find_best_tour():
    min_tour = None
    min_cost = float('inf')
    cities_to_visit = list(cities.keys())[1:]  # exclude the depot from selections
    # Generate combinations of selecting 12 cities excluding depot, then add depot back
    for subset in permutations(cities_to_visit, 12):
        current_subset = [0] + list(subset)  # start and end at depot
        # Try all permutations within this subset for the shortest path
        for perm in permutations(current_subset[1:]):
            tour = [0] + list(perm) + [0]
            cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
            if cost < min_cost:
                min_cost = cost
                min_tour = tour
                
    return min_tour, min_cost

# Calling the function to calculate the best tour and cost
best_tour, best_cost = find_best_tour()

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")