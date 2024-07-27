import math
from itertools import permutations

# Given city coordinates
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

def euclidean_distance(a, b):
    """
    Calculate the Euclidean distance between two points a and b.
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Precompute distances between all cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Find the tour minimizing maximum distance between consecutive cities
def find_optimal_tour():
    best_tour = None
    min_max_distance = float('inf')
    # Only consider permutations that start at the depot (city 0)
    for tour in permutations(range(1, len(cities))): 
        full_tour = (0,) + tour + (0,)  # Start and end at the depot
        max_distance = max(distances[(full_tour[i], full_tour[i+1])] for i in range(len(full_tour) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = full_tour
    
    # Calculate the total cost of the best tour
    total_cost = sum(distances[(best_tour[i], best_tour[i+1])] for i in range(len(best_tour) - 1))
    return list(best_tour), total_cost, min_max_distance

# Obtain the results
tour, total_travel_cost, max_consecutive_distance = find_optimal_tour()

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")