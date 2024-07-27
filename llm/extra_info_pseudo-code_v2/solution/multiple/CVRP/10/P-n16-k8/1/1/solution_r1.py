import numpy as np
import random
from math import sqrt

# Data definition
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Problem parameters
num_robots = 8
robot_capacity = 35

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate cost matrix
cost_matrix = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))] for i in range(len(city_coords))]

# Calculate savings (Cij = Ci0 + C0j - Cij)
savings = {}
for i in range(1, len(city_coords)):
    for j in range(i + 1, len(city_coords)):
        if i != j:
            savings[(i, j)] = cost_matrix[i][0] + cost_matrix[0][j] - cost_matrix[i][j]

# Sort the savings in descending order
sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)

# Initialize routes and loads
routes = []
loads = []

def can_add_to_route(route, city):
    if demands[city] + loads[route] <= robot_capacity and (routes[route][-1] == 0 or city not in routes[route]):
        return True
    return False

# Greedy route formation based on savings
for ((i, j), saving) in sorted_savings:
    added = False
    for r1 in range(len(routes)):
        if can_add_to_route(r1, i):
            for r2 in range(len(routes)):
                if can_add_to_route(r2, j) and r1 != r2:
                    # Merge routes r1 and r2 through i and j
                    if routes[r1][-2] == i and routes[r2][1] == j:
                        routes[r1].pop()  # Remove last 0
                        routes[r1].extend(routes[r2])
                        loads[r1] += loads[r2]
                        routes.pop(r2)
                        loads.pop(r2)
                        added = True
                        break
            if not added:
                if can_add_to_route(r1, j):
                    routes[r1].insert(-1, j)
                    loads[r1] += demands[j]
                    added = True
            if added:
                break

    if not added:
        if demands[i] + demands[j] <= robot_capacity:
            routes.append([0, i, j, 0])
            loads.append(demands[i] + demands[j])

# Output tour and costs
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(cost_matrix[route[n]][route[n+1]] for n in range(len(route) - 1))
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")