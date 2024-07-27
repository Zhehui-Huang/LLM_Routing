import numpy as np
import math

# City and demand data
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

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Basic greedy closest neighbor solution to start with
def initial_solution():
    num_vehicles = 8
    vehicle_capacity = 40
    routes = [[] for _ in range(num_vehicles)]
    capacities = [0] * num_vehicles
    unvisited = list(cities.keys())[1:]  # Exclude depot
    current_city = [0] * num_vehicles
    
    for v in range(num_vehicles):
        while unvisited:
            next_city = None
            min_distance = float('inf')
            for city in unvisited:
                if distances[current_city[v]][city] < min_distance and (capacities[v] + demands[city] <= vehicle_capacity):
                    next_city = city
                    min_distance = distances[current_city[v]][city]
            if next_city is None:
                break
            routes[v].append(next_city)
            unvisited.remove(next_city)
            capacities[v] += demands[next_city]
            current_city[v] = next_city
    
    return routes, capacities

distances = calculate_distance_matrix(cities)
routes, capacities = initial_solution()

# Computing total travel costs
total_cost = 0
for idx, route in enumerate(routes):
    if route:
        route = [0] + route + [0]  # Add start and end at the depot
        cost = sum([distances[route[i]][route[i + 1]] for i in range(len(route) - 1)])
        print(f'Robot {idx} Tour: {route}')
        print(f'Robot {idx} Total Travel Cost: {cost:.2f}')
        total_cost += cost

print(f'Overall Total Travel Cost: {total_cost:.2f}')