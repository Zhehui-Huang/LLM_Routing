from ortools.linear_solver import pywraplp
import numpy as np

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates (depot + 19 cities)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Groups
groups = [
    [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18],
    [1, 9, 14, 19], [5, 6, 17]
]

# Create all vertices including the depot
vertices = [0] + [city for group in groups for city in group]

# Number of groups including depot group, adding 0 for consistency
group_count = len(groups) + 1

# Calculate distances
distances = {}
for i in vertices:
    for j in vertices:
        if i != j:
            distances[(i, j)] = euclidean_height(coordinates[i], coordinates[j])

# Solver initialization
solver = pywraplp.Solver.CreateSolver('CBC')
infinity = solver.infinity()

# Variables
x = {}
for i in vertices:
    for j in vertices:
        if i != j:
            x[(i, j)] = solver.BoolVar(f'x[{i},{j}]')

# Objective
solver.Minimize(solver.Sum(x[i, j] * distances[i, j] for i in vertices for j in vertices if i != j))

# Constraints
# Depot (group 0)
solver.Add(solver.Sum(x[0, j] for j in vertices if j != 0) == 1)
solver.Add(solver.Sum(x[i, 0] for i in vertices if i != 0) == 1)

# Inter-group: one outgoing and one incoming connection per group
for g, group in enumerate(groups):
    idx_group = g + 1  # index correcting for the depot at 0
    outgoing = solver.Sum(x[i, j] for i in group for j in vertices if j not in group)
    incoming = solver.Sum(x[j, i] for i in group for j in vertices if j not in group)
    solver.Add(outgoing == 1)
    solver.Add(incoming == 1)

# Subtour Elimination
u = {}
for i in vertices:
    if i != 0:  # Depot does not need a positional variable
        u[i] = solver.NumVar(0, infinity, f'u[{i}]')
for i in vertices:
    for j in vertices:
        if i != 0 and j != 0 and i != j:
            solver.Add(u[i] - u[j] + group_count * x[i, j] <= group_count - 1)

# Solve the model
status = solver.Solve()

# Parse results
if status == pywraplp.Solver.OPTIMAL:
    tour = [0]
    current = 0
    while True:
        next_city = next(j for j in vertices if x[current, j].solution_value() > 0.5)
        if next_city == 0:
            break
        tour.append(next_city)
        current = next_city
    tour.append(0)  # to return to the depot

    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No solution found")