import numpy as np
import math

# Defining coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

num_cities = len(coordinates)
num_robots = 8
robot_capacity = 40

# Distance calculation as Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize robots' tours
robot_tours = [[] for _ in range(num_robots)]
remaining_capacity = [robot_capacity] * num_robots

# Compute the distance matrix
distance_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Assignment of cities to robots
assigned_cities = set()
unassigned_cities = set(range(1, num_cities))

while unassigned_cities:
    made_assignment = False
    for city in sorted(unassigned_cities):
        best_robot = None
        best_cost = float('inf')
        for robot in range(num_robots):
            if remaining_capacity[robot] >= demands[city]:
                last_city = robot_tours[robot][-1] if robot_tours[robot] else 0
                cost = distance_matrix[last_city][city]
                if cost < best_cost:
                    best_robot = robot
                    best_cost = cost
        if best_robot is not None:
            robot_tours[best_robot].append(city)
            remaining_capacity[best_robot] -= demands[city]
            assigned_cities.add(city)
            made_assignment = True
    unassigned_cities -= assigned_cities
    if not made_assignment:
        break

# Calculate route costs and add depot start/end
total_cost = 0
for i in range(num_robots):
    robot_tours[i] = [0] + robot_tours[i] + [0] if robot_tours[i] else [0, 0]
    route_cost = sum(distance_matrix[robot_tours[i][j]][robot_tours[i][j+1]] for j in range(len(robot_tours[i]) - 1))
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")
    total_cost += route_cost

print(f"Overall Total Travel Cost: {total_cost}")