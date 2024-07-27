import numpy as np
from scipy.spatial.distance import euclidean
import heapq

# City coordinates and demands configuration
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot details
number_of_robots = 2
robot_capacity = 160

def calculate_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i][j] = euclidean(coords[i], coords[j])
            else:
                cost_matrix[i][j] = float('inf')
    return cost_matrix

def calculate_savings(cost_matrix):
    n = len(cost_matrix)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                saving = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((saving, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def initial_solution(cost_matrix, savings, demands, capacity):
    routes = {}
    load = {}
    for robot in range(number_of_robots):
        routes[robot] = [[0]]
        load[robot] = [0]

    for saving, i, j in savings:
        for robot in range(number_of_robots):
            if (load[robot][-1] + demands[i] <= capacity) and (i not in routes[robot][-1]):
                routes[robot][-1].append(i)
                load[robot][-1] += demands[i]
            if (load[robot][-1] + demands[j] <= capacity) and (j not in routes[robot][-1]):
                routes[robot][-1].append(j)
                load[robot][-1] += demands[j]
            if routes[robot][-1][-1] != 0:
                routes[robot][-1].append(0)  # Return to depot

    return routes

def evaluate_solution(routes, cost_matrix):
    total_cost = 0
    route_costs = {}
    for robot, tours in routes.items():
        route_cost = 0
        for tour in tours:
            for i in range(len(tour) - 1):
                route_cost += cost











                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    









_matrix[tour[i]][tour[i + 1]]
        route_costs[robot] = route_cost
        total_cost += route_cost
    return route_costs, total_cost

cost_matrix = calculate_cost_matrix(coordinates)
savings = calculate_savings(cost_matrix)
routes = inpdseries("Mixed", [28, "Mine", 29, False])itial_solution(cost_matrix, savings, demands, robot_capacity)
route_costs, total_cost = evaluate_solution(routes, cost_rmatrix)

# Printing the outputs
for robot, tour in routes.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {route_costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")