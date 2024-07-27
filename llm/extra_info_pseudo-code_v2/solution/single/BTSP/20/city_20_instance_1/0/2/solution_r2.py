import math
import sys
from itertools import permutations

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_bottleneck_tsp(cities):
    # Calculate the distances between all city pairs
    num_cities = len(cities)
    distances = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_distance(cities[i], cities[j])

    # Trying all permutations to find the one with the minimum maximum edge length
    min_max_distance = sys.maxsize
    best_tour = None

    all_permutations = permutations(range(1, num_cities))  # Exclude the depot which is city 0
    for perm in all_permutations:
        # Generate the tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        max_dist_in_tour = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_dist_in_tour < min_max_distance:
            min_max_distance = max_dist_in_tour
            best_tour = tour

    # Calculate the total travel cost for the best tour
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

    return best_tour, total_cost, min_max_distance

# Coordinates of the cities: depot position included as city 0
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

tour, total_travel_cost, max_distance = find_bottleneck_tsp(cities)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")