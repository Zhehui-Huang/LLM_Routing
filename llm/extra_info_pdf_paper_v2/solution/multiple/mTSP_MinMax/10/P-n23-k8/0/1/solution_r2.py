import math
import random

# Given city coordinates where the index represents the city number
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Greedy partition to initialize robots' routes
def greedy_partition():
    cities = list(range(1, 23))  # Cities excluding the depot
    random.shuffle(cities)
    routes = [[] for _ in range(num_robots)]
    for city in cities:
        min_increment = float('inf')
        best_robot = 0
        for robot_index in range(num_robots):
            if routes[robot_index]:
                increase = euclidean_distance(routes[robot_index][-1], city)
            else:
                increase = euclidean_distance(0, city)
            if increase < min_increment:
                min_increment = increase
                best_robot = robot_index
        routes[best_robot].append(city)
    return routes

# Function to calculate the cost of a route
def calculate_route_cost(route):
    last_city = 0
    total_cost = 0
    for city in route:
        total_cost += euclidean_distance(last_city, city)
        last_city = city
    total_cost += euclidean_distance(last_city, 0)  # Return to the depot
    return total_cost

# Getting initial routes using a greedy heuristic
initial_routes = greedy_partition()

# Calculating route costs and determining the maximum route cost
max_travel_cost = 0
for idx, route in enumerate(initial_routes):
    complete_route = [0] + route + [0]
    route_cost = calculate_route_cost(route)
    print(f"Robot {idx} Tour: {complete_route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")
    max_travel_cost = max(max_travel_cost, route_cost)

# Outputting the maximum travel cost across all robot routes
print(f"Maximum Travel Cost: {max_travel_cost}")