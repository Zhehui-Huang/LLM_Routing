import numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Define your data
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
          (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
n = len(coords)
m = 2

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p1[1])**2)

dist_matrix = {(i, j): euclidean_distance(coords[i], coords[j]) for i in range(n) for j in range(n) if i != j}

# Create a Concrete Model
model = ConcreteModel()

# Create sets
model.I = RangeSet(0, n-1)  # Set of nodes including depot
model.N = RangeSet(1, n-1)  # Set of nodes excluding depot
model.K = RangeMax = max_dist

# Variables
model.x = Var(model.I, model.I, model.K, within=Binary)
model.u = Var(model.N, within=NonNegativeReals)
model.max_dist = Var(within=NonNegativeReals)

# Objective
model.obj = Objective(expr=model.max_dist, sense=minimize)

# Constraints
def each_city_only_once_rule(m, j):  # Each city except the depot is visited exactly once
    return sum(m.x[i, j, k] for i in m.I for k in m.K if i != j) == 1
model.each_city_only_once = Constraint(model.N, rule=each_city_only_once_rule)

def exit_depot_rule(m, k):  # Each vehicle leaves the depot
    return sum(m.x[0, j, k] for j in m.N) == 1
model.exit_depot = Constraint(model.K, rule=exit_depot_rule)

def enter_depot_rule(m, k):  # Each vehicle enters the depot
    return sum(m.x[j, 0, k] for j in m.N) == 1
model.enter_depot = Constraint(model.K, rule=enter_depot_rule)

def salesman_leaves_city_rule(m, k, i):  # Each salesman leaves each city
    if i != 0:
        return sum(m.x[i, j, k] for j in m.I if j != i) == sum(m.x[j, i, k] for j in m.I if j != i)
    return Constraint.Skip
model.salesman_leaves_city = Constraint(model.K, model.I, rule=salesman_leaves_city_rule)

def subtour_elimination_rule(m, i, j, k):
    if i != j:
        return m.u[i] - m.u[j] + n * m.x[i, j, k] <= n - 1
    return Constraint.Skip
model.subtour_elimination = Constraint(model.N, model.N, model.K, rule=subtour_elimination_rule)

def max_distance_rule(m, k):  # Maximize the tour distance
    return sum(m.x[i, j, k] * dist_matrix[i, j] for i in m.I for j in m.I if i != j) <= m.max_dist
model.distance_constraint = Constraint(model.K, rule=max_distance_rule)

# Solver
solver = SolverFactory('glpk')
results = solver.solve(model, tee=True)

# Extract solution
if results.solver.status == SolverStatus.ok:
    for k in model.K:
        tour = [0]
        current = 0
        while True:
            for j in model.I:
                if j != current and model.x[current, j, k]() > 0.5:
                    tour.append(j)
                    current = j
                    break
            if current == 0:
                break
        print(f"Robot {k} Tour: {tour}")
        tour_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    max_cost = max(sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1)) for tour in tours)
    print(f'Maximum Travel Cost: {max_cost}')
else:
     print("No valid solution found")