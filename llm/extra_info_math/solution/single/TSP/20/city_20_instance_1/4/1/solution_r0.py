from ortools.linear_solver import pywraplp
import math

# City coordinates as provided, with the depot city at index 0
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Calculate Euclidean distance between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

n = len(coordinates)  # Total number of cities including the depot
cost = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

solver = pywraplp.Solver.CreateSolver('SCIP')

# Variables: x[i, j] = 1 if route goes from city i to city j
x = {}
for i in range(n):
    for j in range(n):
        if i != j:  # No loops
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# Objective: Minimize the total distance traveled
objective = solver.Objective()
for i in range(n):
    for j in range(n):
        if i != j:
            objective.SetCoefficient(x[i, j], cost[i][j])
objective.SetMinimization()

# Constraints
# Each city must be left exactly once
for i in range(n):
    solver.Add(sum(x[i, j] for j in range(n) if i != j) == 1)

# Each city must be entered exactly once
for j in range(n):
    solver.Add(sum(x[i, j] for i in range(n) if i != j) == 1)

# Subtour elimination constraints (Using Miller-Tucker-Zemlin formulation)
u = []
for i in range(n):
    u.append(solver.IntVar(0.0, n - 1, f'u[{i}]'))

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            solver.Add(u[i] - u[j] + n * x[i, j] <= n - 1)

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Found optimal solution!')

    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and x[i, j].solution_value() > 0.5:
                tour.append((i, j))

    # Find the tour order
    ordered_tour = [0]
    current_city = 0
    while len(ordered_tour) < n:
        for k in tour:
            if k[0] == current_city:
                ordered_tour.append(k[1])
                current_city = k[1]
                break

    ordered_tour.append(0)  # Going back to the depot

    total_cost = sum(cost[ordered_tour[k]][ordered_tour[k + 1]] for k in range(len(ordered_tour) - 1))

    print(f"Tour: {ordered_tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("Solver did not find an optimal solution.")