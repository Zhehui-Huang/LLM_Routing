import pyomo.environ as pyo
from math import sqrt

# Coordinates of the cities indexed by city number
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate the Euclidean distance between two cities
def distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create a model
model = pyo.ConcreteModel()

# Sets of cities and depots
cities = set(coordinates.keys())
depots = {0}  # All robots start from depot city 0
cities_without_depots = cities - depots

# Add variables
model.x = pyo.Var(cities, cities, within=pyo.Binary)  # 1 if travel between i and j, 0 otherwise
model.u = pyo.Var(cities, within=pyo.NonNegativeReals)  # Position in the tour

# Objective: minimize total travel distance
def objective(model):
    return sum(distance(i, j) * model.x[i, j] for i in cities for j in cities if i != j)
model.obj = pyo.Objective(rule=objective, sense=pyo.minimize)

# Constraints
# Ensure each city is visited exactly once
def visit_once(model, j):
    return sum(model.x[i, j] for i in cities if i != j) == 1
model.visit_once = pyo.Constraint(cities_without_depots, rule=visit_once)

def depart_once(model, i):
    return sum(model.x[i, j] for j in cities if i != j) == 1
model.depart_once = pyo.Constraint(cities_without_depots, rule=depart_once)

# Subtour elimination
def subtour_elimination(model, i, j):
    if i != j and i in cities_without_depots and j in cities_without_depots:
        return model.u[i] - model.u[j] + len(cities) * model.x[i, j] <= len(cities) - 1
    return pyo.Constraint.Skip
model.subtour_elim = pyo.Constraint(cities, cities, rule=subtour_elimination)

# Solve the problem
solver = pyo.SolverFactory('glpk')
result = solver.solve(model)

# Extract the tours and calculate each tour's total distance
tours = []
for i in cities:
    if any(model.x[i, j]() > 0.5 for j in cities):
        tour = []
        current = i
        start = i
        while True:
            tour.append(current)
            next_cities = [j for j in cities if model.x[current, j]() > 0.5]
            if not next_cities:
                break
            current = next_cities[0]
            if current == start:
                break
        tours.append(tour)

# Calculate costs of each tour
tour_costs = [sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) for tour in tours]

# Output results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")

overall_cost = sum(tour_costs)
print(f"Overall Total Travel Cost: {overall_cost}")