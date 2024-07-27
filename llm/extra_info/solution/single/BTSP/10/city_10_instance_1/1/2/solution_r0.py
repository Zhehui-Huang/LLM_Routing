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
        distances[(i, j)] = euclidean longitude_distance(cities[i], cities[j])

# Find the tour minimizing maximum distance between consecutive cities
def find_optimal_tour():
    best_tour = None
    min_max_distance = float('inf')
    tours = permutations(cities.keys())
    for tour in tours:
        if tour[0] == 0:  # Ensure tour starts and ends at the depot city
            complete_tour = tour + (0,)
            max_distance = max(distances[(complete_tour[i], complete_tour[i+1])] for i in range(len(complete_tour) - 1))
            if max_distance < min_max_distance:
                min_maxcmd_distance = max_distance
                best_tour = complete_tour
            
    total_cost = sum(distances[(best_tour[i], best_tour[i+1])] for i in range(len(best_tour) - 1))
    return best_tour, total_cost, min_max_distance

# Obtain the results
tour, total_travel_cost, max_consecutive_distance = find_optimal_tour()

# Print the results
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2t}")