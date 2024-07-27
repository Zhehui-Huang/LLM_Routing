import numpy as np

# Data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63),
    (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40
num_robots = 8

num_cities = len(coordinates)

# Compute distance matrix
def euclidean(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = [[euclidean(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Initialize routes and capacity used per robot
routes = [[] for _ in range(num_robots)]
capacity_used = [0] * num_robots

# Sort savings priority based on the maximum savings calculation (i.e., maximal distance reduction)
savings_list = []
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        savings = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
        savings_list.append((savings, i, j))
savings_list.sort(reverse=True, key=lambda x: x[0])

# Method to find an available robot with enough capacity
def find_robot(added_demand):
    for index, cap in enumerate(capacity_used):
        if cap + added_demand <= robot_capacity:
            return index
    return None

# Assign routes to robots based on savings and available capacity
for saving, i, j in savings_list:
    robot_i = find_robot(demands[i])
    robot_j = find_robot(demands[j])
    
    if robot_i is not None and robot_i == robot_j:
        routes[robot_i].extend([i, j])
        capacity_used[robot_i] += (demands[i] + (demands[j] if j not in routes[robot_i] else 0))

# Complete each route with the depot at the start and end
for i in range(num_robots):
    if routes[i]:
        routes[i] = [0] + routes[i] + [0]

# Calculate and print out the solution
overall_total_cost = 0
for i in range(num_robots):
    route_cost = sum(distance_matrix[routes[i][k]][routes[i][k+1]] for k in range(len(routes[i])-1))
    overall_total_cost += route_cost
    if routes[i]:
        print(f"Robot {i} Tour: {routes[i]}")
        print(f"Robot {i} Total Travel Cost: {route_cost}")
        
print(f"Overall Total Travel Cost: {overall_total_cost}")