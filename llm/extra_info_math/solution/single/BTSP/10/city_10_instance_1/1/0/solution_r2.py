import pyomo.environ as pyo
import math

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

n = len(cities)  # number of cities

# Calculate distances
distances = [[math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
              for j in range(n)] for i in range(n)]

model = pyo.ConcreteModel()

# Sets
model.Nodes = pyo.RangeSet(0, n-1)
model.Pairs = pyo.Set(initialize=model.Nodes * model.Nodes, filter=lambda model, i, j: i != j)

# Variables
model.x = pyo.Var(model.Pairs, within=pyo.Binary)
model.z = pyo.Var(within=pyo.NonNegativeReals)

# Objective
model.obj = pyo.Objective(expr=model.z, sense=pyo.minimize)

# Constraints
def max_dist_constraint(model, i, j):
    return model.z >= model.x[i, j] * distances[i][j]
model.MaxDistCons = pyo.Constraint(model.Pairs, rule=max_dist_constraint)

def enter_each_city_once_constraint(model, j):
    return sum(model.x[i, j] for i in model.Nodes if i != j) == 1
model.EnterCityCons = pyo.Constraint(model.Nodes, rule=enter_each_city_once_constraint)

def leave_each_city_once_constraint(model, i):
    return sum(model.x[i, j] for j in model.Nodes if i != j) == 1
model.LeaveCityCons = pyo.Constraint(model.Nodes, rule=leave_each_city_once_constraint)

def subtour_elimination_constraint(model, S):
    if len(S) > 1 and len(S) < n:
        return sum(model.x[i, j] for i in S for j in S if i != j) <= len(S) - 1
model.SubtourElimCons = pyo.ConstraintList()
for S_size in range(2, n):
    for S in combinations(model.Nodes, S_size):
        model.SubtourElimCons.add(subtour_elimination_constraint(model, S))

# Solve the model
solver = pyo.SolverFactory('cbc')
result = solver.solve(model, tee=True)

def extract_tour(x_vars):
    tour = [0]
    # Start from the depot
    current_city = 0
    while True:
        # Find next city with x_ij = 1 and not returning to depot except to finish
        next_cities = [j for j in model.Nodes if pyo.value(x_vars[current_city, j]) == 1 and j != 0]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_var)
        if next_var == 0:
            break
        current_var = next_var
    return tour

tour = extract_tour(model.x)
max_distance = pyo.value(model.z)
total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")