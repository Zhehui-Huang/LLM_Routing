import pyomo.environ as pyo
from math import sqrt

# Data
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Distance between cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Model
model = pyo.ConcreteModel()

# Sets
V = list(cities.keys())
P = list(range(len(groups)))
G = {p: group for p, group in enumerate(groups)}

# Variables
model.x = pyo.Var(V, V, within=pyo.Binary)
model.u = pyo.Var(P, within=pyo.NonNegativeReals)

# Objective
def obj_rule(m):
    return sum(distance(i, j) * m.x[i, j] for i in V for j in V if i != j)
model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

# Constraints
def exit_group_rule(m, p):
    return sum(m.x[i, j] for i in G[p] for j in V if j not in G[p]) == 1
model.exit_group_cons = pyo.Constraint(P, rule=exit_group_rule)

def enter_group_rule(m, p):
    return sum(m.x[j, i] for i in G[p] for j in V if j not in G[p]) == 1
model.enter_group_cons = pyo.Constraint(P, rule=enter_group_rule)

def flow_conservation_rule(m, i):
    return sum(m.x[j, i] for j in V if i != j) - sum(m.x[i, k] for k in V if i != k) == 0
model.flow_conservation = pyo.Constraint(V, rule=flow_conservation_rule)

# Solver
solver = pyo.SolverFactory('cbc')
result = solver.solve(model, tee=True)

# Extract solution
tour = [0]
visited = [0]
current = 0
while sum(model.x[current, j].value for j in V if j != current) > 0:
    next_city = next(j for j in V if j != current and pyo.value(model.x[current, j]) > 0.5)
    if next_city in visited:
        break
    tour.append(next_city)
    visited.append(next_city)
    current = next_city

tour.append(0)  # Return to depot

# Compute total cost
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)