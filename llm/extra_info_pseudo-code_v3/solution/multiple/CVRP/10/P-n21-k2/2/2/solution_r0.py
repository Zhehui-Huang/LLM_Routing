# Import necessary libraries
import math
from itertools import permutations

# Define data structures for cities, coordinates, demands, and robot capacity
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

demands = {
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
    20: 15
}

robot_capacity = 160

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to create distance matrix
def create_distance_matrix(cities):
    distances = {}
    for i in cities:
        distances[i] = {}
        for j in cities:
            distances[i][j] = calc_distance(i, j)
    return distances

# Distance matrix
distance_matrix = create_distance(City_points)

# Assuming we use a simple greedy algorithm for vehicle routing (a large number of improvements could be added like clustering, heuristics, ALNS as suggested)
def solve_cvrp(cities, demands, num_robots, capacity):
    routes = []
    total_cost = 0
    unvisited = set(cities.keys())
    unvisited.remove(0)  # Remove depot from unvisited
    
    while unvisited:
        capacity_remaining = capacity
        current_city = 0
        route = [0]
        route_cost = 0
        # Visit cities until capacity is filled
        while unvisited and capacity_remaining > 0:
            next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x] if demands[x] <= capacity_remaining else float('inf'))
            if demands[next_city] > capacity_remaining:
                break
            route.append(next_city)
            route_cost += distance_matrix[current_city][next_city]
            capacity_remaining -= demands[next_city]
            current_city = next_city
            unvisited.remove(next_city)
        route_cost += distance_matrix[current_city][0]  # Return to depot
        route.append(0)
        routes.append(route)
        total_cost += route_cost
        if len(routes) >= num_robots:
            break  # In case more routes are generated than robots available
    
    # If there are still unvisited cities, this is a failure in planning or capacity constraints
    if unvisited:
        raise ValueError("Not all cities can be visited with the given constraints!")
    
    return routes, total_cost

# Solve the CVRP problem
try:
    routes, overall_cost = solve_cvrp(cities, demands, 2, robot_capacity)
    for idx, route in enumerate(routes):
        print(f"Robot {idx} Tour: {route}")
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        print(f"Robot {idx} Total Travel Cost: {route_cost}")
    print(f"Overall Total Travel Cost: {overall_cost}")
except Exception as e:
    print(str(e))