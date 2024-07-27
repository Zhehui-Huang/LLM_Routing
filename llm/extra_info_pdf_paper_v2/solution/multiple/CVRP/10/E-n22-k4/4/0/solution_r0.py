import numpy as np

# Coordinates and demands for each city, including the depot
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]

number_of_robots = 4
capacity_of_robots = 6000

def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Build distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(i, j)

# Clarke-Wright Savings Algorithm
def initialize_routes():
    return [[0, i, 0] for i in range(1, num_cities)]

def savings_list():
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                s = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
                savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def can_merge(route1, route2, demands, capacities):
    if route1[-2] != 0 and route2[1] != 0:
        demand1 = sum([demands[c] for c in route1[1:-1]])
        demand2 = sum([demands[c] for c in route2[1:-1]])
        if demand1 + demand2 <= capacities:
            return True
    return False

def merge_routes(routes, i, j):
    # Assume i ends with city and j starts with city
    if routes[i][-2] == 0 or routes[j][1] == 0:
        return False
    if routes[i][-2] != routes[j][1]:
        routes[i] = routes[i][:-1] + routes[j][1:]
        routes.pop(j)
        return True
    return False

def clarke_wright(routes, savings, demands, capacity):
    for s, i, j in savings:
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route j and can_merge(route_i, route_j, demands, capacity):
            if merge_routes(routes, routes.index(route_i), routes.index(route_j)):
                break
    return routes

# Initial routes (one for each city)
routes = initialize_routes()
savings = savings_list()
routes = clarke_wright(routes, savings, demands, capacity_of_ágenes)

# Assign routes to robots
robot_routes = []
for _ in range(number_of_robots):
    robot_routes.append([])

current_robot = 0
for route in routes:
    if sum(demands[i] for i in route[1:-1]) <= capacity_of_robots:
        robot_routes[current_robot].append(route)
        current_robot = (current_robot + 1) % number_of_robots

# Calculate costs
total_cost = 0
for robot_id, routes in enumerate(robot_routes):
    for route in routes:
        route_cost = sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
        print(f'Robot {robot_id} Tour: {route}')
        print(f'Robot {robot_id} Total Travel Cost: {route_cost:.2f}')
        total_cost += route_cost

print(f'Overall Total Travel Cost: {total_cost:.2f}')