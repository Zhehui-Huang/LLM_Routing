import pyomo.environ as pyo
import numpy as np
from math import sqrt

# Define city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}
n = len(cities)  # Number of cities including the depot
m = 2  # Number of robots

# Calculate Euclidean distances
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Model definition
model = pyo.ConcreteModel()

# Variables
model.x = pyo.Var(((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), domain=pyo.Binary)
model.u = pyo.Var(range(1, n), domain=pyo.NonNegativeReals)

# Objective
model.obj = pyo.Objective(expr=sum(distances[i, j] * model.x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j), sense=pyo.minimize)

# Constraints
def visit_constraint(model, j):
    return sum(model.x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

model.visit = pyo.Constraint(range(1, n), rule=visit_constraint)

def unique_exit_entry_constraint(model, k, p):
    return sum(model.x[p, j, k] for j in range(n) if j != p) \
        == sum(model.x[i, p, k] for i in range(n) if i != p) == 1

model.unique_exit_entry = pyo.Constraint(range(m), range(n), rule=unique_exit_entry_constraint)

def leave_depot_constraint(model, k):
    return sum(model.x[0, j, k] for j in range(1, n)) == 1

model.leave_depot = pyo.Constraint(range(m), rule=leave_depot_constraint)

def subtour_elimination_constraint(model, i, j):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + n * sum(model.x[i, j, k] for k in range(m)) <= n - 1
    return pyo.Constraint.Skip

model.no_subtour = pyo.Constraint(range(n), range(n), rule=subtour_elimination_constraint)

# Solve the model
solver = pyo.SolverFactory('glpk')
result = solver.solve(model, tee=True)

# Extracting solution
tours = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j and pyo.value(model.x[i, j, k]) > 0.9:  # Small tolerance for binary
                tours[k].append((i, j))

# Convert to ordered tours starting at the depot
ordered_tours = {k: [0] for k in range(m)}
for k, tour in tours.items():
    current_city = 0
    while len(tour) > 0:
        for i, (fr, to) in enumerate(tour):
            if fr == current_city:
                ordered_tours[k].append(to)
                current_city = to
                tour.pop(i)
                break

# Include return to depot
for k in range(m):
    ordered_tours[k].append(0)

# Calculate costs
total_cost = 0
for k in range(m):
    cost = sum(distances[ordered_tours[k][i], ordered_tours[k][i+1]] for i in range(len(ordered_tours[k])-1))
    print(f"Robot {k} Tour: {ordered_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {cost}")
    total_cost += cost
print(f"Overall Total Travel Cost: {total">