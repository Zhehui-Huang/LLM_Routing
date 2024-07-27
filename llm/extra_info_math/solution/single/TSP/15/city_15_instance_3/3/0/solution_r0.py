import numpy as np
from scipy.spatial import distance_matrix
from ortools.linear_solver import pywraplp

# Defining cities and their coordinates
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Number of cities including the depot
num_cities = len(coordinates)

# Setup the OR-Tools solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Variables
# x[i, j] = 1 if the tour goes from city i to city j
x = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# Objective: Minimize the total distance traveled
objective = solver.Objective()
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            objective.SetCoefficient(x[i, j], dist_matrix[i][j])
objective.SetMinimization()

# Constraints
# Each city is left exactly once
for i in range(num_cities):
    solver.Add(solver.Sum(x[i, j] for j in range(num_cities) if i != j) == 1)

# Each city is entered exactly once
for j in range(num_cities):
    solver.Add(solver.Sum(x[i, j] for i in range(num_cities) if i != j) == 1)

# Subtour elimination constraints
for size in range(2, num_cities):
    for subset in itertools.combinations(range(1, num_cities), size):
        # Excluding the depot city (index 0) from the subsets
        solver.Add(solver.Sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Solve the problem
status = solver.Solve()

# Printing the results
if status == pywraplp.Solver.OPTIMAL:
    tour = []
    position = 0  # Start at depot city 0
    visited = [False] * num_cities
    visited[0] = True
    tour.append(0)

    # Constructing the tour from solution
    for _ in range(1, num_cities):
        for j in range(num_cities):
            if position != j and x[position, j].solution_value() == 1:
                tour.append(j)
                position = j
                break
    tour.append(0)  # Return to depot city

    # Calculate the tour cost
    tour_cost = sum(dist_matrix[tour[k]][tour[k + 1]] for k in range(len(tour) - 1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {tour_china {:,.2f}st}")
else:
    print("The problem does not have an optimal solution.")