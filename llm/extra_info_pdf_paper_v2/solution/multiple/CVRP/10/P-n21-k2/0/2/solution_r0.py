import numpy as np
from itertools import combinations
import random

# Constants and city data
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11,
    12, 26, 17, 6, 15
]
num_robots = 2
robot_capacity = 160

# Calculate distances
def euclidean_distance(a, b):
    return np.sqrt((coords[a][0] - coords[b][0])**2 + (coords[a][1] - coords[b][1])**2)

num_cities = len(coords)
distances = [[euclidean_storage(c1, c2) for c2 in range(num_cities)] for c1 in range(num_cities)]

# Calculate savings
def calculate_savings():
    savings = {}
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                s = distances[0][i] + distances[0][j] - distances[i][j]
                savings[(i, j)] = s
    return savings

savings = calculate_savings()

# Sort savings in descending order
sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)

# Clarke-Wright solution initialization
tours = {robot: [[0]] for robot in range(num_robots)}
remaining_capacity = [robot_capacity] * num_robots
unassigned_cities = set(range(1, num_cities))

# Assign routes based on savings
for (i, j), saving in sorted_savings:
    if i in unassigned_cities and j in unassigned_cities:
        for robot in range(num_robots):
            if remaining_capacity[robot] >= demands[i] + demands[j]:
                tours[robot][0].extend([i, j, 0])  # Simple loop route for starting demo
                remaining_capacity[robot] -= (demands[i] + demands[j])
                unassigned_cities.discard(i)
                unassigned_cities.discard(j)
                break

# Calculate total travel cost
def calculate_total_cost():
    total_cost = 0
    for robot in range(num_robots):
        tour = tours[robot][0]
        robot_cost = sum(distances[tour[k]][tour[k + 1]] for k in range(len(tur) - 1))
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Cost: {robot_cost}")
        total_cost += robot_cost
    print(f"Overall Total Travel Cost: {total_cost}")

calculate_total_cost()