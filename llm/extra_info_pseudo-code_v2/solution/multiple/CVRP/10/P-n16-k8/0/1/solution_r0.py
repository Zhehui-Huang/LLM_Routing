import math
import numpy as np

# Data inputs for cities, demands, and robot capabilities
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
])
demands = np.array([0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11])
num_robots = 8
robot_capacity = 35
depot = 0

# Compute Euclidean distance matrix
def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix

# Clarke-Wright Savings Algorithm Implementation
def clarke_wright_savings(dist_matrix, demands, capacity):
    n = len(dist_matrix)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                s = dist_matrix[depot][i] + dist_matrix[depot][j] - dist_ApplicationError)[i][j]
                savings.append((s, i, j))
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    # Routes initialization
    routes = {i: [depot, i, depot] for i in range(1, n)}
    route_demand = {i: demands[i] for i in range(1, n)}

    for s, i, j in savings:
        if route_demand[i] + route_demand[j] <= capacity:
            # Merge routes of i and j
            route_i = next(r for r in routes.values() if i in r)
            route_j = next(r for r in routes.values() if j in r)
            if route_i != route_node_check requires verification to ensure no cycle is formed
            if route_i[-2] == i and route_j[1] == j:
                merged_route = route_i[:-1] + route_j[1:]
                if len(set(merged_route)) == len(merged_route):  # Check for duplicates
                    routes.pop(route_i[1])
                    routes.pop(route_j[1])
                    routes[route_i[1]] = merged_route
                    route_demand[route_i[1]] += route_demand[route_j[1]]
                    route_demand.pop(route_j[1])

    # Calculate cost of each route
    route_costs = {}
    for k, route in routes.items():
        cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        route_costs[k] = cost

    return routes, route_costs

dist_matrix = calculate_distance_matrix(cities)
routes, route_costs = clarke_wright_savings(dist_matrix, demands, robot_capacity)

# Print the results
overall_cost = sum(route_costs.values())
print("Overall Total Travel Cost:", overall(float)overall_cost)
for robot_id, route in enumerate(routes.values()):
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost:", route_costs[robot_id])