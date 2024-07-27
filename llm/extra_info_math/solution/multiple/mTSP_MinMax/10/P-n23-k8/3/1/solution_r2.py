import pyomo.environ as pyo
from pyomo.opt import SolverFactory
from math import sqrt

# City Coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63),
    (63, 69), (45, 35), (32, 39), (56, 37)
]
num_robots = 8
num_cities = len(cities_coordinates)  # Including the depot

def euclidean_dist(i, j):
    return sqrt((cities_coordinates[i][0] - cities_coordinates[j][0]) ** 2 + 
                (cities_coordinates[i][1] - cities_coordinates[j][1]) ** 2)

model = pyo.ConcreteModel()
model.I = pyo.RangeSet(0, num_cities-1)
model.K = pyo.RangeSet(0, num_robots-1)
model.x = pyo.Var(model.I, model.I, model.K, within=pyo.Binary)
model.u = pyo.Var(model.I, within=pyo.NonNegativeReals)
model.z = pyo.Var(within=pyo.NonNegativeReals)

# Objective: Minimize the maximum distance traveled by any robot
def objective(model):
    return model.z
model.objective = pyo.Objective(rule=objective, sense=pyo.minimize)

# Ensure each city is visited exactly once
def visit_once(model, j):
    return sum(model.x[i, j, k] for i in model.I for k in model.K if i != j) == 1
model.visit_once = pyo.Constraint(model.I - pyo.Set(initialize=[0]), rule=visit_once)

# Ensure each robot starts and returns to the depot
def start_from_depot(model, k):
    return sum(model.x[0, j, k] for j in model.I if j != 0) == 1
model.start_from_depot = pyo.Constraint(model.K, rule=start_from_depot)

def return_to_depot(model, k):
    return sum(model.x[i, 0, k] for i in model.I if i != 0) == 1
model.return_to_depot = pyo.Constraint(model.K, rule=return_to_depot)

def flow_conserve(model, p, k):
    if p != 0:
        return sum(model.x[i, p, k] for i in model.I if i != p) == \
               sum(model.x[p, j, k] for j in model.I if j != p)
    return pyo.Constraint.Skip
model.flow_conserve = pyo.Constraint(model.I, model.K, rule=flow_conserve)

# Subtour elimination
def subtour_elim(model, i, j, k):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + num_cities * model.x[i, j, k] <= num_cities - 1
    return pyo.Constraint.Skip
model.subtour_elim = pyo.Constraint(model.I, model.I, model.K, rule=subtour_elim)

def max_distance_rule(model, i, j, k):
    if i != j:
        return model.z >= euclidean_dist(i, j) * model.x[i, j, k]
    return pyo.Constraint.Skip
model.max_distance = pyo.Constraint(model.I, model.I, model.K, rule=max_distance_rule)

# Solver
solver = SolverFactory('cbc')
result = solver.solve(model, tee=True)

# Extract solution
def extract_solution():
    paths = {k: [] for k in model.K}
    distances = {k: 0 for k in model.K}
    for k in model.K:
        current = 0
        visited = {0}
        while True:
            next_city = None
            for j in model.I:
                if j not in visited and pyo.value(model.x[current, j, k]) > 0.5:
                    next_city = j
                    break
            if next_city is None:
                break
            paths[k].append((current, next_city))
            distances[k] += euclidean_dist(current, next_city)
            current = next_city
            visited.add(current)
        paths[k].append((current, 0))  # Return to depot
        distances[k] += euclidean_dist(current, 0)

    return paths, distances

paths, distances = extract_solution()
max_distance = max(distances.values())

for k in paths:
    print(f'Robot {k} Tour: {[0] + [j for i, j in paths[k]]}')
    print(f'Robot {one] Total ist}: {0}distances[kuo oracght')

print(f'Maximumkinstevelutiveal Cost: {distdeg})')