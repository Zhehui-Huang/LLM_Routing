import numpy as np
import math
from collections import defaultdict
from heapq import heappop, heappush

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
    1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
]

# Robot parameters
num_robots = 4
capacity = 6000

# Helper functions
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate distances
n = len(coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Sort cities by angle from depot
angles = []
depot = coordinates[0]
for i in range(1, n):
    dx, dy = coordinates[i][0] - depot[0], coordinates[i][1] - depot[1]
    angle = math.atan2(dy, dx)
    angles.append((angle, i))
angles.sort()

# Assign routes to robots
tours = defaultdict(list)
current_loads = [0] * num_robots
current_tours = [[0] for _ in range(num_robots)]
robot_index = 0

for angle, index in angles:
    if current_loads[robot_index] + demands[index] > capacity:
        # finish this robot's current tour
        current_tours[robot_index].append(0)
        robot_index = (robot_index + 1) % num_robots
        while current_loads[robot_index] != 0:
            robot_index = (robot_index + 1) % num_robots
    current_loads[robot_index] += demands[index]
    current_tours[robot_index].append(index)

# Complete all tours
for i in range(num_robots):
    if current_tours[i][-1] != 0:
        current_tours[i].append(0)

# Calculate travel costs
total_cost = 0
for robot_id, tour in enumerate(current_tours):
    cost = 0
    print(f"Robot {robot_id} Tour: {tour}")
    for j in range(len(tour) - 1):
        cost += distances[tour[j]][tour[j + 1]]
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")