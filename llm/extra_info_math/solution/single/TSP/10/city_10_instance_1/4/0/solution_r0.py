from math import sqrt
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Coordinates: city index mapped to (x, y)
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Number of cities
n = len(coordinates)

# Calculate Euclidean distance
def euclidean_distance(ci, cj):
    return sqrt((coordinates[ci][0] - coordinates[cj][0])**2 + (coordinates[ci][1] - coordinates[cj][1])**2)

# Creating distance matrix
distance_matrix = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Create a model
model = pyo.ConcreteModel()

# Sets of indices
model.I = pyo.RangeSet(0, n-1)
model.J = pyo.RangeSet(0, n-1)

# Decision variables
model.x = pyo.Var(model.I, model.J, domain=pyo.Binary)

# Objective function: minimize the total travel cost
def obj_rule(model):
    return sum(distance_matrix[i][j] * model.x[i,j] for i in model.I for j in model.J)
model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

# Constraints
# Each city must be left exactly once
def outflow_rule(model, i):
    return sum(model.x[i,j] for j in model.J if i != j) == 1
model.outflow = pyo.Constraint(model.I, rule=outflow_rule)

# Each city must be entered exactly once
def inflow_rule(model, j):
    return sum(model.x[i,j] for i in model.I if i != j) == 1
model.inflow = pyo.Constraint(model.J, rule=inflow_rule)

# Subtour elimination constraints (will use the lazy constraints approach at callback or a simple version using pyomo)
# Solve the model using a suitable solver
solver = SolverFactory('glpk')
result = solver.solve(model, tee=True)

# Extract the solution
tour = []
visited = 0
while True:
    for j in model.J:
        if pyo.value(model.x[visited, j]) == 1:
            tour.append(j)
            visited = j
            break
    if visited == 0:
        break

# Append the start point
tour.insert(0, 0)

# Calculate the total travel cost
total_cost = sum(pyo.value(model.x[i, j])*distance_matrix[i][j] for i in tour[:-1] for j in tour[1:])

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)