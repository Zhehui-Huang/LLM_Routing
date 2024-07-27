import numpy as np
from math import sqrt

# City coordinates and demands
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Constants
num_robots = 8
capacity = 35
depot_index = 0

# Function to calculate distance between two points
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Distance matrix calculation
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Clarke and Wright Savings algorithm
def savings_algorithm(demands, capacity, distance_matrix):
    savings = {}
    routes = []
    num_cities = len(demands)

    # Calculate savings
    for i in range(1, num_cities):
        for j in range(i+1, num_cities):
            if i != j:
                s = distance_matrix[depot_index][i] + distance_matrix[depot_index][j] - distance_matrix[i][j]
                savings[(i, j)] = s

    # Sort savings in descending order
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

    # Create routes based on savings
    assigned = set()
    routes = []
    for (i, j), _ in sorted_savings:
        if i not in assigned and j not in assigned and (demands[i] + demands[j]) <= capacity:
            routes.append([depot_index, i, j, depot_index])
            assigned.update([i, j])
    
    # Assign remaining unassigned cities, each to a new route if capacity allows
    for i in range(1, num_cities):
        if i not in assigned:
            if demands[i] <= capacity:
                routes.append([depot_index, i, depot_index])
                assigned.add(i)

    return routes

# Generate routes
routes = savings_algorithm(demands, capacity, distance_matrix)

# Calculate route distances and total cost
total_distance = 0
for r, route in enumerate(routes):
    route_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_distance += route_distance
    print(f"Robot {r} Tour: {route}")
    print(f"Robot {r} Total Travel Cost: {round(route_distance, 2)}")

print(f"Overall Total Travel Cost: {round(total_distance, 2)}")