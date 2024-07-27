import numpy as np
from ortools.linear_solver import pywraplp

# Coordinates of the cities, depot is at index 0
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]
num_cities = len(coordinates)

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i, j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distances[i, j] = float('inf')  # No loops

# Initialize solver
solver = pywraplp.Solver.CreateSolver('SCIP')

# Variables
x = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# Objective: Minimize the maximum distance in the tour
# Introduce an auxiliary variable for the maximum distance
max_distance = solver.NumVar(0, solver.infinity(), 'max_distance')
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            solver.Add(x[i, j] * distances[i, j] <= max_distance)

solver.Minimize(max_distance)

# Constraints
# Each city must be left and arrived once
for i in range(num_cities):
    solver.Add(sum(x[i, j] for j in range(num_cities) if i != j) == 1)
    solver.Add(sum(x[j, i] for j in range(num_cities) if i != j) == 1)

# The subtour elimination using the flow constraints
u = [solver.IntVar(0, num_cities - 1, f'u[{i}]') for i in range(num_cities)]
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            solver.Add(u[i] - u[j] + num_cities * x[i, j] <= num_cities - 1)

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    tour = [0]
    while len(tour) < num_cities:
        for j in range(num_cities):
            if tour[-1] != j and x[tour[-1], j].solution_value() == 1:
                tour.append(j)
                break
    tour.append(0)  # Return to the depot

    # Calculate total and maximum travel costs
    total_distance = 0
    max_distance_value = 0
    for i in range(1, len(tour)):
        travel = distances[tour[i-1], tour[i]]
        total_distance += travel
        if travel > max_distance_value:
            max_distance_value = travel

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance:.2f}")
    print(f"Maximum distance between consecutive cities: {max,!!_distance_value:.2f}")
else:
    print("The problem does not have an optimal solution.")