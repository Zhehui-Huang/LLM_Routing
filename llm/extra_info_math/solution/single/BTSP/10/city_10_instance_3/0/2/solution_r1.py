import pyomo.environ as pyo
from pyomo.environ import *
from math import sqrt

# Coordinates for the cities
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Number of cities
n = len(coordinates)

def euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Model
model = pyo.ConcreteModel()

# Indices for cities
model.N = range(n)
model.arcs = distances.keys()

# Variables
model.x = pyo.Var(model.arcs, within=Binary)
model.u = pyo.Var(model.N, within=NonNegativeReals)

# Objective
def obj_rule(model):
    return max(model.x[i, j] * distances[i, j] for i, j in model.arcs)
model.obj = pyo.Objective(rule=obj_rule, sense=minimize)

# Constraints
def rule_constrain_from(model, i):
    return sum(model.x[i, j] for j in model.N if (i, j) in model.arcs) == 1
model.con_from = pyo.Constraint(model.N, rule=rule_constrain_from)

def rule_constrain_to(model, j):
    return sum(model.x[i, j] for i in model.N if (i, j) in model.arcs) == 1
model.con_to = pyo.Constraint(model.N, rule=rule_constrain_to)

# Subtour elimination constraint
def subtour_elimination(model, i, j):
    if i != j and (i != 0 and j != 0) and (i, j) in model.arcs:
        return model.u[i] - model.u[j] + model.x[i, j] * (n - 1) <= n - 2
    else:
        return Constraint.Skip
model.subtour_elim = pyo.Constraint(model.N, model.N, rule=subtour_elimination)

# Optimize
opt = pyo.SolverFactory('cbc')
results = opt.solve(model)

# Output the results
tour = []
for i in model.N:
    for j in model.N:
        if (i, j) in model.arcs and pyo.value(model.x[i, j]) == 1:
            tour.append((i, j))

# Fix the tour order
ordered_tour = [0]
for _ in range(n-1):
    last = ordered_tour[-1]
    next_city = next(j for i, j in tour if i == last)
    ordered_tour.append(next_city)

ordered_tour.append(0)  # complete the tour back to the depot

# Calculate the total cost and max distance
total_cost = sum(distances[i, j] for i, j in zip(ordered_tour[:-1], ordered_tour[1:]))
max_distance = max(distances[i, j] for i, j in zip(ordered_tour[:-1], ordered_tour[1:]))

print(f"Tour: {ordered_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")