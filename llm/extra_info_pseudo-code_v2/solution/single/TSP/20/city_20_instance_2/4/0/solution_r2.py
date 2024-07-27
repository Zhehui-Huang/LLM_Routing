import math
from itertools import permutations

# Define cities coordinates indexed from 0 (depot) to 19
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two points.
    Args:
        c1, c2 (tuple): Coordinates of two cities (x1, y1) and (x2, y2).

    Returns:
        float: Euclidean distance between two points given.
    """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Precompute distance matrix for all city pairs
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def calculate_total_tour_cost(tour):
    """ Calculate the cost of given tour based on distance matrix.
    Args:
        tour (list): List of city indices representing tour order.

    Returns:
        float: Total cost of the tour.
    """
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Generate all permutations of city indices except for the depot (0)
city_indices = list(range(1, len(cities)))  # cities 1 through 19
shortest_tour = None
min_cost = float('inf')

# Iterate through all possible tours, adding the depot (0) at the start and end
for perm in permutations(city_indices):
    curr_tour = [0] + list(perm) + [0]
    curr_cost = calculate_total_tour_step(curr_tour)
    if curr_cost < min_cost:
        min_cost = curr_cost
        shortest_tour = curr_tour

# Output the best tour and the cost of that tour
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)