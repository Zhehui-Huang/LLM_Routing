import numpy as np
from pulp import *

# City coordinates (index 0-7 as depots, then 8-22 as cities)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Create the distance matrix
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord102[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Problem setup
problem = LpProblem("Multiple_TSP_Problem", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(23) for j in range(23) for k in range(num_robots)], 
                     cat='Binary', lowBound=0, upBound=1)

u = LpVariable.dicts("u", [i for i in range(23)], lowBound=0, cat='Continuous')

# Objective: Minimize the total cost
problem += lpSum(distance_matrix[i][j] * x[(i, j, k)] for i in range(23) for j in range(23) for k in range(num_robots))

# Constraints
# Each node must be visited exactly once by any robot
for j in range(23):
    problem += lpSum(x[(i, j, k)] for k in range(num_robots) for i in range(23)) == 1

# Robots must complete a tour starting and ending at their depots
for k in range(num_robots):
    problem += lpSum(x[(k, j, k)] for j in range(23) if j != k) == 1
    problem += lpSum(x[(j, k, k)] for j in range(23) if j != k) == 1
    
# Ensuring sub-tours are eliminated and every other city is visited once per robot
for k in range(num_robots):
    for i in range(23):
        for j in range(23):
            if i != j:
                problem += u[i] - u[j] + (23 - 1) * x[(i, j, k)] <= 23 - 2

# Solve problem
problem.solve()

# Output results
overall_cost = 0
for k in range(num_robots):
    print(f"Robot {k} Tour: ", end='')
    current_city = k
    tour = [current_city]
    while True:
        next_city = next(j for j in range(23) if x[(current_city, j, k)].varValue == 1)
        if next_city == k:
            break
        tour.append(next_city)
        current_city = next_city
    tour.append(k)
    print(tour)
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")