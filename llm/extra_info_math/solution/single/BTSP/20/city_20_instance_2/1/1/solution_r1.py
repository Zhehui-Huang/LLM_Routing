import math
from ortools.linear_solver import pywraplp
import itertools

# Coordinates of cities including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities (including the depot)
n = len(cities)

# Create the solver
solver = pywraplp.Solver.CreateSolver('CBC')

# x[i, j] is 1 if the route moves from i to j
x = {}
for i in range(n):
    for j in range(n):
        if i != j:
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# d is the maximum distance between consecutive cities in the tour
d = solver.NumVar(0, solver.infinity(), 'd')

# Objective: Minimize the maximum distance d
solver.Minimize(d)

# Constraints
# Each city must be left exactly once
for i in range(n):
    solver.Add(sum(x[i, j] for j in range(n) if i != j) == 1)

# Each city must be entered exactly once
for j in range(n):
    solver.Add(sum(x[i, j] for i in range(n) if i != j) == 1)

# Subtour elimination constraints
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        solver.Add(sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Link the distances with the maximum distance variable d
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
        # Find the next city in the tour
        next_city = next(j for j in range(n) if j != current and x[current, j].solution_value() > 0.5)
        tour.append(current)
        current = next_city
    tour.append(0)  # complete the tour back to the depot

    # Calculate the total and max distances based on the tour
    total_distance = sum(distance(cities[tour[k]], cities[tour[k+1]]) for k in range(len(tour)-1))
    max_distance = max(distance(cities[tour[k]], cities[tour[k+1]]) for k in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No solution found.")