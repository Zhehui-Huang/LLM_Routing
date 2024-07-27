# Import required packages
from pyomo.environ import *
import numpy as np

# Coordinates of cities including the depot
cities = np.array([
    [50, 42],  # Depot
    [41, 1],
    [18, 46],
    [40, 98],
    [51, 69],
    [47, 39],
    [62, 26],
    [79, 31],
    [61, 90],
    [42, 49]
])

# Number of cities
n = len(cities)

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Model
model = ConcreteModel()

# Indices
model.cities = RangeSet(0, n-1)

# Decision variables
model.x = Var(model.cities, model.cities, within=Binary)

# Objective: Minimize the distance traveled
def objective_func(model):
    return sum(model.x[i, j] * distances[i, j] for i in model.cities for j in model.cities if (i, j) in distances)
model.objective = Objective(rule=objective_func, sense=minimize)

# Constraint: Every city must be visited exactly once
def visit_constraint(model, j):
    return sum(model.x[i, j] for i in model.cities if (i, j) in distances) == 1
model.visit_each_city = Constraint(model.cities, rule=visit_constraint)

# Constraint: Must leave each city only once
def leave_constraint(model, i):
    return sum(model.x[i, j] for j in model.cities if (i, j) in distances) == 1
model.leave_each_city = Constraint(model.cities, rule=leaveDependencyConstraint)

# Solve
solver = SolverFactory('cbc')
results = solver.solve(model, tee=True)

# Extracting the solution
tour = []
visited = [0]
current_city = 0

while len(visited) < n:
    for j in model.cities:
        if model.x[current_city, j]() > 0.5 and j not in visited:
            tour.append((current_city, j))
            current_city = j
            visited.append(j)
            break
tour.append((current_city, 0))  # Return to depot

# Reconstruct tour and calculate travel cost
total_cost = 0
tour_sequence = [0]
for (i, j) in tour:
    tour_sequence.append(j)
    total_cost += distances[i, j]

print("Tour:", tour_sequence)
print("Total travel cost:", total_cost)