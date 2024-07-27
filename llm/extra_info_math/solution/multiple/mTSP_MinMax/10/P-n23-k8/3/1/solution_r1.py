import pyomo.environ as pyo
from math import sqrt

# City Coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 
    19: (63, 70), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
num_robots = 8
num_cities = len(cities_coordinates)

# Euclidean distance between two cities
def euclidean_dist(i, j):
    return sqrt((cities_coordinates[i][0] - cities_coordinates[j][0]) ** 2 + (cities_coordinates[i][1] - cities_coordinates[j][1]) ** 2)

# Model
model = pyo.ConcreteModel()

# Sets
model.I = pyo.RangeSet(0, num_cities-1)  # Nodes
model.K = pyo.RangeSet(0, num_robots-1)  # Salesmen

# Variables
model.x = pyo.Var(model.I, model.I, model.K, domain=pyo.Binary)   # Travel variables
model.u = pyo.Var(model.I, domain=pyo.NonNegativeReals)           # Subtour elimination variables
model.z = pyo.Var(domain=pyo.NonNegativeReals)                    # Max distance variable

# Objective: Minimize the maximum distance traveled by any robot
def objective_rule(model):
    return model.z
model.obj = pyo.Objective(rule=objective_rule, sense=pyo.minimize)

# Each city is visited once
def visiting_constraint(model, j):
    if j == 0:
        return pyo.Constraint.Skip
    return sum(model.x[i, j, k] for i in model.I for k in model.K if i != j) == 1
model.city_visited_once = pyo.Constraint(model.I, rule=visiting_constraint)

# Depart from the depot constraint
def depart_depot_constraint(model, k):
    return sum(model.x[0, j, k] for j in model.I if j != 0) == 1
model.depart_from_depot = pyo.Constraint(model.K, rule=depart_depot_constraint)

# Enter the depot constraint
def enter_depot_constraint(model, k):
    return sum(model.x[i, 0, k] for i in model.I if i != 0) == 1
model.enter_depot = pyo.Constraint(model.K, rule=enter_depot_constraint)

# Conservation of flow constraint
def flow_constraint(model, p, k):
    if p == 0:
        return pyo.Constraint.Skip
    return sum(model.x[i, p, k] for i in model.I if i != p) == sum(model.x[p, j, k] for j in model.I if j != p)
model.conserve_flow = pyo.Constraint(model.I, model.K, rule=flow_constraint)

# Subtour elimination constraints
def subtour_elimination_rule(model, i, j, k):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + num_cities * model.x[i, j, k] <= num_cities - 1
    return pyo.Constraint.Skip
model.subtour_elimination = pyo.Constraint(model.I, model.I, model.K, rule=subtour_elimination_rule)

# Maximum distance constraint
def max_dist_constraint(model, i, j, k):
    return model.z >= euclidean_dist(i, j) * model.x[i, j, k]
model.max_

import pyomo.environ as pyo
from math import sqrt

# Input Data Setup
cities_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
                      6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
                      12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
                      18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)}
num_robots = 8
num_cities = len(cities_coordinates)  # Including depot

# Distance calculation using Euclidean formula
def calc_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Setting up the Pyomo model
model = pyo.ConcreteModel()

# Sets for cities and robots
model.I = pyo.RangeSet(0, num_cities-1)  # Including depot as 0
model.K = pyo.RangeSet(0, num_robots-1)

# Variables for decision making
model.x = pyo.Var(model.I, model.I, model.K, domain=pyo.Binary)   # Travel decision
model.u = pyo.Var(model.I, domain=pyo.NonNegativeReals)           # Position for subtour elimination
model.z = pyo.Var(domain=pyo.NonNegativeReals)                    # Maximize distance variable

# Objective: Minimize the maximum distance traveled by any robot
def obj_rule(model):
    return model.z
model.objective = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

# Constraints
# Each city must be visited exactly once by exactly one robot
def visit_cities_rule(model, j):
    if j == 0:
        return pyo.Constraint.Skip  # Skip depot
    return sum(model.x[i, j, k] for i in model.I for k in model.K if i != j) == 1
model.visit_cities = pyo.Constraint(model.I, rule=visit_cities_rule)

# Each robot leaves each city it visits
def leave_city_rule(model, k):
    return sum(model.x[0, j, k] for j in model.I if j != 0) == 1  # Leave from depot
model.leave_city = pyo.Constraint(model.K, rule=leave_city_rule)

# Flow conservation at cities for each robot
def flow_conserve_rule(model, k, p):
    return sum(model.x[i, p, k] for i in model.I if i != p) == sum(model.x[p, j, k] for j in model.I if j != p)
model.flow_conserve = pyo.Constraint(model.K, model.I - pyo.Set(initialize=[0]), rule=flow_conserve_rule)

# Subtour elimination (prevent cycles)
def subtour_elim_rule(model, i, j, k):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + num_cities * model.x[i, j, k] <= num_cities - 1
    return pyo.Constraint.Skip
model.subtour_elim = pyo.Constraint(model.I, model.I, model.K, rule=subtour_elim_rule)

# Limit the maximum distance to the value of z
def max_distance_rule(model, i, j, k):
    if i != j:
        return model.z >= calc_distance(i, j) * model.x[i, j, k]
    return pyo.Constraint.Skip
model.max_distance = pyo.Constraint(model.I, model.I, model.K, rule=max_distance_rule)

# Solver setup and execution
solver = pyo.SolverFactory('cbc')
result = solver.solve(model, tee=True)

if (result.solver.status == pyo.SolverStatus.ok) and (result.solver.termination_condition == pyo.TerminationCondition.optimal):
    # Extracting and printing the routes solution
    routes = {}
    for k in model.K:
        route = [(i, j) for i in model.I for j in model.I if pyo.value(model.x[i, j, k]) > 0.5 and i != j]
        # Order 
        organized_route = [0]
        while len(organized_route) - 1 < len(route):
            last = organized_route[-1]
            for (i, j) in route:
                if i == last:
                    organized_route.append(j)
                    break
        routes[k] = organized_route
        print(f"Robot {k} Tour: {organized_qrouteCost(rule={model.k} = {pyo.value{model.z}})

else:
    print("No optimal solution found")