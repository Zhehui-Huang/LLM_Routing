from math import sqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

# Distance function
def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Establishing city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robots info
num_robots = 8
capacity = 40

# Generate cost matrix
n = len(coordinates)
cost_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Basic greedy assignment: simple split of workload focusing on demands, not an optimal split
robot_routes = [[] for _ in range(num_robots)]
current_capacities = [capacity] * num_robots
current_locations = [0] * num_robots

assigned_cities = [False] * n
assigned_cities[0] = True  # Depot is not a city to assign

# Greedy distribution of cities to robots
for city in range(1, n):
    if demands[city] == 0:
        continue
    for robot in range(num_robots):
        if current_capacities[robot] >= demands[city]:
            robot_routes[robot].append(city)
            current_capacities[robot] -= demands[city]
            assigned_cities[city] = True
            break

# Calculate travel costs and final configuration
overall_cost = 0
results = []

for idx, route in enumerate(robot_routes):
    if route:
        full_route = [0] + route + [0]
        cost = sum(cost_matrix[full_route[i]][full_route[i + 1]] for i in range(len(full_route) - 1))
        overall_cost += cost
        results.append({
            'robot_id': idx,
            'tour': full_route,
            'cost': round(cost, 2)
        })

# Output results
print("\nCalculated routes and costs:")
for result in results:
    print(f"Robot {result['robot_id']} Tour: {result['tour']}")
    print(f"Robot {result['robot_id']} Total Travel Cost: {result['cost']}")
print(f"\nOverall Total Travel Cost: {round(overall_cost, 2)}")