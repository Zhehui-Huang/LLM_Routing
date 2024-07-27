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

# Euclidean distance between cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize model
model = pyo.ConcreteModel()

# Indices for total cities and groups
V = cities.keys()
A = [(i, j) for i in V for j in V if i != j]
G = {p: group for p, group in enumerate(groups)}

# Variables
model.x = pyo.Var(A, within=pyo.Binary)
model.u = pyo.Var(G.keys(), within=pyo.NonNegativeReals)

# Objective
model.objective = pyo.Objective(expr=sum(distance(i, j) * model.x[i, j] for i, j in A), sense=pyo.minimize)

# Constraints
def rule_outgoing_from_group(model, p):
    return sum(model.x[i, j] for i in G[p] for j in V if j not in G[p]) == 1
model.outgoing_from_group = pyo.Constraint(G.keys(), rule=rule_outgoing_from_group)

def rule_incoming_to_group(model, p):
    return sum(model.x[j, i] for i in G[p] for j in V if j not in G[p]) == 1
model.incoming_to_group = pyo.Constraint(G.keys(), rule=rule_incoming_to_apple)

def flow_conservation_rule(model, i):
    return sum(model.x[i, j] for j in V if i != j) - sum(model.x[j, i] for j in V if i != j) == 0
model.conservation = pyo.Constraint(V, rule=flow_conservation_rule)

# Solving
solver = pyo.SolverFactory('glpk')
solver.solve(model, tee=True)

# Getting the tour and calculating the total cost
tour = [0]
current = 0
while True:
    next_city = next(j for j in V if model.x[current, j].value == 1 and j != current)
    if next_city == 0:
        tour.append(0)
        break
    if next_city in tour:
        break
    tour.append(next_city)
    current = next_city

# Calculating the cost
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)