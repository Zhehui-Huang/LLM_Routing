from ortools.linear_solver import pywraplp
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates (depot + 19 cities)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Groups of cities
groups = [
    [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18],
    [1, 9, 14, 19], [5, 6, 17]
]

# Solver initialization
solver = pywraplp.Solver.CreateSolver('CBC')

# Variables
x = {}
for i in range(20):
    for j in range(20):
        if i != j:
            x[(i, j)] = solver.BoolVar(f'x[{i},{j}]')

# Objective function: Minimize the total travel cost
solver.Minimize(solver.Sum(x[(i, j)] * euclidean_distance(coordinates[i], coordinates[j])
                            for i in range(20) for j in range(20) if i != j))

# Constraints
# A node must be left exactly once and entered exactly once
for j in range(1, 20):  # skip the depot for subtour constraints
    solver.Add(sum(x[(i, j)] for i in range(20) if i != j) == 1)
    solver.Add(sum(x[(j, i)] for i in range(20) if i != j) == 1)

# Subtour avoidance using additional variables (MTZ constraints)
u = {}
for i in range(1, 20): # depot does not need a u variable
    u[i] = solver.IntVar(0, 19, 'u[%i]' % i)
for i in range(1, 20):
    for j in range(1, 20):
        if i != j:
            solver.Add(u[i] - u[j] + 19 * x[(i, j)] <= 18)

# Each group should connect exactly once to the rest of the graph
for group in groups:
    solver.Add(solver.Sum(x[(i, j)] for i in group for j in range(20) if j not in group) == 1)  # Leave group exactly once
    solver.Add(solver.Sum(x[(j, i)] for i in group for j in range(20) if j not in group) == 1)  # Enter group exactly once

# Solve the model and output the results
status = solver.Solve()

if status == pywrapprs.Solver.OPTIMAL:
    # Build the tour from the decision variables
    tour = []
    current_location = 0
    for _ in range(20):
        tour.append(current_location)
        next_location = next(j for j in range(20) if x[(current_location, j)].solution_value() > 0.5)
        if next_location == 0:
            break
        current_location = next_location

    tour.append(0)  # close the tour
    total_distance = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    print("Tour: ", tour)
    print("Total travel cost: {:.2f}".format(total_distance))
else:
    print("The problem does not have an optimal solution.")