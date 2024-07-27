import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Demand list
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Number of robots and their capacity
n_robots = 8
capacity = 40

# Compute cost matrix using Euclidean distance
def compute_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cost_matrix[i][j] = euclidean(coords[i], coords[j])
    return cost_matrix

cost_matrix = compute_cost_matrix(coordinates)

# Clarke-Wright Savings Algorithm helper functions
def compute_savings(cost_matrix):
    n = len(cost_matrix)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                saving = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((saving, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

savings = compute_savings(cost_matrix)

# Assign routes to vehicles using Clarke-Wright Savings Algorithm
def cw_savings_algorithm(savings, demands, n_robots, capacity):
    routes = [[] for _ in range(n_robots)]
    remaining_capacity = [capacity] * n_robots
    demand_fulfilled = [0] * len(demands)

    # Initialize routes with only the depot
    for i in range(n_robots):
        routes[i].append(0)

    for saving, i, j in savings:
        for k in range(n_robots):
            if remaining_capacity[k] >= demands[i] and remaining_capacity[k] >= demands[j]:
                if (i not in routes[k]) and (j not in routes[k]):
                    routes[k].extend([i, j])
                    remaining_capacity[k] -= (demands[i] + demands[j])
                    demand_fulfilled[i] = 1
                    demand_fulfilled[j] = 1
                    break
                elif (i in routes[k]) and (j not in routes[k]) and routes[k][-1] == i:
                    routes[k].append(j)
                    remaining_capacity[k] -= demands[j]
                    demand_fulfilled[j] = 1
                    break
                elif (j in routes[k]) and (i not in routes[k]) and routes[k][-1] == j:
                    routes[k].append(i)
                    remaining_capacity[k] -= demands[i]
                    demand_fulfilled[i] = 1
                    break

    # Make sure all cities are visited
    for idx, demand in enumerate(demands[1:], 1):
        if not demand_fulfilled[idx]:  # if not visited
            for k in range(n_robots):
                if remaining_capacity[k] >= demand:
                    if routes[k][-1] != idx:
                        routes[k].append(idx)
                    remaining_capacity[k] -= demand
                    demand_fulfilled[idx] = 1
                    break

    # Close all routes returning to the depot
    for route in routes:
        if route[-1] != 0:
            route.append(0)

    return routes

routes = cw_savings_algorithm(savings, demands, n_robots, capacity)

# Calculate the total travel cost
def calculate_travel_cost(routes, cost_matrix):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += cost_matrix[route[i]][route[i + 1]]
        costs.append(route_cost)
        total_cost += route_cost
    return total_cost, costs

total_cost, individual_costs = calculate_travel_cost(routes, cost_matrix)

# Output the results
for i, (route, cost) in enumerate(zip(routes, individual_costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Myght be mistaken: {total_cost}")