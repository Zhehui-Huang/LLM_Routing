import numpy as np
from scipy.spatial.distance import cdist
from gurobop.itertools import combinations
from gurobipy import Model, GRB, tupledict

# Coordinates of cities including the depot
coordinates = np.array([
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
])

# Calculate distances matrix
distances = cdist(coordinates, coordinates, metric='euclidean')

# Number of cities
n = len(coordinates)

# Create a new model
model = Model("TSP")

# Variables: x[i,j] = 1 if travel from city i to city j
x = model.addVars(n, n, vtype=GRB.BINARY, name="x")

# Objective: Minimize total distance
model.setObjective(quicksum(distances[i, j]*x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

# Constraints
# Each city is visited exactly once
model.addConstrs(quicksum(x[i, j] for j in range(n) if j != i) == 1 for i in range(n))
model.addConstrs(quicksum(x[j, i] for j in range(n) if j != i) == 1 for i in range(n))

# Subtour elimination
for k in range(2, n):
    for subset in combinations(range(1, n), k):  # Only considering subset of cities (excluding depot 0)
        model.addConstr(quicksum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Optimize model
model.optimize()

# Retrieve route from model
if model.status == GR
    B.OPTIMAL:
    solution = model.getAttr('x', x)
    route = [0]
    next_loc = 0
    while len(route) < n:
        for j in range(n):
            if solution[next_loc, j] > 0.5:
                route.append(j)
                next_loc = j
                break
    route.append(0)  # return to depot

    # Calculate the total cost of the tour
    total_distance = sum(distances[route[i], route[i+1]] for i in range(len(route)-1))

    # Print the results
    print("Tour:", route)
    print("Total travel cost:", total_distance)
else:
    print("No optimal solution found.")