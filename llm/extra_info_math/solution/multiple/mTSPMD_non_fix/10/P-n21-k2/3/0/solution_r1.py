import numpy as to
from pyomo.environ import *

# Define the coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Setup the Pyomo model
model = ConcreteModel()
N = range(len(coordinates))
A = [(i, j) for i in N for j in N if i != j]
C = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i, j in A}

model.x = Var(A, within=Binary)
model.u = Var(N, within=NonNegativeReals)

# Objective: minimize the distance traveled
model.obj = Objective(expr=sum(C[i, j] * model.x[i, j] for i, j in A), sense=minimize)

# Constraint: Leave each city only once
model.outbonds = ConstraintList()
for i in N:
    model.outbonds.add(expr = sum(model.x[i, j] for j in N if i != j) == 1)

# Constraint: Enter each city only once
model.inbounds = ConstraintList()
for j in N:
    model.inbounds.add(expr = sum(model.x[i, j] for i in N if i != j) == 1)

# Subtour elimination
model.subtour = ConstraintList()
for i in N:
    for j in N:
        if i != j:
            model.subtour.add(model.u[i] - model.u[j] + len(N) * model.x[i, j] <= len(N) - 1)

# Solve the model
solver = SolverFactory('cbc')
result = solver.solve(model, tee=True)

# Extract solution
tour = []
i = 0
while True:
    tour.append(i)
    nexts = [j for j in N if j != i and value(model.x[i, j]) > 0.5]
    if nexts == []:
        break
    i = nexts[0]

tour = tour + [tour[0]]
total_cost = sum(C[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print("Tour: ", tour)
print("Total travel cost: ", total_cost)