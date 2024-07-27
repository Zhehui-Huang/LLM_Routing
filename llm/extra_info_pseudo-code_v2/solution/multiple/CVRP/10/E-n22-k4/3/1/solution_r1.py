import math
from collections import defaultdict

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_cost_matrix(coords):
    n = len(coords)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
            matrix[i][j] = matrix[j][i] = distance
    return matrix

def calculate_savings_list(coords, demands):
    n = len(coords)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                savings.append(((euclidean_distance(coords[0][0], coords[0][1], coords[i][0], coords[i][1]) +
                                 euclidean_distance(coords[0][0], coords[0][1], coords[j][0], coords[j][1]) -
                                 euclidean_distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])), i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def construct_tours(cost_matrix, savings, demands, capacity):
    n = len(demands)
    routes = []
    load = {}
    used = [False] * n

    while savings:
        s, i, j = savings.pop(0)
        if not used[i] and not used[j] and demands[i] + demands[j] <= capacity:
            route = [0, i, j, 0]
            load_current = demands[i] + demands[j]
            used[i] = used[j] = True
            # Try to add more cities to the route while respecting capacity constraints
            improvements = True
            while improvements:
                improvements = False
                for k in range(1, n):
                    if not used[k] and load_current + demands[k] <= capacity:
                        last_city = route[-2]
                        if euclidean_distance(coords[last_city][0], coords[last_city][1],
                                              coords[k][0], coords[k][1]) < euclidean_distance(coords[last_city][0],
                                                                                               coords[last_city][1],
                                                                                               coords[0][0], coords[0][1]):
                            route.insert(-1, k)
                            load_current += demands[k]
                            used[k] = True
                            improvements = True
            routes.append(route)

    return routes

def calculate_route_cost(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Define problem data
coords = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
          (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
          (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000,
           900, 2500, 1800, 700]
capacity = 6000

cost_matrix = calculate_cost_matrix(coords)
savings = calculate_savings_list(coords, demands)
routes = construct_tours(cost_matrix, savings, demands, capacity)

# Print routes and costs
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = calculate_route_cost(route, cost_matrix)
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Crest: {total_cost}")