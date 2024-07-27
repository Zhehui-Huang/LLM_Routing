import pyomo.environ as pyo
import math

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 191), (129, 189),
    (155, 185), (139, 182)
]

# Distance function
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Model setup
model = pyo.ConcreteModel()

# Indices and sets
model.cities = pyo.Set(initialize=range(len(coordinates)))
model.depots = pyo.Set(initialize=range(4))  # First four cities are depots

# Variables
model.x = pyo.Var(model.depots, model.cities, model.cities, domain=pyo.Binary)

# Objective
def obj_rule(m):
    return sum(distance(coordinates[i], coordinates[j]) * model.x[k, i, j] 
               for k in model.depots 
               for i in model.cities 
               for j in model.cities if i != j)
model.objective = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

# Constraints
# Each city should be visited exactly once and return to a depot
def visit_exactly_once_rule(m, j):
    return sum(model.x[k, i, j] for k in model.depots for i in model.cities if i != j) == \
           sum(model.x[k, j, i] for k in model.depots for i in model.cities if i != j) == 1
model.visit_exactly_once = pyo.Constraint(model.cities - model.depots, rule=visit_exactly_once_rule)

# Each depot starts and ends at itself
def depot_starts_and_ends_rule(m, k):
    return sum(model.x[k, k, j] for j in model.cities if j != k) == \
           sum(model.x[k, j, k] for j in model.cities if j != k) == 1
model.depot_starts_and_ends = pyo.Constraint(model.depots, rule=depot_starts_and_ends_rule)

# Solver
solver = pyo.SolverFactory('glpk')
results = solver.solve(model, tee=True)

# Results
if (results.solver.status == 'ok') and (results.solver.termination_condition == pyo.TerminationCondition.optimal):
    print(f"Objective: Minimized travel cost = {pyo.value(model.objective)}")
    for k in model.depots:
        tour = [k]
        current_city = k
        while True:
            next_city = [j for j in model.cities if pyo.value(model.x[k, current_city, j]) == 1 and j != current_city]
            if not next_city or next_city[0] == k:
                tour.append(k)
                break
            next_city = next_city[0]
            tour.append(next_city)
            current_city = next_city
        tour_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        print(f"Robot from Depot {k} Tour: {tour}")
        print(f"Robot from Depot {k} Tour Cost: {tour_cost}")
else:
    print("No optimal solution obtained")