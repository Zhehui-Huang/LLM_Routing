import math
from itertools import permutations

# Define city coordinates
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

# Compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute all pairwise city distances
distances = {
    (i, j): euclidean_distance(i, j)
    for i in cities.keys()
    for j in cities.keys() if i != j
}

# Brute force TSP solution to find minimum bottleneck tour (not optimal in general for large n)
def find_min_bottleneck_tsp():
    min_bottleneck = float('inf')
    best_tour = None
    all_permutations = permutations(cities.keys() - {0})  # Exclude depot initially, add at the beginning and end later
    for perm in all_permutations:
        # Add depot city in the beginning and the end
        tour = [0] + list(perm) + [0]
        # Find the maximum distance in the current tour
        max_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        if max_distance < min_bottleneck:
            min_bottleneck = max_distance
            best_tour = tour
    # Calculate total travel cost
    total_travel_cost = sum(distances[best_tour[i], best_tour[i + 1]] for i in range(len(best_tour) - 1))
    return best_tour, total_travel_cost, min_bottleneck

# Find the optimal tour based on the defined approach
tour, total_cost, max_distance = find_min_bottleneck_tsp()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)