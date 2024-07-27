import numpy as np
from itertools import permutations

# Define coordinates for each city
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute distances between all pairs of cities
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(cities[i], cities[j])

# Generate all possible choices of 8 cities including city 0
def possible_city_sets():
    from itertools import combinations
    all_cities = list(cities.keys())
    for combo in combinations(all_cities, 7):
        if 0 in combo:
            yield combo
        else:
            yield (0,) + combo

# Find shortest tour for given set of cities including returns to the depot
def find_shortest_tour(cities_set):
    min_dist = float('inf')
    shortest_path = None
    for perm in permutations(cities_set):
        if perm[0] == 0:  # start from depot
            # Calculate path distance
            dist = sum(dist_matrix[(perm[i], perm[i+1])] for i in range(len(perm) - 1))
            # Return to depot
            dist += dist_matrix[(perm[-1], 0)]
            if dist < min_dist:
                min_dist = dist
                shortest_path = perm
    return shortest_path, min_dist

# Main logic to find the best tour from all possible city sets
best_distance = float('inf')
best_tour = None
for cities_set in possible_city_set_gen():
    tour, distance = find_shortest_tour(cities_set)
    if distance < best_distance:
        best_distance = distance
        best_tour = tour + (0,)

# Output the result
print("Tour:", list(best_tour))
print("Total travel cost:", best_distance)