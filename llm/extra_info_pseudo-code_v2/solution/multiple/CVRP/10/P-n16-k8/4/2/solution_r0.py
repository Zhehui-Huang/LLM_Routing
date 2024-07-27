import math
from itertools import combinations

# City data
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

num_cities = len(coords)
num_robots = 8
robot_capacity = 35

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute the cost matrix
def compute_cost_matrix():
    return [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Compute savings (S_ij = C_i0 + C_0j - C_ij)
def compute_savings(cost_matrix):
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            saving = cost_matrix[i][0] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((saving, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])  # Sort savings in descending order
    return savings

# Generate initial solution based on savings
def generate_initial_solution(savings, demands, robot_capacity):
    routes = []
    load = [0] * num_robots
    for _, i, j in savings:
        if demands[i] <= robot_capacity and demands[j] <= robot_capacity:
            routes.append([0, i, j, 0])
            load.append(demands[i] + demands[j])
            demands[i] = demands[j] = 0  # Mark as serviced
    return routes

# Calculate total travel cost for a given route
def calculate_route_cost(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Main function to solve the CVRP
def solve_cvrp():
    cost_matrix = compute_cost_matrix()
    savings = compute_savings(cost_matrix)
    routes = generate_initial_solution(savings, demands, robot_capacity)
    
    total_cost = 0
    for idx, route in enumerate(routes):
        route_cost = calculate_route_cost(route, cost_matrix)
        total_cost += route_cost
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {route_adj_cost}")
    
    print(f"Overall Total Travel Cost: {total_cost}")

# Run the solver
solve_cvrp()