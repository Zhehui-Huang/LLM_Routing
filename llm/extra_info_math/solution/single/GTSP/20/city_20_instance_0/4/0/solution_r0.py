from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, RangeSet, NonNegativeReals, Binary
from math import sqrt

# Define the cities and their coordinates
coordinates = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Define city groups
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate distances between each pair of cities
def euclidean_distance(c1, c2):
    return sqrt((coordinates[c1][0] - coordinates[c2][0])**2 + (coordinates[c1][1] - coordinates[c2][1])**2)

# Model
model = ConcreteModel()

# Sets
model.V = RangeSet(0, 19)
model.Pairs = model.V * model.V

# Variables
model.x = Var(model.Pairs, within=Binary)
model.u = Var(model.V, within=NonNegativeReals)

# Objective
def obj_rule(m):
    return sum(model.x[i, j] * euclidean_distance(i, j) for i in m.V for j in m.V if i != j)
model.obj = Objective(rule=obj_rule, sense=minimize)

# Constraints
def exit_group_rule(m, p):
    return sum(model.x[i, j] for i in groups[p] for j in m.V if j not in groups[p]) == 1
model.exit_group = Constraint(range(len(groups)), rule=exit_group_rule)

def enter_group_rule(m, p):
    return sum(model.x[j, i] for i in groups[p] for j in m.V if j not in groups[p]) == 1
model.enter_group = Constraint(range(len(groups)), rule=enter_group_rule)

def flow_conservation_rule(m, i):
    return sum(model.x[j, i] for j in m.V if j != i) == sum(model.x[i, j] for j in m.V if j != i)
model.flow_conservation = Constraint(model.V, rule=flow_conservation_rule)

def subtour_elimination_rule(m, i, j):
    if i != j and i != 0 and j != 0:
        return m.u[i] - m.u[j] + len(m.V) * model.x[i, j] <= len(m.V) - 1
    return Constraint.Skip
model.subtour_elimination = Constraint(model.V, model.V, rule=subtour_elimination_rule)

# Solver
solver = SolverFactory('cbc')
result = solver.solve(model)

# Output tour and cost
tour = []
visited = set([0])
current = 0
while True:
    for next_city in range(20):
        if current != next_city and model.x[current, next_city].value == 1:
            tour.append(next_city)
            current = next_city
            visited.add(next_city)
            break
    if current == 0:
        break

tour = [0] + tour + [0]

print("Tour:", tour)
print("Total travel cost:", model.obj())