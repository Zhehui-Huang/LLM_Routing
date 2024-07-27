import math

# Data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35
num_cities = len(coordinates)

# Calculate Euclidean distance matrix
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] 
                   for i in range(num_cities)]

# Simple Greedy Initial Solution Construction
def greedy_initial_solution():
    unvisited = set(range(1, num_cities))
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [robot_capacity] * num_robots
    
    for vehicle in range(num_robots):
        current_city = 0
        route_complete = False
        
        while not route_complete:
            possible_next_cities = [(distance_matrix[current_city][j], j) for j in unvisited if demands[j] <= capacity_remaining[vehicle]]
            if not possible_next_cities:
                route_complete = True
                continue

            # Choose the closest feasible city
            _, next_city = min(possible_next_cities)
            routes[vehicle].append(next_city)
            capacity_remaining[vehicle] -= demands[nextCity]
            current_city = next_city
            unvisited.remove(next_city)

        if routes[vehicle]:
            routes[vehicle] = [0] + routes[vehicle] + [0]
    
    return routes

# Calculate total cost of tours
def calculate_total_cost(routes):
    total_cost = 0
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += distance_matrix[route[i]][route[i + 1]]
        total_cost += route_cost
        print(f"Robot {routes.index(route)} Tour: {route}")
        print(f"Robot {routes.index(route)} Total Travel Cost: {route_cost}")
    return total_cost

# Generating the initial greedy solution
routes = greedy_initial_solution()

# Calculate and print the total cost
overall_total_cost = calculate_total_cost(routes)
print(f"Overall Total Travel Cost: {overall_total_cost}")