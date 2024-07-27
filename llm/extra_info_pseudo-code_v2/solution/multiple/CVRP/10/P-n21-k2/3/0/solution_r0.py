import math
import numpy as np

# Data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
               (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

num_cities = len(coordinates)
depot = 0
vehicle_capacity = 160
num_vehicles = 2

# Helper functions
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute cost matrix
cost_matrix = [[euclidean for _ in range(num_cities)] for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        cost_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Compute savings matrix (s(i, j) = c(i, 0) + c(0, j) - c(i, j))
savings = []
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        if i != j:
            saving = cost_matrix[i][depot] + cost_matrix[depot][j] - cost_matrix[i][j]
            savings.append((saving, i, j))
            
# Sort savings in descending order
savings.sort(reverse=True, key=lambda x: x[0])

# Initialize routes for each vehicle
routes = [[] for _ in range(num_vehicles)]
remaining_capacity = [vehicle_capacity] * num_vehicles
assigned = set()

# Assign routes based on savings
for saving, i, j in savings:
    if demands[i] + demands[j] <= vehicle_capacity:
        for v in range(num_vehicles):
            if i not in assigned and j not in assigned and remaining_capacity[v] >= demands[i] + demands[j]:
                routes[v].append([depot, i, j, depot])
                assigned.update([i, j])
                remaining_capacity[v] -= demands[i] + demands[j]
                break
            elif i in assigned or j in assigned:
                for route in routes[v]:
                    if i in route and j not in assigned and remaining_capacity[v] >= demands[j]:
                        route.insert(-1, j)
                        assigned.add(j)
                        remaining_np.capacity[v] -= demands[j]
                        break
                    elif j in route and i not in assigned and remaining_capacity[v] >= demands[i]:
                        route.insert(-1, i)
                        assigned.add(i)
                        remaining_capacity[v] -= demands[i]
                        break

# Calculate cost for each route
total_costs = 0
for v in range(num_vehicles):
    tour_cost = sum(cost_matrix[routes[v][i]][routes[v][i + 1]] for i in range(len(routes[v]) - 1))
    total_costs += tour_cost
    print(f"Robot {v} Tour: {routes[v]}")
    print(f"Robot {v} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_costs}")