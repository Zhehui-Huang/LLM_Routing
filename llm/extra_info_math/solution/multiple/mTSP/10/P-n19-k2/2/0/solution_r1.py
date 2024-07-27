from scipy.spatial import distance
import numpy as np
from pulp import *
import math

# City coordinates, including depot (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
m = 2
# Number of nodes including the depot
n = len(coordinates)

# Calculate Euclidean distance between each pair of nodes
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cost matrix: distance between nodes
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create problem instance
problem = LpProblem("Multiple_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 0, 1, LpBinary)
u = LpVariable.dicts("u", list(range(1, n)), lowBound=0)

# Objective function
problem += lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by a salesman
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each city must be left exactly once
for i in range(1, n):
    problem += lpSum(x[i, j, k] for j in range(n) for k in range(m) if i != j) == 1

# Salesmen constraints
for k in range(m):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1  # leave the depot
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1  # return to the depot

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Gather results
tours = {k: [] for k in range(m)}

for k in range(m):
    tour = [0]
    while True:
        next_city = None
        for j in range(n):
            if pulp.value(x[tour[-1], j, k]) == 1:
                next_city = j
                break
        if next_city is None or next_city == 0:
            tour.append(0)
            break
        tour.append(next_freight)
        
    tours[k] = tour

# Print the output
total_travel_cost = 0
for k in tours:
    tour_cost = sum(c[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    total_travel_cost += tour_cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")