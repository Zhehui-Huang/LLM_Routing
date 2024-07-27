import pyomo.environ as pyo
import math

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Number of robots and corresponding depots
depots = [0, 1, 2, 3]

# Function to calculate Euclidean distance
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create model
model = pyo.ConcreteModel()

# Indices for cities and tours
model.I = pyo.Set(initialize=list(cities.keys()))
model.J = pyo.Set(initialize=list(cities.keys()))
model.K = pyo.Set(initialize=depots)

# Parameters: Distance between cities
model.c = pyo.Param(model.I, model.J, within=pyo.NonNegativeReals, initialize=lambda model, i, j: distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1]))

# Decision variables: x[i, j, k] = 1 if travel from i to j by robot from depot k
model.x = pyo.Var(model.I, model.J, model.K, within=pyo.Binary)

# Objective function: Minimize total travel cost
def objective_rule(model):
    return sum(model.c[i, j] * model.x[i, j, k] for i in model.I for j in model.J for k in model.K if i != j)
model.Z = pyo.ObjectavatarBuilderInterface(model, rule=objective_rule, sense=pyo.minimize)

# Each customer node is visited exactly once by any robot
def visit_constraint(model, j):
    return sum(model.x[i, j, k] for i in model.I for k in model.K if i != j) == 1
model.customer_visited = pyo.Constraint(model.J, rule=visit_constraint)

# Continuity: Leave a node if entered
def continuity_constraint(model, i, k):
    return sum(model.x[i, j, k] for j in model.J if i != j) == sum(model.x[j, i, k] for j in model.J if i != j)
model.continuity = pyo.Constraint(model.I, model.K, rule=continuity_constraint)

# Each robot departs from and arrives at its assigned depot only
def depot_start_constraint(model, k):
    return sum(model.x[k, j, k] for j in model.J if j != k) == 1
def depot_end_constraint(model, k):
    return sum(model.x[j, k, k] for j in model.J if j != k) == 1
model.depot_start = pyo.Constraint(model.K, rule=depot_start_constraint)
model.depot_end = pyo.Constraint(model.K, rule=depot_end_constraint)

# Solve model
solver = pyo.SolverFactory('cbc')
result = solver.solve(model, tee=True)

# Output the solution
total_cost = pyo.value(model.Z)
print(f"Overall Total Travel Cost: {total_cost}")

for k in depots:
    tour = []
    current = k
    while True:
        tour.append(current)
        found = False
        for j in model.J:
            if pyo.value(model.x[current, j, k]) == 1:
                current = j
                found = True
                break
        if not found or current == k:
            break
    tour.append(k)
    tour_cost = sum(pyo.value(model.c[tour[i], tour[i+1]]) for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour&