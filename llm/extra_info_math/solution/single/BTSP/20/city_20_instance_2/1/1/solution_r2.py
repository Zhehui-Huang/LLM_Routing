import math
from ortools.linear_solver import pywraplp
import itertools

# Coordinates of the cities including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

n = len(cities)  # Number of cities including the depot

# Create the solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Variables
x = {(i, j): solver.BoolVar(f'x[{i},{j}]') for i in range(n) for j in range(n) if i != j}
d = solver.NumVar(0, solver.infinity(), 'd')

# Objective
solver.Minimize(d)

# Constraints
for i in range(n):
    solver.Add(sum(x[i, j] for j in range(n) if i != j) == 1)  # leave each city once
    solver.Add(sum(x[j, i] for j in range(n) if i != j) == 1)  # enter each city once

# Eliminate subtours
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        solver.Add(sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Link distances and d
for i in range(n):
    for j in range(n):
        if i != j:
            solver.Add(distance(cities[i], cities[j]) * x[i, j] <= d)

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    tour = []
    next_city = 0
    for _ in range(n):
        for j in range(n):
            if j != next_city and x[next_city, j].solution_value() > 0.5:
                tour.append(next_city)
                next_city = j
                break
    tour.append(0)  # Complete the tour by returning to the depot

    max_distance = max(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    total_cost = sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No solution found.")