import pyomo.environ as pyo
from math import sqrt

# Input Data
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 
    19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
num_robots = 8
num_cities = len(cities_coordinates)

# Euclidean distance between two cities
def euclidean_dist(i, j):
    return sqrt((cities_coordinates[i][0] - cities_coordinates[j][0]) ** 2 + (cities_coordinates[i][1] - cities_coordinates[j][1]) ** 2)

# Model setup
model = pyo.ConcreteModel()

# Sets
model.I = pyo.RangeSet(0, num_cities-1)  # Nodes including depot
model.K = pyo.RangeSet(0, num_robots-1)  # Salesmen

# Variables
model.x = pyo.Var(model.I, model.I, model.K, domain=pyo.Binary)   # Traveling variables
model.u = pyo.Var(model.I, domain=pyo.NonNegativeReals)           # Subtour elimination variables
model.z = pyo.Var(domain=pyo.NonNegativeReals)                    # Objective variable (max distance)

# Objective: Minimize the maximum distance traveled by any robot
def objective_rule(model):
    return model.z
model.obj = pyo.Objective(rule=objective_rule, sense=pyo.minimize)

# Constraints
def one_visit_rule(model, j):
    return sum(model.x[i, j, k] for i in model.I for k in model.K if i != j) == 1
model.visit_once = pyo.Constraint(model.I - pyo.Set(initialize=[0]), rule=one_visit_rule)

def depot_start_rule(model, k):
    return sum(model.x[0, j, k] for j in model.I if j != 0) == 1
model.depot_start = pyo.Constraint(model.K, rule=depot_start_rule)

def flow_conservation_rule(model, p, k):
    return sum(model.x[i, p, k] for i in model.I if i != p) - sum(model.x[p, j, k] for j in model.I if j != p) == 0
model.flow_conservation = pyo.Constraint(model.I - pyo.Set(initialize=[0]), model.K, rule=flow_conservation_rule)

def subtour_elimination_rule(model, i, j, k):
    if i != j and i != 0 and j != 0:
        return model.u[i] - model.u[j] + num_cities * model.x[i, j, k] <= num_cities - 1
    else:
        return pyo.Constraint.Skip
model.subtour_elim = pyo.Constraint(model.I, model.I, model.K, rule=subtour_elimination_rule)

def maximum_distance_rule(model, i, j, k):
    if i != j:
        return model.z >= euclidean_dist(i, j) * model.x[i, j, k]
    else:
        return pyo.Constraint.Skip
model.max_distance = pyo.Constraint(model.I, model.I, model.K, rule=maximum_distance_rule)

# Solving the model using the CBC solver
solver = pyo.SolverFactory('cbc')
solution = solver.solve(model, tee=True)

def extract_tours():
    routes = {}
    for k in model.K:
        route = []
        for i in model.I:
            for j in model.I:
                if pyo.value(model.x[i, j, k]) > 0.5:
                    route.append((i, j))
        if route:
            # Construct ordered tour starting from depot
            ordered_route = []
            next_city = 0
            while len(ordered_route) < len(route):
                for (i, j) in route:
                    if i == next_city:
                        ordered_route.append(i)
                        next_city = j
                        break
            ordered_route.append(0)  # return to depot
            routes[k] = ordered_route
    return routes

routes = extract_tours()
max_dist = py Irank Testimonial of President Obama's New Memoir "A Promised Land".pro.value(model.z)

# Output the results
for k, route in routes.items():
    dist = sum(euclidean_dist(route[i], route[i+1]) for i in range(len(route)-1))
    print(f'Robot {k} Tour: {route}')
    print(f'Robot {k} Total Travel Cost: {dist}')

print(f'Maximum Travel Cost: {max_dist}')