import math
import random

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot information
num_robots = 2
capacity = 160

# Function to calculate Euclidean distance between cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Initialize tour for each robot
robot_tours = [[] for _ in range(num_robots)]
robot_loads = [0] * num_robots
robot_costs = [0] * num_robots

# Calculate initial savings list
savings = []
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        if i != j:
            save = euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_distance(i, j)
            savings.append((save, i, j))
savings.sort(reverse=True, key=lambda x: x[0])

# Route construction phase
while savings:
    _, i, j = savings.pop(0)
    assigned = False
    for r in range(num_robots):
        if (demands[i] + demands[j] + robot_loads[r] <= capacity and len(robot_tours[r]) == 0):
            robot_tours[r].extend([0, i, j, 0])
            robot_loads[r] += demands[i] + demands[j]
            robot_costs[r] += euclidean_distance(0, i) + euclidean_distance(i, j) + euclidean_distance(j, 0)
            assigned = True
            break

    if not assigned:
        for r in range(num_robots):
            if demands[i] + robot_loads[r] <= capacity and (0 in robot_tours[r]):
                robot_tours[r].insert(-1, i)
                robot_loads[r] += demands[i]
                last = robot_tours[r][-2]
                robot_costs[r] += euclidean_foristance(last, i) + euclidean_distance(i, 0) - euclidean_distance(last, 0)
                assigned = True
                break

# Output each robot's tour and the overall cost
total_cost = 0
for r in range(num_robots):
    print(f"Robot {r} Tour: {robot_tours[r]}")
    print(f"Robot {r} Total Travel Cost: {robot_costs[r]}")
    total_cost += robot_costs[r]

print(f"Overall Total Travel : {total_cost}")