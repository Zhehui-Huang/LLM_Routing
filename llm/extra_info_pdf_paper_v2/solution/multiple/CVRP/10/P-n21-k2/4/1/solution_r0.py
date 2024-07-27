import math
from itertools import combinations

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot details
num_robots = 2
robot_capacity = 160

def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

# Compute the matrix of distances between each pair of cities
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = distance_matrix[j][i] = euclidean_distance(coordinates[i], coordinates[j])

# Clarke-Wright Savings Calculation
savings = []
for i in range(1, num_cities):
    for j in range(i+1, num_cities):
        if i != j:
            S_ij = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((S_ij, i, j))
savings.sort(reverse=True, key=lambda x: x[0])  # Sort by savings in descending order

# Attempt to construct routes
routes = []
capacity_used = {}

for _, i, j in savings:
    # Check if either city is already assigned to a route and if not, exceed capacity constraints
    found_i, found_j = None, None
    for route in routes:
        if i in route:
            found_i = route
        if j in (route):
            found_j = route

    if found_i is not None and found_j is not None and found_i is not found_j:
        # If merging two routes, check the combined capacity
        if sum(demands[k] for k in found_i) + sum(demands[k] for k in found_j) <= robot_capacity:
            combined_route = found_i + [0] + list(reversed(found_j))
            routes.remove(found_i)
            routes.remove(found_j)
            routes.append(combined_route)
    elif found_i is not None and found_j is None and sum(demands[k] for k in found_i) + demands[j] <= robot_capacity:
        found_i.append(j)
    elif found_j is not None and found_i is None and sum(demands[k] for k in found_j) + demands[i] <= robot_capacity:
        found_j.insert(0, i)
    elif found_i is None and found_j is None:
        if demands[i] + demands[j] <= robot_capacity:
            routes.append([i, 0, j])

# Add depot to the beginning and the end of each route
for route in routes:
    if route[0] != 0:
        route.insert(0, 0)
    if route[-1] != 0:
        route.append(0)

# Results Display
total_travel_cost = 0
output_results = []
for idx, route in enumerate(routes):
    cost = sum(distance_matrix[route[k]][route[k + 1]] for k in range(len(route) - 1))
    total_travel_cost += cost
    output_results.append((f"Robot {idx} Tour: {route}", f"Robot {idx} Total Travel Cost: {round(cost, 2)}"))

output_results.append(f"Overall Total Travel Cost: {round(total_travel_cost, 2)}")

for result in output_results:
    print(result)