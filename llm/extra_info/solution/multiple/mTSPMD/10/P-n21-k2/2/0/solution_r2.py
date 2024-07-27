import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the coordinates for the cities
cities_coordinates = {
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

# Calculating the distance using Euclidean formula
def calculate_distances(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i, j] = euclidean(cities[i], cities[j])
    return distance_matrix

distances = calculate_distances(cities_coordinates)

# Function to find the best tour starting and ending at a given depot
def find_best_route(cities, depot):
    min_cost = float('inf')
    best_route = None
    non_depot_cities = list(cities.keys())
    non_depot_cities.remove(depot)

    for perm in permutations(non_depot_cities):
        route = [depot] + list(perm) + [depot]
        cost = sum(distances[route[i], route[i+1]] for i in range(len(route) - 1))
        if cost < min_cost:
            min_cost = cost
            best_route = route
            
    return best_route, min_cost

# The tours for each robot, assuming Robot 0 starts at depot 0 and Robot 1 at depot 1
robot_0_tour, robot_0_cost = find_best_route(cities_coordinates, 0)
robot_1_tour, robot_1_cost = find_best_route(cities_coordinates, 1)

# Calculating overall cost
overall_cost = robot_0_cost + robot_1_cost

# Output required results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("\nRobot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("\nOverall Total Travel Cost:", overall_cost)