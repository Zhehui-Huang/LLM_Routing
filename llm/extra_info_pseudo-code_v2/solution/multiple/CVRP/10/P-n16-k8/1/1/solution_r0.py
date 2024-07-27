import numpy as np
import random
from math import sqrt

# City coordinates and demand
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of robots and their capacities
num_robots = 8
robot_capacity = 35

def euc_dist(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Calculate cost matrix
cost_matrix = [[euc_dist(city_coords[i], city_coords[j]) for j in range(len(city_coords))] for i in range(len(city_coords))]

# Calculate savings matrix (Sij = Ci0 + C0j - Cij)
savings = {}
for i in range(1, len(city_coords)):
    for j in range(i + 1, len(city_coords)):
        savings[(i, j)] = cost_matrix[i][0] + cost_matrix[0][j] - cost_matrix[i][j]

# Sort savings in descending order
sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

# Initialization of routes
routes = []
load = {}

def find_route(city):
    for route in routes:
        if city in route:
            return route
    return None

def can_merge(r1, r2):
    combined_load = load[r1] + load[r2]
    return combined_load <= robot_capacity and r1 != r2

# Creating initial routes based on highest savings
for (i, j), _ in sorted_savings:
    route_i = find_route(i)
    route_j = find_route(j)
    if not route_i and not route_j:
        # Both cities are not in a route, create new if possible
        if demands[i] + demands[j] <= robot_capacity:
            routes.append([0, i, j, 0])
            load[len(routes)-1] = demands[i] + demands[j]
    elif route_i and not route_j:
        # City i is in a route, city j is not
        if route_i[-2] == i and load[route_i] + demands[j] <= robot_capacity:  # Can append j to route i
            route_i.insert(-1, j)
            load[route_i] += demands[j]
    elif not route_i and route_j:
        # City j is in a route, city i is not
        if route_j[1] == j and load[route_j] + demands[i] <= robot_capacity:  # Can prepend i to route j
            route_j.insert(1, i)
            load[route_j] += demands[i]
    elif route_i and route_j and route_i != route_j:
        # Both cities are in different routes, try to merge
        if route_i[-2] == i and route_j[1] == j and can_merge(route_i, route_j):
            # Merge route_j into route_i
            load[route_i] += load.pop(route_j)
            routes.remove(route_j)
            route_i.remove(0)
            route_i.extend(route_j[1:])

# Printing the solution
total_cost = 0
for idx, route in enumerate(routes, start=1):
    route_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost += route_cost
    print(f"Robot {idx-1} Tour: {route}")
    print(f"Robot {idx-1} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")