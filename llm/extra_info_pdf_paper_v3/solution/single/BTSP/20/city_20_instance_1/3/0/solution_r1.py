import math
from itertools import permutations

# Coordinates of the depot and the cities
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the tour minimizing the longest distance between any two consecutive cities
def find_best_tour():
    n = len(coordinates)
    best_tour = None
    minimal_longest_edge = float('inf')
    minimal_total_cost = float('inf')

    # Generate all possible tours (permutations of cities, excluding the depot)
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        longest_edge = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            edge_cost = distance(tour[i], tour[i+1])
            total_cost += edge_cost
            if edge_cost > longest_edge:
                longest_edge = edge_cost

        if longest_edge < minimal_longest_edge or (longest_edge == minimal_longest_edge and total_cost < minimal_total_cost):
            minimal_longest_edge = longest_edge
            minimal_total_cost = total_cost
            best_tour = tour

    return best_tour, minimal_total_cost, minimal_longest_edge

# Calculate the optimal tour and parameters
best_tour, total_cost, max_consecutive_distance = find_best_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")