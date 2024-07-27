import pyomo.environ as pyo
import math
from scipy.spatial.distance import euclidean

# City coordinates as given
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

# Calculate distances between each pair of nodes
distances = [[math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
              for j in range(n)] for i in range(n)]

# Optimization model
model = pyo.ConcreteModel()

# Sets of nodes
model.N = pyo.RangeSet(0, n-1)
model.Nodes = pyo.Set(initialize=model.N)

# Decision variables: x[i,j] is 1 if travel between node i and j, otherwise 0
model.x = pyo.Var(model.Nodes, model.Nodes, within=pyo.Binary)

# The maximum distance variable
model.z = pyo.Var(within=pyo.NonNegativeReals)

# Objective: minimize the maximum distance in the tour
def objective_rule(model):
    return model.z
model.obj = pyo.Objective(rule=objective_rule, sense=pyo.minimize)

# Constraint: Enter each city exactly once
def enter_constraint_rule(model, j):
    return sum(model.x[i, j] for i in model.Nodes if i != j) == 1
model.enter_constraint = pyo.Constraint(model.Nodes, rule=enter_constraint_rule)

# Constraint: Leave each city exactly once
def leave_constraint_rule(model, i):
    return sum(model.x[i, j] for j in model.Nodes if i != j) == 1
model.leave_constraint = pyo.Constraint(model.Nodes, rule=leave_commit_constraint_rule)

# Sub-tour elimination
def subtour_elimination_rule(model, S):
    return sum(model.x[i, j] for i in S for j in S if i != j) <= len(S) - 1
model.subtour_elimination = pyo.ConstraintList()
for S in range(2, n):
    model.subtour_elimination.add(expr=subtour_elimination_rule(model, S))

# Maximum distance constraint
def max_distance_rule(model, i, j):
    return model.z >= distances[i][j] * model.x[i, j]
model.max_distance_constraint = pyo.Constraint(model.Nodes, model.Nodes, rule=max_distance_rule)

# Solver options
solver = pyo.SolverFactory('cbc')
results = solver.solve(model, tee=True)

def get_tour_and_metrics(solution_model):
    tour = []
    current_city = 0
    while True:
        next_city = [j for j in model.Nodes if pyo.value(solution_model.x[current_city, j]) == 1 and current_city != j][0]
        tour.append(current_city)
        if next_city == 0:
            tour.append(next_city)
            break
        else:
            current_city = next_city

    max_distance = pyo.value(solution_model.z)
    total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    return tour, total_distance, max_distance

# Extract the results
tour, total_cost, max_dist = get_tour_and_metrics(model)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")