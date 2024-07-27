# Python code to minimize the maximum distance between consecutive cities in a TSP.
from gurobipy import Model, GRB, quicksum
import math

# Define the cities and their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Calculate Euclidean distances between all pairs of cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

dist = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Create a model
m = Model()

# Variables: x[i, j] == 1 if route goes from city i to city j
x = m.addVars(dist.keys(), vtype=GRB.BINARY, name='x')
# Variable which signifies the maximum distance in the route
max_dist = m.addVar(name='max_dist')

# Objective: minimize the maximum distance
m.setObjective(max_dist, GRB.MINIMIZE)

# Add constraints

# Enter and exit each city exactly once
m.addConstrs(quicksum(x[i, j] for j in cities if j != i) == 1 for i in cities)
m.addConstrs(quicksum(x[i, j] for i in cities if i != j) == 1 for j in cities)

# Subtour elimination
vals = range(len(cities))
for i in range(2, len(vals)):
    for s in combinations(vals, i):
        m.addConstr(quicksum(x[i, j] for i in s for j in s if i != j) <= len(s) - 1)

# Link max_dist with x
m.addConstrs((x[i, j] * dist[i, j] <= max_dist for i, j in x.keys()), name='MaxDistLink')

# Solve the problem
m.optimize()

if m.status == GRB.OPTIMAL:
    solution = m.getAttr('x', x)
    tour = []
    active = 0
    while len(tour) < len(cities):
        tour.append(active)
        for k in cities:
            if k != active and solution[active, k] > 0.5:
                active = k
                break
    
    # Adding the return to the depot
    tour.append(0)

    total_cost = sum(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    maximum_distance = max(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {maximum_distance}")
else:
    print("No solution")