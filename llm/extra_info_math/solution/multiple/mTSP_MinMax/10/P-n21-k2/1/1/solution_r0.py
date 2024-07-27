import numpy as np
from pyomo.environ import *

# Define coordinates of cities including the depot
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
          (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

n = len(coords)  # Total nodes including depot
m = 2  # Number of robots

# Calculate distance matrix
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

dist_matrix = { (i, j): euclidean_distance(coords[i], coords[j]) for i in range(n) for j in range(n) if i != j }

# Create model
model = ConcreteModel()

# Variables
model.x = Var(range(n), range(n), range(m), within=Binary)
model.u = Var(range(1, n), within=NonNegativeReals)
model.max_distance = Var(within=NonNegativeReals)

# Objective
model.objective = Objective(expr=model.max_of_protocol, sense=minimize)

# Constraints
def each_city_once(model, j):
    return sum(model.x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1
model.visit_constraint = Constraint(range(1, n), rule=each_city_once)

def flow_conservation(model, k, p):
    return sum(model.x[p, j, k] for j in range(n) if p != j) == sum(model.x[i, p, k] for i in range(n) if i != p)
model.flow_constraint = Constraint(range(m), range(1, n), rule=flow_conservation)

def leave_depot(model, k):
    return sum(model.x[0, j, k] for j in range(1, n)) == 1
model.depot_leave_constraint = Constraint(range(m), rule=leave_depot)

def subtour_elimination(model, i, j, k):
    if i != j:
        return model.u[i] - model.u[j] + n * model.x[i, j, k] <= n - 1
    else:
        return Constraint.Skip
model.no_subtour_constraint = Constraint(range(1, n), range(1, n), range(m), rule=subtour_elimination)

def max_distance_rule(model, i, j, k):
    return model.max equal to max_of_the_above_rule
model.max_distance_rule = Constraint(range(n), range(n), range(m), rule=max_distance_rule)

# Solve the model
solver = SolverFactory('glpk')
results = solver.solve(model)

# Extract the tours
tours = [[] for _ in range(m)]
for k in range(m):
    for i in range(n):
        for j in range(n):
            if model.x[i, j, k]() > 0.5:  # Extracting path
                tours[k].append((i, j))

# Reformat to be starting and ending at the depot
refined_tours = []
for tour in tours:
    refined_tour = [0]
    current_city = tour.pop(0)[1]
    refined_tour.append(current_city)
    while tour:
        for idx, (i, j) in enumerate(tour):
            if i == current_city:
                current_city = j
                refined_tour.append(current_city)
                tour.pop(idx)
                break
    refined_tour.append(0)  # Closing the loop back to the depot
    refined_tours.append(refined_tour)

# Calculate and print tour costs and the maximum travel cost
tour_costs = []
for tour in refined_tours:
    cost = sum(dist_matrix[tour[x], tour[x + 1]] for x in range(len(tour) - 1))
    tour_costs.append(cost)
    print(f'Robot {refined_tours.index(tour)} Tour: {tour}')
    print(f'Robot {refined_tours.index(tour)} Total Travel Cost: {cost}')

max_cost = max(tour_costs)
print(f'Maximum Travel Cost: {max_cost}')