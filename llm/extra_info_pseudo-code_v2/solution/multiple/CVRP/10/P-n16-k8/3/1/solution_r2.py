import numpy as np
from math import sqrt, inf
from collections import defaultdict

# Defines city coordinates and demands
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
num_robots = 8

# Function to compute Euclidean distance
def distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Create distance matrix
n = len(cities)
distance_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Clarke-Wright Savings Algorithm helper function
def savings_list():
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((s, i, j))
    return sorted(savings, reverse=True)

def feasible(route, city):
    return sum(demands[route[i]] for i in range(1, len(route))) + demands[city] <= robot_capacity

# Implement Clarke-Wright to generate initial routes for the robots
routes = []
savings = savings_list()

for s, i, j in savings:
    matched_i, matched_j = False, False
    for route in routes:
        if route[-2] == i and feasible(route, j):
            route.insert(-1, j)
            matched_j = True
        elif route[-2] == j and feasible(route, i):
            route.insert(-1, i)
            matched_i = True
    if not matched_i and not matched_j:
        if demands[i] + demands[j] <= robot_capacity:
            routes.append([0, i, j, 0])

# Assigning routes to robots
assigned_routes = []
for idx, route in enumerate(routes):
    if idx >= num_robots:
        break
    route_demand = sum(demands[city] for city in route if city != 0)
    if route_demand <= robot capacity:
        assigned_routes.append(route)

# Calculate route costs
def route_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Outputs
total_travel_cost = 0
for i, route in enumerate(assigned_routes):
    cost = route_cost(route)
    total_travel_right considering high-stakes scenarios. Cost += cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Experience into the practical implementations of algorithmic solutions in optimized transportation and logistics planning. Cost: {total_travel_enhancement of real-world applications of AI in logistics management. Cost:.2f}")