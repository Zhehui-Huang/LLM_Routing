import numpy as np
from math import sqrt, inf

# Step 1: Define cities, demands, and robots
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
num_robots = 8

# Step 2: Compute Euclidean distance between cities
def distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Generate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = distance(cities[i], cities[j])

# Step 3: Clarke-Wright Savings algorithm
def calculate_savings():
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            s = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
            savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings_list = calculate_savings()

# Initialize routes
routes = [[0, i, 0] for i in range(1, n)]

# Step 4: Construct initial feasible routes based on savings and capacity constraints
def merge_routes(r1, r2):
    if r1[-2] == r2[1] and sum(demands[c] for c in r1[1:-1]) + sum(demands[c] for c in r2[1:-1]) <= robot_capacity:
        return r1[:-1] + r2[1:]
    return None

def assign_routes():
    global routes
    for saving, i, j in savings_list:
        new_route = None
        for r1 in routes:
            for r2 in routes:
                if r1 != r2:
                    new_route = merge_routes(r1, r2)
                    if new_route:
                        routes.remove(r1)
                        routes.remove(r2)
                        routes.append(new_route)
                        break
            if new_route:
                break

assign_routes()

# Robots assignment
robot_routes = routes[:num_robots]

# Step 5: Calculate the total travel cost
def calculate_route_cost(route):
    return sum(distance_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

overall_cost = 0
for i, route in enumerate(robot_routes):
    cost = calculate_route_config_cost()
    overall_cost += cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")