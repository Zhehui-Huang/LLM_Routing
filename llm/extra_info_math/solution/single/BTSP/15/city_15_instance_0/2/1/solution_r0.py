# Import necessary libraries
import pyomo.environ as pyo
import math

# Data for the problem
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

n = len(cities)

# Distance calculation
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Model initialization
model = pyo.ConcreteModel()

# Variables
model.x = pyo.Var(distances.keys(), within=pyo.Binary)
model.max_distance = pyo.Var(within=pyo.NonNegativeReals)

# Objective
model.objective = pyo.Objective(expr=model.max_distance, sense=pyo.minimize)

# Constraints
def rule_max_distance(model, i, j):
    return model.x[i, j] * distances[i, j] <= model.max_distance
model.constraint_max_distance = pyo.Constraint(distances.keys(), rule=rule_max_distance)

def rule_out_one(model, i):
    return sum(model.x[i, j] for j in cities if (i, j) in distances) == 1
model.out_constraints = pyo.Constraint(cities.keys(), rule=rule_out_one)

def rule_in_one(model, j):
    return sum(model.x[i, j] for i in cities if (i, j) in distances) == 1
model.in_constraints = pyo.Constraint(cities.keys(), rule=rule_in_one)

# Solver configuration
solver = pyo.SolverFactory("cbc")
result = solver.solve(model, tee=True)

# Extracting the solution
solution_edges = [(i, j) for i, j in distances if pyo.value(model.x[i, j]) == 1]
tour = [0]
while len(tour) < n:
    i = tour[-1]
    for j in cities:
        if (i, j) in solution_edges:
            tour.append(j)
            break
tour.append(0)  # To return to the depot

# Calculating the total distance and maximum distance
total_distance = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")