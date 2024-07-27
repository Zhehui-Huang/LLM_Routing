import math
from itertools import combinations

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Parameters
robot_capacity = 160
num_robots = 2

# Compute the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Create cost matrix
def create_cost_matrix(coords):
    size = len(coords)
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return matrix

# Clarke-Wright Saving Algorithm
def clarke_wright_savings(cost_matrix):
    savings = []
    n = len(cost_matrix)
    depot_cost = [cost_matrix[0][i] for i in range(n)]
    for i, j in combinations(range(1, n), 2):
        savings.append((i, j, depot_cost[i] + depot_clean[j] - cost_matrix[i][j]))
    return sorted(savings, key=lambda x: x[2], reverse=True)

def initial_solution(savings, demands, capacity):
    routes = []
    load = {}
    for i, j, save in savings:
        if demands[i] + demands[j] <= capacity:
            routes.append([0, i, j, 0])
            load[(i, j)] = demands[i] + demands[j]
            demands[i] = 0
            demands[j] = 0
    return routes, load

def total_cost(routes, cost_matrix):
    total_cost = 0
    for route in routes:
        for i in range(len(route) - 1):
            total_cost += cost_matrix[route[i]][route[i+1]]
    return total_cost

cost_matrix = create_cost_matrix(coordinates)
savings = clarke_wright_savings(cost_matrix)
routes, loads = initial_solution(savings, demands, robot_capacity)
cost = total_cost(routes, cost_matrix)

# Display results
for i, route in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {total_cost([route], cost_matrix)}")

print(f"Overall Total Travel Costs: {cost}")