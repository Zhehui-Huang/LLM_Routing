from ortools.linear_solver import pywraplp
import math
import numpy as np

# Coordinates for each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots
num_robots = 8

# Calculate Euclidean distances between each pair of nodes
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = {
    (i, j): euclidean_distance(coordinates[i], coordinates[j])
    for i in range(len(coordinates))
    for j in range(len(coordinates))
}

# Initialize solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Variables
x = {}
u = {}
n = len(coordinates)

for i in range(n):
    for j in range(n):
        if i != j:
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')
    u[i] = solver.IntVar(0, n, f'u[{i}]')

# Objective
objective = solver.Objective()
for i, j in distances:
    if i != j:
        objective.SetCoefficient(x[i, j], distances[i, j])
objective.SetMinimization()

# Constraints
# Each city must be arrived at and left exactly once
for j in range(1, n):
    solver.Add(sum(x[i, j] for i in range(n) if i != j) == 1)
    solver.Add(sum(x[j, i] for i in range(n) if i != j) == 1)

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            solver.Add(u[i] - u[j] + n * x[i, j] <= n - 1)

# Only num_robots robots can leave the depot city
solver.Add(sum(x[0, j] for j in range(1, n)) == num_robots)

# Solve the model
status = solver.Solve()

# Output the solution
if status == pywraplp.Solver.OPTIMAL:
    tours = {}
    for r in range(num_robots):
        tours[r] = []
        current_city = 0
        tour_cost = 0
        while True:
            for j in range(n):
                if j != current_city and x[current_city, j].solution_value() > 0.5:
                    tours[r].append(j)
                    tour_cost += distances[current_city, j]
                    current_city = j
                    break
            if current_city == 0:
                break
        print(f"Robot {r} Tour: {[0] + tours[r]}")
        print(f"Robot {r} Total Travel Cost: {tour_cost}")
    
    # Calculate overall cost
    overall_total_cost = sum(distances[i, j] * x[i, j].solution_value()
                             for i in range(n) for j in range(n) if i != j)
    print(f"Overall Total Travel Cost: {overall_total_cost}")
else:
    print("The problem does not have an optimal solution.")