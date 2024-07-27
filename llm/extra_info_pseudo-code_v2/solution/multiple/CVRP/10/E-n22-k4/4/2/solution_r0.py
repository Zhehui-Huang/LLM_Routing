import numpy as np
import itertools

# City coordinates and demands
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

num_robots = 4
robot_capacity = 6000

# Function to compute Euclidean distance
def compute_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute distance matrix
n_cities = len(cities)
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i, j] = compute_distance(cities[i], cities[j])

# Clarke-Wright Savings Algorithm adapted for CVRP
def savings_list(dist_matrix, depot=0):
    savings = []
    for i in range(1, n_cities):
        for j in range(i + 1, n_cities):
            s = dist_matrix[depot, i] + dist_matrix[depot, j] - dist_matrix[i, j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])  # Sort savings in descending order
    return savings

# Implementing Clarke-Wright algorithm with probabilistic enhancements
def clarke_wright():
    routes = {i: [0, i, 0] for i in range(1, n_cities)}
    load = {i: demands[i] for i in range(1, n_cities)}
    savings = savings_list(dist_matrix)
    
    # Merging routes with savings consideration
    for s, i, j in savings:
        if route_merge_possible(routes[i], routes[j], load, demands, robot_capacity):
            routes[i] = merge_routes(routes[i], routes[j])
            load[i] += load[j]
            del routes[j], load[j]
    
    return routes

# Function to merge routes
def route_merge_possible(route1, route2, load, demands, capacity):
    if route1[-2] == route2[1] or route2[-2] == route1[1]:
        if load[route1[1]] + load[route2[1]] <= capacity:
            return True
    return False

def merge_routes(route1, route2):
    if route1[-2] == route2[1]:
        return route1[:-1] + route2[1:]
    elif route2[-2] == route1[1]:
        return route2[:-1] + route1[1:]
    return route1

# Calculating the costs and creating initial routes
initial_routes = clarke_wright()
route_costs = {key: sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1)) for key, route in initial_routes.items()}
total_cost = sum(route_costs.values())

# Display the routes and costs
for robot_id, route in enumerate(list(initial_routes.values())[:num_robots]):
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_costs[robot_id]}")

print(f"Overall Total Travel Cost: {total_cost}")