from scipy.spatial.distance import euclidean
from ortools.linear_solver import pywraplp

# Define the positions of cities
positions = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities each group must be visited once
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Compute distances
distances = {}
for i in positions:
    for j in positions:
        if i != j:
            distances[(i, j)] = euclidean(positions[i], positions[j])

# Create a solver instance
solver = pywraplp.Solver.CreateSolver('CBC')

# Variable creation: x[(i, j)] = 1 if the path goes from i to j
x = {}
for i in positions:
    for j in positions:
        if i != j:
            x[(i, j)] = solver.BoolVar(f'x_{i}_{j}')

# Objective function: Minimize total distance
objective = solver.Objective()
for i, j in distances:
    objective.SetCoefficient(x[(i, j)], distances[(i, j)])
objective.SetMinimization()

# Add constraints
# Constraint per group to ensure exactly one node from each group is visited
for group in groups:
    # Exactly one outgoing edge to the rest of the network
    solver.Add(solver.Sum(x[i, j] for i in group for j in positions if j not in group) == 1)
    # Exactly one incoming edge from the rest of the network
    solver.Add(solver.Sum(x[j, i] for i in group for j in positions if j not in group) == 1)

# Flow conservation at each city
for i in positions:
    solver.Add(solver.Sum(x[j, i] for j in positions if j != i) ==
               solver.Sum(x[i, j] for j in positions if j != i))

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Solution:")
    print("Objective value =", solver.Objective().Value())
    path = []
    for i in positions:
        for j in positions:
            if i != j and x[i, j].solution_value() > 0.5:
                path.append((i, j))
    print("Path:", path)
else:
    print("The problem does not have an optimal solution.")