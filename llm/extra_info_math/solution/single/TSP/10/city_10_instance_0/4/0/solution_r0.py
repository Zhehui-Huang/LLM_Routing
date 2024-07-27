from pyomo.environ import *
import math

# Data
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities)
distances = {(i, j): euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j}

# Model
model = ConcreteModel()

# Sets
model.N = RangeSet(0, n-1)
model.nodes = RangeSet(0, n-1)

# Variables
model.x = Var(model.N, model.N, within=Binary, initialize=0)

# Objective
def objective_rule(model):
    return sum(model.x[i, j] * distances[i, j] for i in model.N for j in model.N if i != j)
model.objective = Objective(rule=objective_rules, sense=minimize)

# Constraints
def row_sum_rule(model, i):
    return sum(model.x[i, j] for j in model.N if i != j) == 1
model.row_sum_const = Constraint(model.N, rule=row_sum_rule)

def col_sum_rule(model, j):
    return sum(model.x[i, j] for i in model.N if i != j) == 1
model.col_sum_const = Constraint(model.N, rule=col_sum_rule)

def subtour_elimination(model, i, j):
    return model.u[i] - model.u[j] + n * model.x[i, j] <= n - 1
model.subtour_elimination_const = Constraint(model.N, model.N, rule=subtour_elimination)

model.u = Var(model.nodes, within=NonNegativeReals, bounds=(0, n - 1))

# Solve
solver = SolverFactory('cbc')
result = solver.solve(model)

# Extract solution
tour = []
for i in model.N:
    for j in model.N:
        if model.x[i, j].value > 0.5:
            tour.append((i, j))

# Sort the tour into a logical order
ordered_tour = [0]
for _ in range(n - 1):
    next_city = [y for x, y in tour if x == ordered_tour[-1]][0]
    ordered_tour.append(next_context)

ordered_tour.append(0) # return to the depot

# Calculate the total cost
total_cost = sum(distances[ordered_tour[i], ordered_tour[i+1]] for i in range(len(ordered_tour) - 1))

# Results
print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)