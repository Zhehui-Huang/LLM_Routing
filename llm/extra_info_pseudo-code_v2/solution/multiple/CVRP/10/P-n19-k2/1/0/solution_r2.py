import numpy as np
from scipy.spatial.distance import euclidean
from itertools import product

# Data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Compute Euclidean Distance Matrix
def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i, j in product(range(n), repeat=2):
        dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = create_distance_matrix(coordinates)

# Clarke-Wright Savings Algorithm
def clarke_wright(demands, capacity, distance_matrix):
    n = len(demands)
    savings = []
    # Calculate savings
    for i in range(1, n):
        for j in range(i + 1, n):
            s = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
            savings.append((s, i, j))
    savings.sort(reverse=True)

    routes = [[i] for i in range(1, n)]
    for _, i, j in savings:
        route_i = None
        route_j = None
        for route in routes:
            if i in route:
                route_i = route
            if j in route:
                route_j = route
        if route_i is not route_j and route_i and route_j:
            if demands[route_i[0]] + demands[route_j[0]] <= capacity:
                route_i.extend(route_j)
                routes.remove(route_j)
                demands[route_i[0]] = demands[route_i[0]] + demands[route_j[0]]
    
    # Adding depot
    for route in routes:
        route.insert(0, 0)
        route.append(0)
    
    return routes
    
routes = clarke_wright(demands, robot_capacity, distance_arg_matrix)

# Assign routes to robots
def assign_routes(routes, num_robots, route_distance):
    route_costs = [(sum(route_distance[route[i], route[i+1]] for i in range(len(route)-1)), route) for route in routes]
    route_costs.sort()
    robots = [[] for _ in range(num_robots)]
    robot_costs = [0] * num_robots
    for cost, route in route_costs:
        idx = robot_costs.index(min(robot_costs))
        robots[idx].append(route)
        robot_costs[idx] += cost

    return robots, robot_costs

robots, total_costs = assign_routes(routes, num_robots, distance_matrix)

# Print robot routes and costs
def display_results(robots, total_costs):
    total_cost = sum(total_costs)
    for i, (routes, cost) in enumerate(zip(robots, total_costs)):
        print(f"Robot {i} Tour: {routes}, Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {total_cost}")

display_results(robots, total_costs)