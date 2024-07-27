from math import sqrt
from itertools import combinations
from ortools.linear_solver import pywraplp

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Calculate distances matrix
n = len(cities)
dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist[i][j] = sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Solver setup
solver = pywraplp.Solver.CreateSolver('CBC')
x = {}
for i in range(n):
    for j in range(n):
        if i != j:
            x[i, j] = solver.BoolVar(f'x_{i}_{j}')

# Objective: minimize maximum distance
max_d = solver.NumVar(0, solver.infinity(), 'max_d')
for i in range(n):
    for j in range(n):
        if i != j:
            solver.Add(x[i, j] * dist[i][j] <= max_d)

solver.Minimize(max_d)

# Constraints: One departure and one arrival per city
for i in range(n):
    solver.Add(solver.Sum(x[i, j] for j in range(n) if i != j) == 1)
    solver.Add(solver.Sum(x[j, i] for j in range(n) if i != j) == 1)

# Subtour prevention
for size in range(2, n):
    for S in combinations(range(1, n), size):  # Exclude depot from subsets
        solver.Add(solver.Sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

# Solve the model
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Found optimal solution!')
    print('Maximum distance between any two cities in the tour:', solver.Objective().Value())

    # Extract tour
    tour = [0]
    current = 0
    while len(tour) < n:
        for j in range(n):
            if j != current and x[current, j].solution_value() > 0.5:
                tour.append(j)
                current = j
                break
    tour.append(0)  # Return to depot

    # Calculate total cost and max distance
    total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print('Tour:', tour)
    print('Total travel cost:', total_cost)
    print('Maximum distance between consecutive cities:', max_distance)
else:
    print('The problem does not have an optimal solution.')