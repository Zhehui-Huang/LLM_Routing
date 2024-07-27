import numpy as np

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 
           11, 12, 26, 17, 6, 15, 5, 10]

# Robot constraints
num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initialize distances and matrices of distances and savings
def create_matrices(coordinates):
    num_cities = len(coordinates)
    distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] 
                 for i in range(num_cities)]
    savings = [[(distances[0][i] + distances[0][j] - distances[i][j], i, j) 
                for j in range(num_cities) if j != i] for i in range(1, num_cities)]
    return distances, savings

distances, savings = create_matrices(coordinates)

# Flatten and sort savings
flat_savings = [item for sublist in savings for item in sublist]
flat_savings.sort(reverse=True, key=lambda x: x[0])

# Route construction
routes = []
loads = []

# Create routes based on sorted savings
for saving, i, j in flat_savings:
    if i == 0 or j == 0:
        continue
    route_found = False
    for route in routes:
        if (route[-2] == i or route[1] == j) and demands[i] + sum(demands[k] for k in route if k != 0) <= robot_capacity:
            if route[-2] == i:
                route.insert(-1, j)
            else:
                route.insert(1, i)
            route_found = True
            break
    if not route_found:
        if len(routes) < num_robots and demands[i] + demands[j] <= robot_capacity:
            routes.append([0, i, j, 0])
            loads.append(demands[i] + demands[j])

# Add remaining cities
for i in range(1, len(demands)):
    if not any(i in route for route in routes):
        for route in routes:
            if sum(demands[k] for k in route if k != 0) + demands[i] <= robot_capacity:
                route.insert(-2, i)
                break

# Calculate costs and output routes
total_cost = 0
for index, route in enumerate(routes):
    cost = sum(distances[route[k]][route[k + 1]] for k in range(len(route) - 1))
    total_cost += cost
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")