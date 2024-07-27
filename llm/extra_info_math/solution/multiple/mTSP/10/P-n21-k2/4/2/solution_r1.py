import pyomo.environ as pyo
from math import sqrt

# Coordinates of cities including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
n = len(cities)  # Total nodes, including depot
m = 2  # Number of robots

# Euclidean distance function
def distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distances = {
    (i, j): distance(cities[i], cities[j])
    for i in range(n) for j in range(n) if i != j
}

# Create a model
model = pyo.ConcreteModel()

# Indices for salesmen and nodes
nodes = range(n)
salesmen = range(m)

# Variables
model.x = pyo.Var(nodes, nodes, salesmen, within=pyo.Binary)  # Travel between nodes
model.u = pyo.Var(nodes, within=pyo.NonNegativeReals)  # Position in the tour to prevent subtours

# Objective: Minimize distance
model.obj = pyo.Objective(
    expr=sum(model.x[i, j, k] * distances[i, j] for i in nodes for j in nodes for k in salesmen if i != j),
    sense=pyo.minimize)

# Constraints
# Each city must be visited exactly once excluding depot city
model.one_visit = pyo.ConstraintList()
for j in nodes[1:]:
    model.one_visit.add(sum(model.x[i, j, k] for i in nodes for k in salesmen if i != j) == 1)

# Each salesman leaves the depot and returns to the depot
model.depot_start_end = pyo.ConstraintList()
for k in salesmen:
    model.depot_start_end.add(sum(model.x[0, j, k] for j in nodes if j != 0) == 1)
    model.depot_start_end.add(sum(model.x[i, 0, k] for i in nodes if i != 0) == 1)

# Continuity and Subtour elimination constraint
model.tour_continuity = pyo.ConstraintList()
for k in salesmen:
    for i in nodes[1:]:
        model.tour_continuity.add(sum(model.x[i, j, k] for j in nodes if i != j) == sum(model.x[j, i, k] for j in nodes if i != j))

# Subtour prevention (MTZ constraints)
model.subtour_prevention = pyo.ConstraintList()
for i in nodes[1:]:
    for j in nodes[1:]:
        if i != j:
            for k in salesmen:
                model.subtour_prevention.add(model.u[i] - model.u[j] + n * model.x[i, j, k] <= n-1)

# Solve the model
solver = pyo.SolverFactory('glpk')
results = solver.solve(model)

# Extract solution
tours = []
for k in salesmen:
    tour = []
    for i in nodes:
        for j in nodes:
            if pyo.value(model.x[i,j,k]) > 0.5:  # Binary variable threshold
                tour.append((i, j))
    tours.append(tour)

# Print results
robot_itinerary = []
total_cost = 0
for ind, tour in enumerate(tours):
    path = [0]  # Start at the depot
    current = 0
    cost = 0
    while len(tour) > 0:
        for i, (src, dest) in enumerate(tour):
            if src == current:
                cost += distances[src, dest]
                current = dest
                path.append(dest)
                tour.pop(i)
                break
    path.append(0)  # Return to depot
    cost += distances[current, 0]  # Return to depot cost
    total_cost += cost
    print(f"Robot {ind} Tour: {path}")
    print(f"Robot {ind} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")