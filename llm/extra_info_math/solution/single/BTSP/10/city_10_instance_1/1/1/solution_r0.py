import pyomo.environ as pyo
from math import sqrt

# Define city coordinates
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

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities)  # number of cities
dist = {(i, j): distance(i, j) for i in range(n) for j in range(n) if i != j}

# Pyomo model
model = pyo.ConcreteModel()

# Variables
model.x = pyo.Var(dist.keys(), domain=pyo.Binary)
model.z = pyo.Var(domain=pyo.NonNegativeReals)  # maximum distance variable

# Objective
model.obj = pyo.Objective(expr=model.z, sense=pyo.minimize)

# Constraints
model.constraints = pyo.ConstraintList()

# Degree constraints
for j in range(n):
    model.constraints.add(sum(model.x[i, j] for i in range(n) if (i, j) in dist) == 1)
    model.constraints.add(sum(model.x[j, k] for k in range(n) if (j, k) in dist) == 1)

# Subtour elimination and max distance constraints
def subtour_rule(model, S):
    if len(S) <= 1 or len(S) >= n:
        return pyo.Constraint.Skip
    return sum(model.x[i, j] for i in S for j in S if i != j) <= len(S) - 1

model.subtour_elimination = pyo.Constraint(powerset(range(1, n)), rule=subtour_rule)

for i, j in dist:
    model.constraints.add(model.z >= model.x[i, j] * dist[i, j])

# Solver and execution
solver = pyo.SolverFactory('cbc')
results = solver.solve(model)

# Extract solution
tour = [0]
if results.solver.status == pyo.SolverStatus.ok:
    current_city = 0
    while True:
        next_city = next(j for j in range(n) if model.x[current_city, j].value > 0.9)
        if next city == 0:
            break
        tour.append(next_city)
        current_city = next_city
    tour.append(0)  # return to the depot

# Calculate total travel cost and max distance
total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")