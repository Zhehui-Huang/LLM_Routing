import math
import pulp
from itertools import product

# Number of depots and robots
num_robots = 2
depots = [0, 1]  # Depots map directly to the robot id
num_cities = 21

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance for the distance matrix
def euclidean_distance(point1, point2):
    return round(math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2))

# Problem instance
prob = pulp.LpProblem("Partitioned_VRP", pulp.LpMinimize)

# Variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
     for i in range(num_cities) for j in range(num_cities) if i != j for k in depots}

# Distance matrix
distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

# Objective function
prob += pulp.lpSum(distance_matrix[i][j] * x[i, j, k]
                   for i, j, k in x.keys()), "Total_Tour_Distance"

# Each non-depot city is visited exactly once
for j in range(2, num_cities):
    prob += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in depots if i != j) == 1

# Departure from each depot for each robot
for k in depots:
    prob += pulp.lpSum(x[k, j, k] for j in range(num_cities) if j != k) == 1

# Arrival to each depot for each robot
for k in depots:
    prob += pulp.lpSum(x[j, k, k] for j in range(num_cities) if j != k) == 1

# Flow conservation for each non-depot city
for k in depots:
    for j in range(2, num_cities):
        prob += (
            pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) ==
            pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j)
        )

# Solve the problem
prob.solve()

# Output results
routes = {k: [] for k in depots}
for k in depots:
    # Start from the depot
    next_city = k
    while True:
        next_city = next(j for i, j, dk in x.keys() if i == next_city and pulp.value(x[i, j, dk]) == 1 and dk == k)
        if next_city == k:
            break
        routes[k].append(next_city)

# Output formatted results
total_cost = sum(distance_matrix[i][j] * pulp.value(x[i, j, k])
                 for i, j, k in x.keys() if pulp.value(x[i, j, k]) == 1)
for k in depots:
    route_cost = sum(distance_matrix[i][j] * pulp.value(x[i, j, k])
                     for i, j in zip([k] + routes[k], routes[k] + [k]))
    print(f"Robot {k} Tour: {[k] + routes[k] + [k]}")
    print(f"Robot {k} Total Travel Cost: {round(route_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")