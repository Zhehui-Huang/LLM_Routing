from math import sqrt
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Coordinates of cities
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

# Creating a Pyomo model
model = pyo.ConcreteModel()

# Indices of cities
model.I = pyo.RangeSet(0, n-1)
model.J = pyo.RangeSet(0, n-1)

# Decision variables
model.x = pyo.Var(model.I, model.J, domain=pyo.Binary)

# Objective function to minimize total distance
def obj_func(model):
    return sum(distance_matrix[i][j] * model.x[i, j] for i in model.I for j in model.J)
model.obj = pyo.Objective(rule=obj_func, sense=pyo.minimize)

# Constraints
# Each city is left exactly once
def leave_once(model, i):
    return sum(model.x[i, j] for j in model.J if j != i) == 1
model.leave_constraints = pyo.Constraint(model.I, rule=leave_once)

# Each city is visited exactly once
def visit_once(model, j):
    return sum(model.x[i, j] for i in model.I if i != j) == 1
model.visit_constraints = pyo.Constraint(model.J, rule=visit_once)

# Eliminate sub-tours using the MTZ constraints
model.u = pyo.Var(model.I, within=pyo.NonNegativeReals, bounds=(0, n-1))
def subtour_elimination(model, i, j):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + n * model.x[i, j] <= n-1
    else:
        return model.u[i] - model.u[j] + n * model.x[i, j] <= n
model.subtour_constraints = pyo.Constraint(model.I, model.J, rule=subtour_elimination)

# Solve the model
solver = SolverFactory('glpk')
result = solver.solve(model, tee=True)

# Extract the solution
tour = []
current_city = 0
next_city = None

while True:
    next_city = next(j for j in model.J if pyo.value(model.x[current_city, j]) == 1)
    tour.append(next_city)
    if next_city == 0:
        break
    current_city = next_city

# Append the depot start point
tour.insert(0, 0)

# Compute the total tour cost
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total Travel Cost:", total_cost)