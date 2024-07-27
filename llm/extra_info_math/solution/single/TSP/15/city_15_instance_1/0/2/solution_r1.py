import numpy as. np
from scipy.spatial.distance import cdist
import itertools
from gurobipy import Model, GRB, quicksum

# Coordinates of cities including the depot
coordinates = np.array([
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
])

# Calculate distances matrix
distances = cdist(coordinates, coordinates, metric='euclidean')

# Create a model
m = Model("TSP")

# Number of cities
n = distances.shape[0]

# Create variables: x[i, j] = 1 if route goes from i to j
x = m.addVars(n, n, vtype=GRB.BINARY, name="x")

# Set objective: minimize the total travel distance
m.setObjective(quicksum(distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j), GRB.MINIMIZE)

# Constraint: Each city is entered and left exactly once
m.addConstrs((quicksum(x[i, j] for j in range(n) if j != i) == 1 for i in range(n)), "leave")
m.addConstrs((quicksum(x[j, i] for j in range(n) if j != i) == 1 for i in range(n)), "enter")

# Subtour elimination constraints (SEC) using lazy constraints
def subtour_elimination(model, where):
    if where == GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        tours = []
        for i in range(n):
            tour = []
            start = i
            while True:
                tour.append(start)
                start = [j for j in range(n) if vals[start, j] > 0.5][0]  # Go to next city
                if start == i:
                    break
            if len(tour) < n:
                break
        if len(tour) < n:
            model.cbLazy(quicksum(model._vars[i, j] for i in tour for j in tour if i != j) <= len(tour) - 1)

m._vars = x
m.Params.lazyConstraints = 1
m.optimize(subtour_elimination)

# Extract tour order from decision variables and calculate total travel cost
tour = []
current = 0
total_cost = 0
for _ in range(n):
    next_city = [j for j, var in enumerate(x.select(current, '*')) if var.X > 0.5][0]
    total_cost += distances[current, next_city]
    tour.append(current)
    current = next_city
    if current == 0:
        break

# Append the depot city at the end of the tour
tour.append(0)

# Output the required result
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")