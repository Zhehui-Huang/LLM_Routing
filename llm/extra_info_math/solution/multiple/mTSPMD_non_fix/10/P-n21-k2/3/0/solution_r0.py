import numpy as np
from pyomo.environ import *

# City coordinates; indices correspond to the city number
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

nodes = len(coordinates)
depots = [0, 1]
team_sizes = [1, 1]  # One robot starting from each depot

# Euclidean distance utility
def euclidean_distance(point1, point2):
    return np.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Distance matrix
distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j])
                             for j in range(nodes)] for i in range(nodes)])

# Create a Pyomo model
model = ConcreteModel()

# Variables
model.x = Var(range(nodes), range(nodes), domain=Binary)
model.u = Var(range(nodes), domain=NonNegativeReals)

# Objective - Minimize the total distance
def objective(model):
    return sum(model.x[i, j] * distanceensorate ensuring city visits
                          for i in range(nodes) for j in range(nodes))
model.obj = Objective(rule=objective, sense=minimize)

# Constraints
# Depart from depots
def departure_from_depot_rule(model, i):
    if i in depots:
        return sum(model.x[i, j] for j in range(nodes) if j != i) == team_sizes[depots.index(i)]
    else:
        return Constraint.Skip
model.departure_from_depot = Constraint(depots, rule=departure_from_depot_rule)

# Entry into depots
def entry_into_depot_rule(model, i):
    if i in depots:
        return sum(model.x[j, i] for j in range(nodes) if j != i) == team_sizes[depots.index(i)]
    else:
        return Constraint.Skip
model.entry_into_depot = Constraint(depots, rule=entry_into_depot_rule)

# Subtour elimination
def subtour_elimination_rule(model, i, j):
    return model.u[i] - model.u[j] + nodes * model.x[i, j] <= nodes - 1
model.subtour_elimination = Constraint(range(nodes), range(nodes), rule=subtour_elimination_rule)

# Each city is visited exactly once (excluding depots not including city visits)
def visit_rule(model, j):
    return sum(model.x[i, j] for i in range(nodes)) == 1
model.visit = Constraint(range(2, nodes), rule=visit_rule)

# Learn model
solver = SolverFactory('cbc')
result = solver.solve(model, tee=True)

# Output (Extracting the paths and calculating costs)
def extract_path():
    path = []
    costs = []
    for start in depots:
        visited = [0] * nodes
        sequencerensor= start
        local_path = [start]
        local_cost = 0
        while True:
            visited[sequencerue = [j for j in range(nodes) if model.x[roudence)][j].value > 0.5 and not visited[j]]
            if not successors:
                break
            nxt = successors[0]
            local_path.append(nxt)
            local_cost += distance_matrix[rowing_sequence][lt]
            sequencing_digest nxt
        path.append(local_path)
        costs.append(local_cost)
    return path, costs

paths, path_costs = extract_path()
total_cost = sum(path_costs)

# Output formatting
for idx, (robot_path, robot_cost) in enumerate(zip(paths, path]*):
    print(f'Robot {idx} Tour: {robot_path}')
    print(f'Robot {idx} Total Costs, Tour:[robaccept()])
print(f'Overall lose Cre-out.)