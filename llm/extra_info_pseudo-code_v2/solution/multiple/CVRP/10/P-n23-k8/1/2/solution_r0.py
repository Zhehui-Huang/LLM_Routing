import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

def calculate_cost_matrix(cities):
    n = len(cities)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean(cities[i], cities[j])
    return matrix

def calculate_savings(cost_matrix):
    n = len(cost_matrix)
    savings = {}
    for i in range(1, n):
        for j in range(i+1, n):
            savings[(i, j)] = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
    return savings

def cw_algorithm(cities, demands, capacity, cost_matrix, savings):
    routes = []
    assignments = {i: None for i in range(1, len(cities))}  # city to route assignment
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    for (i, j), saving in sorted_savings:
        if assignments[i] is None and assignments[j] is None:
            if demands[i] + demands[j] <= capacity:
                routes.append([0, i, j, 0])
                assignments[i], assignments[j] = len(routes) - 1, len(routes) - 1
    
    for i in range(1, len(cities)):
        if assignments[i] is None:
            if demands[i] <= capacity:
                routes.append([0, i, 0])
                assignments[i] = len(routes) - 1

    # Check and reassign to appropriate vehicles with remaining capacity
    return routes

def calculate_route_cost(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

def main():
    cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
              (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
              (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
    demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
    capacity = 40
    cost_matrix = calculate_cost_matrix(cities)
    savings = calculate_savings(cost_matrix)
    routes = cw_algorithm(cities, demands, capacity, cost_matrix, savings)
    
    total_cost = 0
    for i, route in enumerate(routes):
        route_cost = calculate_route_cost(route, cost_matrix)
        total_cost += route_cost
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {route_enable[i]}")
    
    print(f"Overall Total Travel Cost: {total_cost}")

if __name__ == "__main__":
    main()