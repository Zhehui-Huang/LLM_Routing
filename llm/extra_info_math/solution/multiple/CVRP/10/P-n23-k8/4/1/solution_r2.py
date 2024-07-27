import pulp as pl
import math

# Constants
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64),
                    (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
                    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
                    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63),
                    (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14,
           6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_count = 8
capacity = 40
n = len(city_coordinates)

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
distance_matrix = [[euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the optimization model
model = pl.LpProblem("CVRP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", ((r, i, j) for r in range(robot_count) for i in range(n) for j in range(n) if i != j),
                        cat=pl.LpBinary)

# Objective function: Minimize the total travel cost
model += pl.lpSum(distance_matrix[i][j] * x[r, i, j] for r in range(robot_count) for i in range(n) for j in range(n) if i != j)

# Constraints
# 1. Each city is visited exactly once by any robot
for j in range(1, n):
    model += pl.lpSum(x[r, i, j] for r in range(robot_id) for i in range(n) if i != j) == 1

# 2. Each robot's tour must respect the capacity constraint
for r in range(robot_id):
    model += pl.lpSum(demands[i] * pl.lpSum(x[r, i, j] for j in range(n) if i != j) for i in range(1, n)) <= capacity

# 3. Ensure correct flow into and out of cities
for r in range(robot_id):
    for i in range(1, n):
        model += pl.lpSum(x[r, j, i] for j in range(n) if i != j) - pl.lpSum(x[r, i, j] for j in range(n) if i != j) == 0

# 4. Flow conservation for depot
for r in range(robot_id):
    model += pl.lpSum(x[r, 0, j] for j in range(1, n)) == 1  # leave depot once
    model += pl.lpSum(x[r, j, 0] for j in range(1, n)) == 1  # return to depot once

# Solve the model
model.solve()

# Extracting and displaying the solution
total_cost = 0
for r in range(robot_id):
    route = [0]
    next_location = 0
    while True:
        next_step = [j for j in range(n) if j != next_location and pl.value(x[r, next_location, j]) == 1]
        if not next_step:
            break
        next_location = next_step[0]
        route.append(next_location)
    route.append(0)
    tour_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost += tour_cost
    print(f"Robot {r} Tour: {route}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")