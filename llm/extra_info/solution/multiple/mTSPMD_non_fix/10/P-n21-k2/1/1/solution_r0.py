import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Definition of cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Compute the distance matrix between all pairs of cities
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Simple heuristic: Assign a subset of cities to each robot
# Robot 0 starts at depot 0, Robot 1 starts at depot 1
# For simplicity split by even and odd indices, excluding the depots themselves
robot0_cities = [0] + [i for i in range(2, num_cities, 2)]
robot1_cities = [1] + [i for i in range(3, num_cities, 2)]

# Function to compute the cost of a given tour
def calculate_total_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Function to find the shortest path tour using permutations (not efficient but simple for demonstration)
def find_best_tour(start_city, cities, distance_matrix):
    min_tour = None
    min_cost = float('inf')
    for perm in permutations(cities):
        total_cost = distance_matrix[start_city, perm[0]] + calculate_total_tour_cost(list(perm), distance_matrix)
        if total_cost < min_cost:
            min_tour = [start_city] + list(perm)
            min_cost = total_cost
    return min_tour, min_cost

# Find tours for both robots
tour0, cost0 = find_best_tour(0, robot0_cities[1:], distance_matrix)
tour1, cost1 = find_best_tour(1, robot1_cities[1:], distance_matrix)

overall_total_cost = cost0 + cost1

# Print the results
print(f"Robot 0 Tour: {tour0}")
print(f"Robot 0 Total Travel Cost: {cost0}\n")
print(f"Robot 1 Tour: {tour1}")
print(f"Robot 1 Total Travel, Cost: {cost1}\n")
print(f"Overall Total Travel Cost: {overall_total_cost}")