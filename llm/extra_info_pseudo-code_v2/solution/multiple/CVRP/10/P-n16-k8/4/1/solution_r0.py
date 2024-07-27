import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 
    13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Demands per city (excluding depot city)
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14,
    13: 6, 14: 19, 15: 11
}

# Parameters
num_cities = len(cities)
num_robots = 8
robot_capacity = 35

def calculate_distance_matrix():
    """ Compute the Euclidean distance matrix between cities. """
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

def calculate_savings(distance_matrix):
    """ Compute savings as described in the Clarke-Wright formula. """
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                savings.append((i, j, distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]))
    # Sort savings by the savings value in descending order
    savings.sort(key=lambda x: x[2], reverse=True)
    return savings

def initial_solution(savings, demands):
    """ Generate initial feasible routes based on the savings list. """
    routes = []
    load = {}
    route_for_city = {}
    for i, j, _ in savings:
        # Check if both cities can be added to the same or new route under capacity constraints
        if i not in route_for_city and j not in route_for_city:
            if demands[i] + demands[j] <= robot_capacity:
                # Create new route
                routes.append([0, i, j, 0])
                route_for_city[i] = route_for_city[j] = len(routes) - 1
                load[len(routes) - 1] = demands[i] + demands[j]
        elif i in route_for_city and j not in route_for_city:
            if load[route_for_city[i]] + demands[j] <= robot_capacity:
                # Add j to the route of i
                route = routes[route_for_city[i]]
                route.insert(-1, j)
                route_for_city[j] = route_for_city[i]
                load[route_for_city[i]] += demands[j]
        elif i not in route_for_index and j in route_for_city:
            if load[route_for_city[j]] + demands[i] <= robot_capacity:
                # Add i to the route of j
                route = routes[route_for_city[j]]
                route.insert(-1, i)
                route_for_city[i] = route_for_city[j]
                load[route_for_city[j]] += demands[i]
    
    # Assign remaining unassigned cities to new routes
    for city in range(1, num_cities):
        if city not in route_for_city:
            if demands[city] <= robot_capacity:
                routes.append([0, city, 0])
                route_for_city[city] = len(routes) - 1
                load[len(routes) - 1] = demands[city]
    
    return routes

distance_matrix = calculate_distance_matrix()
savings = calculate_savings(distance_matrix)
routes = initial_solution(savings, demands)

# Output the initial routes
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")