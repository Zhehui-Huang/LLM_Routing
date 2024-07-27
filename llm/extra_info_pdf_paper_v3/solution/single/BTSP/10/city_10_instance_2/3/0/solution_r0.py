import itertools
import math
from sys import maxsize

# Coordinates of the cities
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

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

def find_minimal_tour():
    # Calculation block using permutations - ideally we use more efficient approaches for bigger problems
    city_indices = list(cities.keys())[1:]  # Exclude the depot for permutations
    min_tour = None
    min_cost = maxsize
    min_max_distance = maxsize

    # Explore all permutations of the cities
    for perm in itertools.permutations(city_indices):
        current_tour = [0] + list(perm) + [0]
        total_cost, max_distance = calculate_total_distance(current_tour)
        
        # Check if this permutation offers a better maximum distance
        if max_distance < min_max_cost:
            min_tour = current_tour
            min_cost = total_cost
            min_max_distance = max_distance

    return min_tour, min_cost, min_max_distance

# Obtain the optimal tour, total cost and maximum distance between consecutive cities
optimal_tour, total_cost, max_distance = find_minimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")