from scipy.spatial.distance import euclidean
from itertools import product
from ortools.linear_solver import pywraplp

# Coordinates of the cities
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

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Calculate distances
def calculate_distances(positions):
    distances = {}
    for (i, pos_i), (j, pos_j) in product(positions.items(), repeat=2):
        if i != j:
            distances[(i, j)] = euclidean(pos_i, pos_j)
    return distances

distances = calculate_distances(positions)

# Define the solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Create variables
x = {}
for i in positions.keys():
    for j in positions.keys():
        if i != j:
            x[(i, j)] = solver.BoolVar(f'x_{i}_{j}')

# Objective: Minimize the total travel cost
objective = solver.Objective()
for i, j in distances:
    objective.SetCoefficient(x[(i, j)], distances[(i, j)])
objective.SetMinimization()

# Constraints
# Each group must have exactly one outgoing and one incoming edge to/from a node outside the group
for group in groups:
    solver.Add(sum(x[(i, j)] for i in group for j in positions.keys() if j not in group) == 1)
    solver.Add(sum(x[(j, i)] for i in group for j in positions.keys() if j not in group) == 1)

# Conservation of flow
for i in positions.keys():
    solver.Add(sum(x[(j, i)] for j in positions.keys() if j != i) == sum(x[(i, j)] for j in positions.keys() if j != i))

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print(f'Total travel cost: {solver.Objective().Value()}')
    tour = []
    current_city = 0
    visited = set([0])
    tour.append(current_city)
    while len(visited) < len(positions):
        for j in positions.keys():
            if j not in visited and x[(current_city, j)].solution_value() > 0.5:
                tour.append(j)
                visited.add(j)
                current_city = j
                break
    tour.append(0)  # Returning to the depot
    print(f'Tour: {tour}')
else:
    print("The problem does not have an optimal solution.")