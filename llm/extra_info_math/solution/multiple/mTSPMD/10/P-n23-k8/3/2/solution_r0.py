from ortools.linear_solver import pywraplp
from math import sqrt

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

depots = list(range(8))  # depots are cities from 0 to 7
num_robots = 8

# Calculate Euclidean distance between each pair of cities
def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create the distance matrix
dist_matrix = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        dist_matrix[i, j] = distance(coordinates[i], coordinates[j])

# Create the solver
solver = pywraplp.Solver.CreateSolver('CBC')

x = {}  # Binary variables indicating whether robot k travels from i to j
u = {}  # Continuous variables for subtour elimination

# Initialize variables
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        for k in depots:
            x[i, j, k] = solver.BoolVar(f'x[{i},{j},{k}]')
    u[i] = solver.IntVar(0, len(coordinates), f'u[{i}]')

# Objective function: Minimize the total cost of the tours
objective_terms = []
for k in depots:
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                objective_terms.append(dist_matrix[i, j] * x[i, j, k])
solver.Minimize(solver.Sum(objective_terms))

# Constraints

# Each customer node is visited exactly once
for j in range(8, len(coordinates)):  # start from 8, exclude depots
    solver.Add(sum(x[i, j, k] for i in range(len(coordinates)) for k in depots if i != j) == 1)

# Departure from each depot
for k in depots:
    solver.Add(sum(x[k, j, k] for j in range(len(coordinates)) if j != k) == 1)

# Arrival to each depot
for k in depots:
    solver.Add(sum(x[j, k, k] for j in range(len(coordinates)) if j != k) == 1)

# Maintain flow continuity
for k in depots:
    for i in range(len(coordinates)):
        if i != k:
            solver.Add(sum(x[i, j, k] for j in range(len(coordinates)) if j != i) ==
                       sum(x[j, i, k] for j in range(len(coordinates)) if j != i))

# Subtour elimination constraints
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            for k in depots:
                solver.Add(u[i] - u[j] + len(coordinates) * x[i, j, k] <= len(coordinates) - 1)

# Solve the model
status = solver.Solve()

# Output the results
if status == pywrapstmt.Solver.OPTIMAL:
    total_cost = solver.Objective().Value()
    print('Total cost of all tours:', totalx_cost)
    for k in depots:
        tour = [k]
        while True:
            for j in range(len(coordinates)):
                if j != tour[-1] and x[tour[-1], j, k].solution_value() == 1:
                    tour.append(j)
                    break
            if tour[-1] == k:
                break
        tour_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        print(f'Robot {k} Tour: {tour}')
        print(f'Robot {k} Total Travel Cost: {tour_cost}')
else:
    print('The problem does not have an optimal solution.')