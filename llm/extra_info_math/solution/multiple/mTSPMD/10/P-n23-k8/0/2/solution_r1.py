import numpy as np
from pulp import *

# City coordinates (index 0-7 as depots, then 8-22 as cities)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots (assuming 1 robot per depot)
num_robots = 8

# Distance function using Euclidean distance
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord2[1] - coord1[1])**2)

# Distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i][j] = calculate_particle_distance(coordinates[i], coordinates[j])

# Define the problem
problem = LpProblem("multi_tsp_problem", LpMinimize)

# Decision variables: x[i][j][k] is whether robot k travels from i to j
x = LpVariable.dicts("x", [(i, j, k) for i in range(23) for j in range(23) for k in range(num_robots)], 
                     cat='Binary')

# Continuous variable for preventing subtours
u = LpVariable.dicts("u", (i for i in range(23)), lowBound=0, cat="Continuous")

# Objective function
problem += lpSum(distance_matrix[i][j] * x[(i, j, k)] for i in range(23) for j in range(23) for k in range(num_robots))

# Constraints
# Each city visited exactly once by all robots combined
for j in range(23):
    problem += lpSum(x[(i, j, k)] for i in range(23) for k in range(num_robots) if i != j) == 1

# Each robot starts and ends at its designated depot
for k in range(num_robots):
    problem += lpSum(x[(k, j, k)] for j in range(23) if j != k) == 1
    problem += lpSum(x[(j, k, k)] for j in range(23) if j != k) == 1

# Subtour elimination constraints
for i in range(1, 23):
    for j in range(1, 23):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (23 * x[(i, j, k)]) <= 22

# Solve the MILP
problem.solve()

# Collect tours for each robot
overall_total_cost = 0
for k in range(num_robots):
    tour = []
    # Find tour beginning at depot k
    start = k
    next_city = start
    while True:
        for j in range(23):
            if x[(next_city, j, k)].varValue == 1:
                next_city = j
                tour.append(next_city)
                break
        if next_city == start:
            break
    # Calculate tour cost
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")