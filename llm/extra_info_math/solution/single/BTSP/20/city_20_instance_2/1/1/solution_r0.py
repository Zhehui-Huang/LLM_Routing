from ortools.linear_solver import pywraplp
import math

# Coordinates of cities including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities (including the depot)
n = len(cities)

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create the solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Distance maximization variable
d = solver.NumVar(0, solver.infinity(), 'd')

# x[i, j] is 1 if the tour moves from city i to city j
x = {}
for i in range(n):
    for j in range(n):
        if i != j:
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# Objective: Minimize the maximum distance between consecutive cities
solver.Minimize(d)

# Constraints
for i in range(n):
    solver.Add(solver.Sum(x[i, j] for j in range(n) if i != j) == 1) # leave each city once
    solver.Add(solver.Sum(x[j, i] for j in range(n) if i != j) == 1) # enter each city once

# Subtour elimination constraints
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        solver.Add(sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Maximum distance constraints for each edge used
for i in range(n):
    for j in range(n):
        if i != j:
            solver.Add(x[i, j] * distance(cities[i], cities[j]) <= d)

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    tour = []
    current = 0
    for _ in range(n):
        tour.append(current)
        next_city = next(j for j in range(n) if j != current and x[current, j].solution_value() > 0.5)
        current = next_city
    tour.append(0)  # return to the depot

    max_distance = max(
        distance(cities[tour[k]], cities[tour[k + 1]])
        for k in range(len(tour) - 1)
    )
    total_distance = sum(
        distance(cities[tour[k]], cities[tour[k + 1]])
        for k in range(len(tour) - 1)
    )

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No solution found")