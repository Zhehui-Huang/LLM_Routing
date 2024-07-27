import math
from itertools import permutations

# Cities' coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Demand of each city
demands = [
    0, 7, 30, 16, 23,
    11, 19, 15, 28, 8,
    8, 7, 14, 6, 19,
    11, 12, 26, 17, 6,
    15, 5, 10
]

# Robot parameters
num_robots = 8
capacity = 40

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_cost(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return total_distance

def is_feasible(route, demands, capacity):
    current_load = 0
    for city in route:
        current_load += demands[city]
        if current_load > capacity:
            return False
    return True

def calculate_routes(demands, capacity):
    unvisited = list(range(1, len(demands)))
    routes = []

    while unvisited:
        route = [0]  # start from the depot
        load = 0
        
        for city in list(unvisited):
            if load + demands[city] <= capacity:
                route.append(city)
                load += demands[city]
                unvisited.remove(city)
        
        route.append(0)  # return to depot
        routes.append(route)

    return routes

# Generate initial naive solution
routes = calculate_routes(demands, capacity)

# Assign routes to robots (simple round-robin distribution for example)
robot_tours = {i: [] for i in range(num_robots)}
i = 0
for route in routes:
    robot_tours[i % num_robots].extend(route)
    i += 1

# Calculating costs for each robot and total cost
total_cost = 0
for i in range(num_robots):
    tour_cost = calculate_cost(robot_tours[i])
    total_cost += tour_cost
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")