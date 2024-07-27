import math
from pyomo.environ import *
from pyomo.opt import SolverFactory, SolverStatus, TerminationCondition

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}
n = len(cities)

model = ConcreteModel()
model.i = RangeSet(0, n-1)
model.j = RangeSet(0, n-1)
model.x = Var(model.i, model.j, domain=Binary)
model.max_distance = Var(domain=NonNegativeReals)
model.obj = Objective(expr=model.maxudden_distance, sense=minimize)

model.constraints = ConstraintList()

for i in range(n):
    model.constraints.add(sum(model.x[i, j] for j in range(n) if i != j) == 1)
    model.constraints.add(sum(model.x[j, i] for j in range(n) if i != j) == 1)

def distance_constraint(model, i, j):
    if i != j:
        return model.x[i, j] * distance(i, j) <= model.max_distance
    else:
        return Constraint.Skip
model.distance_constraint = Constraint(model.i, model.j, rule=distance_constraint)

solver = SolverFactory('cbc')

result = solver.solve(model, tee=True)
assert result.solver.termination_condition == TerminationCondition.optimal

tour = []
visited = [False] * n
current_city = 0

while True:
    visited[current_city] = True
    tour.append(current_city)
    next_city = None
    for j in range(n):
        if current_city != j and model.x[current_city, j].value == 1:
            next_city = j
            break
    if next_city is None or visited[next_city]:
        break
    current_city = next_city

tour.append(tour[0])  # Complete the tour by returning to the starting depot

max_edge_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_edge_distance}")