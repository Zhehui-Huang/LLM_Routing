from ortools.linear_solver import pywraplp
import math
import numpy as np

# Define the cities (coordinates)
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Number of cities
n = len(coordinates)

# Cost matrix - Euclidean distance between each pair of nodes
def calculate_distance(coord1, coord2):
    return int(math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2))

cost_matrix = [
    [calculate_distance(coordinates[i], coordinates[j]) for j in range(n)]
    for i in range(n)
]
    
# Create the integer programming solver
solver = pywraplp.Solver('TSP', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# Variables
x = {}
for i in range(n):
    for j in range(n):
        if i != j:  # No loops (i.e., a city can't go to itself)
            x[(i, j)] = solver.BoolVar(f'x_{i}_{j}')

# Objective - minimize the total distance
objective = solver.Objective()
for i in range(n):
    for j in range(n):
        if i != j:
            objective.SetCoefficient(x[(i, j)], cost_matrix[i][j])
objective.SetMinimization()

# Constraint 1: Each city has exactly one exit
for i in range(n):
    solver.Add(solver.Sum([x[(i, j)] for j in range(n) if i != j]) == 1)

# Constraint 2: Each city has exactly one entrance
for j in range(n):
    solver.Add(solver.Sum([x[(i, j)] for i in range(n) if i != j]) == 1)

# Subtour elimination constraints (simplified by using the Miller-Tucker-Zemlin formulation)
u = [solver.IntVar(0, n-1, f'u_{i}') for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            solver.Add(u[i] - u[j] + n * x[(i, j)] <= n-1)

# Solve the model
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution found!')
    tour = []
    visited = np.zeros(n, dtype=int)
    current = 0
    tour.append(current)

    for _ in range(1, n):
        next_city = [j for j in range(n) if j != current and x[(current, j)].solution_value() > 0.5][0]
        tour.append(next_city)
        visited[current] = 1
        current = next_city

    # Return to the depot
    tour.append(0)

    total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print('The problem does not have an optimal solution.')