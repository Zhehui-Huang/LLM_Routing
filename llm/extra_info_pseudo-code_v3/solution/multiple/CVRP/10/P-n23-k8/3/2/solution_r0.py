import numpy as np
import math
from itertools import permutations

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

demands = {
    0: 0,
    1: 7,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 19,
    7: 15,
    8: 28,
    9: 8,
    10: 8,
    11: 7,
    12: 14,
    13: 6,
    14: 19,
    15: 11,
    16: 12,
    17: 26,
    18: 17,
    19: 6,
    20: 15,
    21: 5,
    22: 10
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

def create_initial_solution(cities, distance_matrix, demands, num_vehicles, vehicle_capacity):
    unvisited = set(cities.keys()) - {0}
    routes = []
    capacities = [0] * num_vehicles
    current_location = [0] * num_vehicles
    routes = [[] for _ in range(num_vehicles)]
    
    for v in range(num_vehicles):
        routes[v].append(0)  # Start at the depot
    
    while unvisited:
        for v in range(num_vehicles):
            if not unvisited:
                break
            # Find nearest unvisited city that doesn't violate load constraints
            next_city = None
            min_dist = float('inf')
            for city in unvisited:
                if distances[current_location[v]][city] < min_dist and (capacities[v] + demands[city] <= vehicle_capacity):
                    next_city = city
                    min_dist = distances[current_location[v]][city]
            if next_city is not None:
                routes[v].append(next_city)
                capacities[v] += demands[next_city]
                current_location[v] = next_city
                unvisited.remove(next_city)
        for v in range(num_vehicles):
            routes[v].append(0)  # Return to depot
    return routes

# Choose 8 vehicles and 40 capacity each
num_vehicles = 8
vehicle_capacity = 40
initial_solution = create_initial_solution(cities, distance_matrix, demands, num_vehicles, vehicle_capacity)

# Output information (simplified display)
for idx, route in enumerate(initial_solution):
    print(f'Robot {idx} Tour: {route}')
    cost = sum([distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1)])
    print(f'Robot {idx} Total Travel Cost: {cost:.2f}')