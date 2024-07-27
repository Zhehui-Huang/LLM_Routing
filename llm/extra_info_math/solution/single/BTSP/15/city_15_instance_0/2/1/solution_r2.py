import pyomo.environ as pyo
import math

# Coordinates of the cities
coordinates = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Number of cities
n = len(coordinates)

# Euclidean distance calculator
def euclidean_distance(city1, city2):
    x_diff = coordinates[city1][0] - coordinates[city2][0]
    y_diff = coordinates[city1][1] - coordinates[city2][1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Creating the model
model = pyo.ConcreteModel()

# Indices for the cities
model.I = pyo.RangeSet(0, n-1)

# Variables
model.x = pyo.Var(model.I, model.I, within=pyo.Binary)
model.d = pyo.Var(within=pyo.NonNegativeReals)  # Max distance variable

# Objective: Minimize the maximum distance
model.obj = pyo.Objective(expr=model.d, sense=pyo.minimize)

# Constraints
def max_dist_constraint(model, i, j):
    if i != j:
        return model.x[i, j] * euclidean_distance(i, j) <= model.d
    else:
        return pyo.Constraint.Skip

model.max_dist = pyo.Constraint(model.I, model.I, rule=max_dist_constraint)

def in_out_constraint(model, j):
    return sum(model.x[i, j] for i in model.I if i != j) == 1

model.in_con = pyo.Constraint(model.I, rule=in_out_constraint)
model.out_con = pyo.Constraint(model.I, rule=in_out_tconstraint)


# Subtour elimination
def subtour_elim(model, I):
    length = len(I)
    if length > 1:
        return sum(model.x[i, j] for i in I for j in I if i != j) <= length - 1
    else:
        return pyo.Constraint.Skip

model.subtour = pyo.Constraint(pyo.powerset(model.I) - {()}, rule=subtour_elim)

# Solve the model
solver = pyo.SolverFactory('cbc')
results = solver.solve(model, tee=True)

# Extracting the solution
tour_order = []
if results.solver.status == pyo.SolverStatus.ok and results.solver.termination_condition == pyo.TerminationCondition.optimal:
    for i in model.I:
        for j in model.I:
            if pyo.value(model.x[i, j]) == 1:
                tour_order.append((i, j))

# Reorder the tour based on starting city
if tour_order:
    start = 0
    ordered_tour = [start]
    current = start
    length = 1
    while length < n:
        for (i, j) in tour_order:
            if i == current:
                ordered_tour.append(j)
                current = j
                length += 1
                break
    ordered_tour.append(start)  # Complete the cycle

    # Calculate metrics
    total_distance = sum(euclidean_distance(ordered_tour[i], ordered_tour[i+1]) for i in range(len(ordered_tour) - 1))
    max_distance = max(euclidean_distance(ordered_tour[i], ordered_tour[i+1]) for i in range(len(ordered_tour) - 1))

    # Print the tour and distances
    print("Tour:", ordered_tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", pyo.value(model.d))
else:
    print("No solution found")