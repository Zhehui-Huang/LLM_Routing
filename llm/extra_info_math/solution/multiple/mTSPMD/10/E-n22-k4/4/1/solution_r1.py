import pyomo.environ as pyo
import math

# Coordinates including depots and other cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Function to calculate Euclidean distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create model
model = pyo.ConcreteModel()

# Sets for cities and depots
model.C = pyo.Set(initialize=range(len(coordinates)))
model.D = pyo.Set(initialize=range(4))  # Depots are the first four cities

# Distance parameter
model.dist = pyo.Param(model.C, model.C, initialize=lambda model, i, j: calc_distance(coordinates[i], coordinates[j]), within=pyo.NonNegativeReals)

# Decision Variables
model.x = pyo.Var(model.C, model.C, model.D, within=pyo.Binary)

# Objective: Minimize total distance
def objective_rule(model):
    return sum(model.dist[i, j] * model.x[i, j, k] for i in model.C for j in model.C for k in model.D if i != j)
model.total_cost = pyo.Objective(rule=objective_rule, sense=pyo.minimize)

# Constraints
# Each city is visited exactly once except depots
def visit_constraint(model, j):
    return sum(model.x[i, j, k] for i in model.C for k in model.D if i != j) == 1 if j not in model.D else pyo.Constraint.Skip
model.visited = pyo.Constraint(model.C, rule=visit_constraint)

# Tour comes back to the originating depot
def return_to_depot_constraint(model, k):
    return sum(model.x[i, k, k] for i in model.C if i != k) == 1
model.return_to_depot = pyo.Constraint(model.D, rule=return_to_depot_constraint)

# Leaving from each depot
def leave_depot_constraint(model, k):
    return sum(model.x[k, j, k] for j in model.C if j != k) == 1
model.leave_depot = pyo.Constraint(model.D, rule=leave_depot_constraint)

# Solve the problem
solver = pyo.SolverFactory('glpk')
result = solver.solve(model, tee=True)

if result.solver.status == pyo.SolverStatus.ok and result.solver.termination_condition == pyo.TerminationCondition.optimal:
    print("Optimal solution obtained")
    total_cost = pyo.value(model.total_cost)
    print(f"Overall Total Travel Cost: {total_cost:.2f}")
    
    for k in model.D:
        tour = [k]
        current = k
        while True:
            next_city = [j for j in model.C if model.x[current, j, k].value > 0.5 and j != current]
            if not next_city:
                break
            next_city = next_city[0]
            tour.append(next_city)
            current = next_city
            if current == k:
                break
        print(f"Robot {k} Tour: {tour}")
        tour_cost = sum(pyo.value(model.dist[tour[i], tour[i+1]]) for i in range(len(tour)-1))
        print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")
else:
    print("No optimal solution found.")