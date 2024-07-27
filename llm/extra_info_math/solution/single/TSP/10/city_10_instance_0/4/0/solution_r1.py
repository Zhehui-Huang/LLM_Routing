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
model.cities = RangeSet(0, n-1)

# Variables
model.x = Var(model.cities, model.cities, within=Binary)

# Objective
def objective_rule(model):
    return sum(model.x[i, j] * distances[i, j] for i in model.cities for j in model.cities if i != j)
model.objective = Objective(rule=objective_rule, sense=minimize)

# Constraints
def enter_city_once_rule(model, j):
    if j != 0:
        return sum(model.x[i, j] for i in model.cities if i != j) == 1
    return Constraint.Skip
model.enter_city_once = Constraint(model.cities, rule=enter_city_once_rule)

def leave_city_once_rule(model, i):
    if i != 0:
        return sum(model.x[i, j] for j in model.cities if i != j) == 1
    return Constraint.Skip
model.leave_city_once = Constraint(model.cities, rule=leave_city_once_rule)

# Subtour elimination logic
model.u = Var(model.cities, within=NonNegativeIntegers, bounds=(0, n-1))
def no_subtour_rule(model, i, j):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + n * model.x[i, j] <= n - 1
    return Constraint.Skip
model.no_subtour = Constraint(model.cities, model.cities, rule=no_subtour_rule)

# Solve the problem using a solver
solver = SolverFactory('glpk')
results = solver.solve(model)

# Check the result
if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition == TerminationCondition.optimal):
    # Extract the solution
    tour = []
    for i in model.cities:
        for j in model.cities:
            if model.x[i, j].value > 0.5:
                tour.append((i, j))

    # Reconstruct the tour from the binary variables
    ordered_tour = []
    next_city = 0
    while True:
        for i, j in tour:
            if i == next_city:
                ordered_tour.append(i)
                next_city = j
                break
        if next_city == 0:
            ordered_tour.append(0)
            break

    # Compute the total travel cost
    total_cost = sum(distances[ordered_tour[i], ordered_tour[i+1]] for i in range(len(ordered_tour) - 1))

    # Print results
    print("Tour:", ordered_tour)
    print("Total travel cost:", total_cost)
else:
   print("No optimal solution found.")