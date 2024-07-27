import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import math

# Function to compute Euclidean distance between cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Data input: city index and their respective coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

n = len(cities)

# Create a distance matrix
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

# Number of robots
num_robots = 8

# Start of optimization model
model = pyo.ConcreteModel()

# Sets
model.N = pyo.RangeSet(0, n-1)
model.R = pyo.RangeSet(0, num_robots-1)

# Variables
model.x = pyo.Var(model.N, model.N, model.R, domain=pyo.Binary)
model.load = pyo.Var(model.N, model.R, domain=pyo.NonNegativeReals)

# Parameters
def dist_init(model, i, j, r):
    return distances[i, j]
model.dist = pyo.Param(model.N, model.N, model.R, initialize=dist_init)

# Objective function: Minimize total distance
def obj_function(model):
    return sum(model.x[i, j, r]*model.dist[i, j, r] for i in model.N for j in model.N for r in model.R)
model.obj = pyo.Objective(rule=obj_function, sense=pyo.minimize)

# Constraint: Leave each node once
def leave_once(model, i, r):
    return sum(model.x[i, j, r] for j in model.N if j != i) == 1
model.leave_once = pyo.Constraint(model.N, model.R, rule=leave_once)

# Constraint: Enter each node once
def enter_once(model, j, r):
    return sum(model.x[i, j, r] for i in model.N if i != j) == 1
model.enter_once = pyo.Constraint(model.N, model.R, rule=enter_once)

# Constraint: Subtour elimination
def subtour_elimination(model, i, j, r):
    if i != j:
        return model.load[i, r] - model.load[j, r] + n * model.x[i, j, r] <= n-1
    else:
        return pyo.Constraint.Skip
model.no_subtour = pyo.Constraint(model.N, model.N, model.R, rule=subtour_elimination)

# Solve the model
solver = SolverFactory('glpk')
result = solver.solve(model, tee=True)

# Check the results and format the output
if result.solver.status == 'ok' and result.solver.termination_condition == pyo.TerminationCondition.optimal:
    total_cost = 0
    for r in model.R:
        tour = []
        current_city = 0
        while True:
            tour.append(current_city)
            next_city = next(j for j in model.N if pyo.value(model.x[current_city, j, r]) > 0.5)
            if next_city == 0:
                break
            current_city = next_city
        tour.append(0)  # Return to starting city
        tour_cost = sum(pyo.value(model.dist[tour[i], tour[i+1], r]) for i in range(len(tour)-1))
        total_cost += tour_cost
        print(f"Robot {r} Tour: {tour}")
        print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")