import numpy as np
from more_itertools import chunked
from itertools import permutations
from math import sqrt

# Define city coordinates
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
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Prepare a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = calc_distance(cities[i], cities[j])

# Number of robots
num_robots = 8

# Initial simple partitioning
city_indices = list(cities.keys())[1:]  # Exclude depot city from candidates
chunks = list(chunked(city_indices, int(np.ceil(len(city_indices) / num_robots))))

# Helper function to calculate travel cost of a tour
def tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Process each robot's tour
robots_tours = []
overall_total_cost = 0

for idx, chunk in enumerate(chunks):
    tour = [0] + list(chunk) + [0]
    cost = tour_cost(tour)
    robots_tours.append((idx, tour, cost))
    overall_total_cost += cost

# Output results
for (robot, tour, cost) in robots_tours:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")