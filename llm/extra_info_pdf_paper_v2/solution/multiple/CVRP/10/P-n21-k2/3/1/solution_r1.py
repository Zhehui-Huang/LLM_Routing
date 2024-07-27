import math
import numpy as np

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Vehicle specifics
num_vehicles = 2
vehicle_capacity = 160

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initialize routes
routes = [[] for _ in range(num_vehicles)]
remaining_capacity = [vehicle_capacity] * num_vehicles
route_distance = [0] * num_vehicles

# Clarke-Wright Savings Algorithm
savings = []
n = len(coordinates)
for i in range(1, n):
    for j in range(i + 1, n):
        if i != j:
            s = calculate_distance(coordinates[0], coordinates[i]) + \
                calculate_distance(coordinates[0], coordinates[j]) - \
                calculate_distance(coordinates[i], coordinates[j])
            savings.append((s, i, j))
savings.sort(reverse=True, key=lambda x: x[0])

# Assign routes to vehicles
for save, i, j in savings:
    assigned_i = assigned_j = -1
    
    for index in range(num_vehicles):
        if i in routes[index]:
            assigned_i = index
        if j in routes[index]:
            assigned_j = index
    
    if assigned_i == assigned_j == -1:  # Neither city is in any route
        for index in range(num_vehicles):
            if remaining_capacity[index] >= demands[i] + demands[j] and len(routes[index]) == 0:
                routes[index].extend([0, i, j, 0])
                remaining_capacity[index] -= (demands[i] + demands[j])
                route_distance[index] = calculate_distance(coordinates[0], coordinates[i]) + \
                                        calculate_distance(coordinates[i], coordinates[j]) + \
                                        calculate_distance(coordinates[j], coordinates[0])
                break
    elif assigned_i == -1 and assigned_j != -1:
        if remaining_capacity[assigned_j] >= demands[i]:
            if routes[assigned_j][1] == j:  # prepend
                routes[assigned_j].insert(1, i)
            else:  # append
                routes[assigned_j].insert(-1, i)
            remaining_capacity[assigned_j] -= demands[i]
    elif assigned_j == -1 and assigned_i != -1:
        if remaining_capacity[assigned_i] >= demands[j]:
            if routes[assigned_i][1] == i:  # prepend
                routes[assigned_i].insert(1, j)
            else:  # append
                routes[assigned_i].insert(-1, j)
            remaining_capacity[assigned_i] -= demands[j]

# Recalculate route distances
for idx in range(num_vehicles):
    route_distance[idx] = sum(calculate_distance(coordinates[routes[idx][k]], coordinates[routes[idx][k + 1]])
                              for k in range(len(routes[idx]) - 1))

# Print results
total_cost = sum(route_distance)
print(f"Overall Total Travel Cost: {total_cost}")
for index in range(num_vehicles):
    print(f"Robot {index} Tour: {routes[index]}")
    print(f"Robot {index} Total Travel Cost: {route_distance[index]}")