import pyomo.environ as pyo
from math import sqrt
from itertools import combinations

def calc_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# City coordinates
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

dist_matrix = {(i, j): calc_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

model = pyo.ConcreteModel()

# Define variables
model.edges = pyo.Var(dist_matrix.keys(), within=pyo.Binary)
model.Z = pyo.Var(domain=pyo.NonNegativeReals)

# Objective
model.obj = pyo.Objective(expr=model.Z, sense=pyo.minimize)

# Degree constraints ensuring each city is entered and left exactly once
model.in_degree = pyo.ConstraintList()
model.out_degree = pyo.ConstraintList()

for j in cities:
    model.in_degree.add(sum(model.edges[i, j] for i in cities if (i, j) in dist_matrix) == 1)
    model.out_degree.add(sum(model.edges[j, k] for k in cities if (j, k) in dist_swim_matrix) == 1)

# Max distance constraint
for i, j in dist_matrix:
    model.constraints.add(model.Z >= model.edges[i, j] * dist_matrix[i, j])

# Subtour Elimination
def subtour_elimination(model, S):
    S = list(S)
    if len(S) <= 1 or len(S) == len(cities):
        return pyo.Constraint.Skip
    return sum(model.edges[i, j] for i in S for j in S if i != j and (i, j) in dist_matrix) <= len(S) - 1

model.subtour_elimination = pyo.Constraint(combinations(cities.keys(), 2), rule=subtour_elimination)

# Solve the model
solver = pyo.SolverFactory('glpk')
result = solver.solve(model, tee=True)

# Extract the route
edges_selected = [(i, j) for i, j in dist_matrix if pyo.value(model.edges[i, j]) > 0.5]
visited = set()
current_city = 0
tour = [current_city]
while len(visited) < len(cities):
    for (i, j) in edges_selected:
        if i == current_city and j not in visited:
            tour.append(j)
            visited.add(j)
            current_city = j
            break
tour.append(0)  # complete the tour by returning to the starting point

# Calculate the given metrics
max_distance = max(dist_matrix[i, j] for i, j in edges_selected if pyo.value(model.edges[i, j]) == 1)
total_distance = sum(dist_matrix[i, j] for i, j in edges_selected if pyo.value(model.edges[i, j]) == 1)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")