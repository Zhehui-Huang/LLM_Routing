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

# Set of cities including depots
cities = set(coordinates.keys())
depot = 0  # Single depot starting point for all robots

# Model
model = pyo.ConcreteModel()

# Decision Variables
model.x = pyo.Var(cities, cities, within=pyo.Binary)
model.u = pyo.Var(cities, within=pyo.NonNegativeReals)

# Objective: Minimize total travel distance
def obj_rule(model):
    return sum(model.x[i, j] * distance(i, j) for i in cities for j in cities if i != j)
model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

# Constraints
# Visit each city exactly once from outside
def con_visit_once(model, j):
    if j != depot:
        return sum(model.x[i, j] for i in cities if i != j) == 1
    else:
        return pyo.Constraint.Skip

model.con_visit_once = pyo.Constraint(cities, rule=con_visit_once)

# Leave each city exactly once to another city
def con_leave_once(model, i):
    if i != depot:
        return sum(model.x[i, j] for j in cities if i != j) == 1
    else:
        return pyo.Constraint.Skip

model.con_leave_once = pyo.Constraint(cities, rule=con_leave_once)

# Subtour prevention constraint
def con_subtour_elimination(model, i, j):
    if i != j and i != depot and j != depot:
        return model.u[i] - model.u[j] + len(cities) * model.x[i, j] <= len(cities)-1
    else:
        return pyo.Constraint.Skip
model.con_subtour_elimination = pyo.Constraint(cities, cities, rule=con_subtour_elimination)

# Assign robots to leave from the initial depot without forcing return
def con_robots_depart(model):
    return sum(model.x[depot, j] for j in cities if j != depot) == 2  # Two robots
model.con_robots_depart = pyo.Constraint(rule=con_robots_depart)

# Solve the problem using a solver
solver = pyo.SolverFactory('glpk')
result = solver.solve(model, tee=True)

# Extract the solution
routes = {}
for i in cities:
    routes[i] = [(j, model.x[i, j]()) for j in cities if model.x[i, j]() > 0.9]

# Building up routes from the solution
tours = []
seen = set()
for start in routes[depot]:
    if start[1] > 0 and start[0] not in seen:
        current = start[0]
        tour = [depot, current]
        seen.add(current)
        while current in routes and any(c > 0 for _, c in routes[current]):
            for next_city, active in routes[current]:
                if active > 0 and next_city not in seen:
                    tour.append(next_city)
                    seen.add(next_city)
                    current = next_city
                    break
        tours.append(tour)

# Calculate Tour Costs
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Display Result
total_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = calculate_cost(tour)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Cost: {total_cost}")