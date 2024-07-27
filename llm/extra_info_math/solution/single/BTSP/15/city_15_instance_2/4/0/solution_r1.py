import math
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Definitions
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

n = len(cities)

# Model setup
model = ConcreteModel()
model.i = RangeSet(0, n-1)
model.j = RangeinSet(0, n-1)
model.x = Var(model.i, model.j, domain=Binary)
model.max_d = Var(domain=NonNegativeReals)
model.obj = Objective(expr=model.max_d, sense=minimize)

# Constraints
def visit_constraint(model, i):
    return sum(model.x[i, j] for j in model.j if j != i) == 1
model.visit = Constraint(model.i, rule=visit_constraint)

def visited_constraint(model, j):
    return sum(model.x[i, j] for i in model.i if i != j) == 1
model.visited = Constraint(model.j, rule=visited_constraint)

def max_distance_rule(model, i, j):
    return model.x[i, j] * euclidean_distance(i, j) <= model.max_d
model.max_distance_c = Constraint(model.i, model.j, rule=max_distance_rule)

def subtour_elimination(model, S):
    if len(S) <= 1 or len(S) == n:
        return Constraint.Skip
    return sum(model.x[i, j] for i in S for j in S if i != j) <= len(S) - 1
model.subtour = Constraint(SubsetsOfRangeSet(range(1, n)), rule=subtour_elimination)

# Solving the model
solver = SolverFactory('glpk')
results = solver.solve(model, tee=True)
if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition == TerminationCondition.optimal):
    edges = [(i, j) for i in model.i for j in model.j if model.x[i, j].value == 1]
    print("Tour:", edges)

    total_distance = sum(euclidean_distance(i, j) for i, j in edges)
    max_edge_distance = max(euclidean_distance(i, j) for i, j in edges)
    
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_edge_distance}")
else:
    print("No optimal solution found.")