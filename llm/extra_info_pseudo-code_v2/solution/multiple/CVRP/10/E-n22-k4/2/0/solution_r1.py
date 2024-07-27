import numpy as np
from scipy.spatial import distance

# Define locations and demands
locations = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
robot_capacity = 6000

# Distance matrix
num_locations = len(locations)
distance_matrix = np.zeros((num_locations, num_locations))
for i in range(num_locations):
    for j in range(num_locations):
        distance_matrix[i][j] = distance.euclidean(locations[i], locations[j])

# Initial empty routes for each robot
routes = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
remaining_demands = demands.copy()

# Assign depot routes initializing
for i in range(num_robots):
    routes[i].append(0)

# Greedy approach to assign locations to each robot
for city_index in range(1, num_locations):
    if remaining_demands[city_index] > 0:
        for robot_index in range(num_robots):
            if current_loads[robot_index] + remaining_demands[city_index] <= robot_capacity:
                # Assign city to robot
                routes[robot_index].append(city_index)
                current_loads[robot_index] += remaining_demands[city_index]
                remaining_demands[city_index] = 0
                break

# Ensure every city is visited and returning to the depot
for i in range(num_robots):
    if len(routes[i]) > 1:  # If more than just the depot
        routes[i].append(0)

# Calculate route costs
route_costs = [0] * num_robots
total_cost = 0

for robot_index in range(num_robots):
    route_cost = 0
    if len(routes[robot_index]) > 1:
        for j in range(1, len(routes[robot_index])):
            route_cost += distance_matrix[routes[robot_index][j - 1]][routes[robot_index][j]]
    route_costs[robot_index] = route_cost
    total_cost += route_cost

# Output results
for robot_index in range(num_robots):
    print(f"Robot {robot_index} Tour: {routes[robot_index]}")
    print(f"Robot {robot_index} Total Travel Cost: {route_costs[robot_index]}")
print(f"Overall Total Travel Cost: {total_cost}")