import numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Coordinates data
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
          (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
n = len(coords)
m = 2

def calc_dist(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

dist_matrix = {(i, j): calc_dist(coords[i], coords[j]) for i in range(n) for j in range(n) if i != j}
model = ConcreteModel()

# Sets
model.N = RangeSet(0, n-1)
model.M = RangeSet(0, m-1)

# Variables
model.x = Var(model.N, model.N, model.M, within=Binary)
model.u = Var(model.N, within=NonNegativeReals, bounds=(0, n-1))
model.max_distance = Var(within=NonNegativeReals)

# Objective
def objective_rule(model):
    return model.max_distance
model.objective = Objective(rule=objective_rule, sense=minimize)

# Constraints
def only_one_exit_rule(model, k):
    return sum(model.x[0, j, k] for j in model.N if j != 0) == 1
model.only_one_exit = Constraint(model.M, rule=only_one_exit_rule)

def only_one_return_rule(model, k):
    return sum(model.x[j, 0, k] for j in model.N if j != 0) == 1
model.only_one_return = Constraint(model.M, rule=only_one_return_rule)

def visit_each_city_once_rule(model, j):
    return sum(model.x[i, j, k] for i in model.N for k in model.M if i != j) == 1
model.visit_each_city_once = Constraint(model.N, rule=visit_each_city_once_rule)

def leave_each_city_once_rule(model, k, i):
    if i != 0:
        return (sum(model.x[i, j, k] for j in model.N if i != j) ==
                sum(model.x[j, i, k] for j in model.N if i != j))
    else:
        return Constraint.Skip
model.leave_each_city_once = Constraint(model.M, model.N, rule=leave_each_city_once_rule)

def subtour_elimination_rule(model, i, j, k):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + n * model.x[i, j, k] <= n - 1
    else:
        return Constraint.Skip
model.subtour_elimination = Constraint(model.N, model.N, model.M, rule=subtour_elimination_rule)

# Max distance definition
def max_distance_rule(model, k):
    return sum(model.x[i, j, k] * dist_matrix[i, j] for i in model.N for j in model.N if i != j) <= model.max_distance
model.max_distance_def = Constraint(model.M, rule=max_distance_rule)

# Solve
solver = SolverFactory('glpk')
results = solver.solve(model)

# Output
def get_tours(model):
    for k in model.M:
        tour = [0]
        current = 0
        while True:
            next_city = None
            for j in model.N:
                if j != current and model.x[current, j, k].value > 0.5:
                    next_city = j
                    tour.append(next_city)
                    break
            if next_city == 0:
                break
            else:
                current = next_city
        yield tour

tour_costs = []
for tour in get_tours(model):
    tour_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    tour_costs.append((tour, tour_cost))
    print(f"Tour: {tour} Cost: {tour_cost}")

max_cost = max(cost for _, cost in tour_costs)
print(f"Maximum Travel Cost: {max_cost}")