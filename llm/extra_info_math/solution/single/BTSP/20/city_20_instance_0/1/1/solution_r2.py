from math import sqrt
from itertools import combinations
from ortools.linear_solver import pywraplp

# Define the cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance
def distance(ci, cj):
    return sqrt((cities[ci][0] - cities[cj][0]) ** 2 + (cities[ci][1] - cities[cj][1]) ** 2)

# Setup solver
solver = pywraplp.Solver.CreateSolver('CBC')
n = len(cities)
x = {(i, j): solver.BoolVar(f'x[{i},{j}]') for i in range(n) for j in range(n) if i != j}

# Define constraints and objective
max_d = solver.NumVar(0, 10000, 'max_d')
for i in range(n):
    solver.Add(sum(x[i, j] for j in range(n) if i != j) == 1)
    solver.Add(sum(x[j, i] for j in range(n) if i != j) == 1)

for i, j in x:
    solver.Add(x[i, j] * distance(i, j) <= max_d)

# Subtour constraints
for s in range(2, n):
    for S in combinations([i for i in range(1, n)], s):  # Avoid the depot in subtours
        solver.Add(sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

# Minimize the maximum edge length
solver.Minimize(max_d)

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    tour = []
    # Find the tour from the variables
    current = 0
    count = 0
    while count < n:
        for j in range(n):
            if j != current and x[current, j].solution_value() == 1:
                tour.append(current)
                current = j
                count += 1
                break
    tour.append(0)  # close the tour back to the depot

    # Calculate the total travel cost and max distance
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    # Output the tour, total cost and max distance
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("The problem does not have an optimal solution.")