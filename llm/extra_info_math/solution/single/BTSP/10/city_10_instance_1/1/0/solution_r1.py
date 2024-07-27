import pyomo.environ as pyo
import math
from itertools import combinations

# City coordinates
cities = {
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

n = len(cities)  # number of cities

# Calculate distances
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

model = pyo.ConcreteModel()

model.Nodes = pyo.RangeSet(0, n-1)
model.x = pyo.Var(model.Nodes, model.Nodes, within=pyo.Binary)
model.z = pyo.Var(within=pyo.NonNegativeReals)

def max_distance_rule(model):
    return model.z
model.max_distance = pyo.Objective(rule=max_distance_rule, sense=pyo.minimize)

def enter_rule(model, j):
    if j != 0:
        return sum(model.x[i, j] for i in model.Nodes if i != j) == 1
    return pyo.Constraint.Skip
model.enter = pyo.Constraint(model.Nodes, rule=enter_rule)

def leave_rule(model, i):
    if i != 0:
        return sum(model.x[i, j] for j in model.Nodes if i != j) == 1
    return pyo.Constraint.Skip
model.leave = pyo.Constraint(model.Nodes, rule=leave_rule)

def max_dist_rule(model, i, j):
    return model.z >= model.x[i, j] * distances[i][j]
model.max_dist_constraint = pyo.Constraint(model.Nodes, model.Nodes, rule=max_dist_rule)

def subtour_elim_rule(model, S):
    return sum(model.x[i, j] for i in S for j in S if i != j) <= len(S) - 1
model.subtour_elimination = pyo.ConstraintList()
for r in range(3, n):
    for S in combinations(model.Nodes, r):
        model.subtour_elimination.add(subtour_elim_rule(model, S))

solver = pyo.SolverFactory('cbc')
result = solver.solve(model)

def get_solution():
    route = [0]
    while True:
        next_city = next(j for j in model.Nodes if pyo.value(model.x[route[-1], j]) == 1)
        if next_city == 0:
            break
        route.append(next_city)
    route.append(0) # return to the starting city
    longest_dist = max(distances[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
    return route, total_cost, longest_dist

tour, total_cost, max_dist = get_solution()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")