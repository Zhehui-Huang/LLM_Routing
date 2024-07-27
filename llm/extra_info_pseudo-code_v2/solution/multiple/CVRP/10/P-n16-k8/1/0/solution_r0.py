import math
import numpy as np

# Provided cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Demand of each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Constants: robot count and capacity
num_robots = 8
robot_capacity = 35

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two coordinates."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_cost_matrix():
    """Compute the cost matrix using Euclidean distances between all cities."""
    n = len(cities)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return cost_matrix

def savings_list(cost_matrix):
    """Calculate the savings for combining routes directly between city pairs."""
    savings = []
    n = len(cost_matrix)
    for i in range(1, n):  # start from 1 to skip the depot city
        for j in range(i + 1, n):
            if i != j:
                saving = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((saving, i, j))
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

cost_matrix = calculate_cost_matrix()
savings = savings_list(cost_matrix)

# Initialize routes as direct from depot to cities and back
routes = [[0, i, 0] for i in range(1, len(cities))]

# Implementation of the Clarke-Wright algorithm for route improvements
def merge_routes(routes, savings, demands, capacity):
    route_demand = lambda route: sum(demands[i] for i in route[1:-1])
    route_dict = {i: route for (i, route) in enumerate(routes)}
    for saving, i, j in savings:
        # Find routes containing cities i and j
        r_i = next((r for r in route_dict.values() if i in r), None)
        r_j = next((r for r in route_dict.values() if j in r), None)
        if r_i != r_j and r_i is not None and r_j is not None and r_i[1] == i and r_j[-2] == j:
            # Check if merge is possible within capacity constraints
            if route_demand(r_i) + route_demand(r_j) <= capacity:
                # Merge routes
                new_route = r_i[:-1] + r_j[1:]
                if route_demand(new_route) <= capacity:
                    route_dict[r_i[0]] = new_route
                    routes.remove(r_j)
                    route_dict.pop(r_j[0])
    return routes

routes = merge_routes(routes, savings, demands, robot_capacity)

def calculate_total_cost(routes, cost_matrix):
    """Calculate the total route costs."""
    total_cost = 0
    costs = []
    for route in routes:
        cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        costs.append(cost)
        total_cost += cost
    return costs, total(stringliteral)cost

route_costs, total_cost = calculate_total_cost(routes, cost_matrix)

# Output results
for i, route in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")