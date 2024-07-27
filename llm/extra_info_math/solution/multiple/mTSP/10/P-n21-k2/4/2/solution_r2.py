import pyomo.environ as pyo
from math import sqrt

# Coordinates of cities including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
n = len(cities)  # Total number of nodes, including depot
m = 2  # Number of robots

# Function to calculate Euclidean distance
def distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Precompute distances
distances = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Pyomo model
model = pyo.ConcreteModel()

# Sets
model.nodes = range(n)
model.robots = range(m)

# Decision variables
model.x = pyo.Var(model.nodes, model.nodes, model.robots, within=pyo.Binary)
model.u = pyo.Var(model.nodes, within=pyo.NonNegativeReals)

# Objective
model.obj = pyo.Objective(expr=sum(model.x[i, j, k] * distances[i, j] for i in model.nodes for j in model.nodes for k in model.robots if i != j), sense=pyo.minimize)

# Constraints
model.constraints = pyo.ConstraintList()

# Each node (except depot) is visited exactly once by any robot
for j in model.nodes[1:]:
    model.constraints.add(sum(model.x[i, j, k] for i in model.nodes for k in model.robots if i != j) == 1)

# Each robot starts and ends at the depot
for k in model.robots:
    model.constraints.add(sum(model.x[0, j, k] for j in model.nodes if j != 0) == 1)
    model.constraints.add(sum(model.x[i, 0, k] for i in model.nodes if i != 0) == 1)

# Flow conservation for each robot and each city
for k in model.robots:
    for j in model.nodes[1:]:
        model.constraints.add(sum(model.x[i, j, k] for i in model.nodes if i != j) - sum(model.x[j, i, k] for i in model.nodes if i != j) == 0)

# Subtour elimination (using MTZ constraints)
for i in model.nodes[1:]:
    for j in model.nodes[1:]:
        if i != j:
            for k in model.robots:
                model.constraints.add(model.u[i] - model.u[j] + n * model.x[i, j, k] <= n - 1)

# Solve the problem
solver = pyo.SolverFactory('glpk')
results = solver.solve(model)

# Interpretation of results
total_distance = pyo.value(model.obj)
tours = []
for k in model.robots:
    tour = []
    current = 0
    while True:
        for j in model.nodes:
            if current != j and pyo.value(model.x[current, j, k]) == 1:
                tour.append(j)
                current = j
                break
        if current == 0:
            break
    tours.append(tour)

for robot, tour in enumerate(tours):
    tour_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print("Overall Total Travel Cost:", total_distance)