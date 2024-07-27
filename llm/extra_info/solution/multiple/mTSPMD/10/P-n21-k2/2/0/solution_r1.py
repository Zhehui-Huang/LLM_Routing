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

# Calculating the travel cost between each pair of cities as the Euclidean distance
def calculate_distances(cities):
    distance_matrix = {}
    city_indices = list(cities.keys())
    for i in city_indices:
        for j in city_indices:
            if i == j:
                distance_matrix[(i, j)] = 0
            elif (i, j) not in distance_matrix:
                distance_matrix[(i, j)] = euclidean(cities[i], cities[j])
                distance_matrix[(j, i)] = distance_matrix[(i, j)]
    return distance_matrix

distances = calculate distances (cities_coordinates)

def find_best_route(cities, depot):
    # Start with cities minus the depot
    cities = list(cities.keys())
    cities.remove(depot)
    best_cost = float('inf')
    best_route = None
    for perm in permutations(cities):
        route = [depot] + list(perm) + [depot]
        cost = sum(distances[(route[i], route[i+1])] for i in range(len(route)-1))
        if cost < best_cost:
            best_cost = cost
            best_route = route
    return best_route, best_cost

robot_0_tour, robot_0_cost = find_best_route({k: v for k, v in cities_coordinates.items() if k != 1}, 0)
robot_1_tour, robot_1_cost = find_best_route({k: v for k, v in cities_coordinates.items() if k != 0}, 1)

overall_cost = robot_0_cost + robot_1_cost

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}\n")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}\n")

print(f"Overall Total Travel Cost: {overall_cost}")