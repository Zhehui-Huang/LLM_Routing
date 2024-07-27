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
model.constraints = pyo.ConstraintList()
for i, j in distances.keys():
    model.constraints.add(model.x[i, j] * distances[i, j] <= model.max_distance)

def supply_constraint(model, i):
    return sum(model.x[i, j] for j in cities if (i, j) in distances) == 1
model.supply_constraint = pyo.Constraint(cities.keys(), rule=supply_constraint)

def demand_constraint(model, j):
    return sum(model.x[i, j] for i in cities if (i, j) in distances) == 1
model.demand_constraint = pyo.Constraint(cities.keys(), rule=demand_constraint)

# Subtour elimination
def subtour_elimination(model, *args):
    nodes = list(args)
    if len(nodes) <= 1 or len(nodes) >= n:
        return pyo.Constraint.Skip
    return sum(model.x[i, j] for i in nodes for j in nodes if i != j) <= len(nodes) - 1

from itertools import combinations

for size in range(2, n):
    for subset in combinations(cities.keys(), size):
        model.constraints.add(subtour_elimination(model, *subset))
        
# Solver configuration
solver = pyo.SolverFactory("cbc")
result = solver.solve(model, tee=True, symbolic_solver_labels=True)

# Extracting the solution
def extract_tour_from_variables(variables):
    # Find the start point, usually the depot
    start = 0
    tour = [start]
    current = start
    iterate = True
    while iterate:
        # Find the next city with x_ij = 1 and not yet in the tour
        next_city = next(i for i in cities if (current, i) in variables and variables[current, i] == 1 and i not in tour)
        tour.append(next_city)
        current = next_city
        if current == start:
            break
    return tour

tour = extract_tour_from_variables({(i, j): pyo.value(model.x[i, j]) for i, j in distances})
total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")