import math
from itertools import combinations

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

def calculate_savings_list(coords):
    n = len(coords)
    savings = []
    depot_distance = [euclidean_distance(coords[0][0], coords[0][1], coords[i][0], coords[i][1]) for i in range(1, n)]
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                s = depot_distance[i-1] + depot_distance[j-1] - euclidean_distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
                savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def initial_solution(savings, demands, capacity):
    routes = []
    load = {}
    for _, i, j in savings:
        if i not in load: load[i] = 0
        if j not in load: load[j] = 0
        if load[i] + demands[i-1] <= capacity and load[j] + demands[j-1] <= capacity:
            routes.append([0, i, j, 0])
            load[i] += demands[i-1]
            load[j] += demands[j-1]
    return routes

def calculate_total_cost(routes, cost_matrix):
    total_cost = 0
    for route in routes:
        cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        total_cost += cost
    return total_cost

def distribute_load(routes, robots, demands, cost_matrix):
    complete_routes = []
    for r in routes:
        capacity_used = sum(demands[city-1] for city in r if city != 0)
        if capacity_used <= robots[1]:
            complete_routes.append(r)
        else:
            # Splitting route logic if needed
            pass
    return complete_routes

# Define the problem data
coords = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
          (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
          (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000,
           900, 2500, 1800, 700]
robots = [4, 6000]  # Number of robots and capacity each

cost_matrix = calculate_cost_matrix(coords)
savings = calculate_savings_list(coords)
routes = initial_solution(savings, demands, robots[1])
overall_total_cost = calculate_total

# Output the resulting tours and costs
overall_cost = 0
for idx, route in enumerate(routes):
    route_cost = calculate_total_cost([route], cost_matrix)
    overall_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")
print(f"Overall Total Travel Cost: {overall_cost}")