from math import sqrt
from itertools import permutations
import gurobipy as gp
from gurobipy import GRB

# Define the cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

n = len(cities)

# Distance matrix computation
def euclidean_dist(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

dist = [[euclidean_dist(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the model
m = gp.Model()

# Variables
x = m.addVars(n, n, vtype=GRB.BINARY, name="x")
max_dist = m.addVar(vtype=GRB.CONTINUOUS, name="max_dist")

# Objective: minimize the maximum distance between consecutive cities
m.setObjective(max_dist, GRB.MINIMIZE)

# Contstraints
# Each city has exactly one outgoing connection
m.addConstrs((x.sum(i, '*') == 1 for i in range(n)), name="out_flow")
# Each city has exactly one incoming connection
m.addConstrs((x.sum('*', i) == 1 for i in range(n)), name="in_flow")
# Eliminate subtours using the lazy constraints approach in the callback function
def subtour_elimination(model, where):
    if where == GRB.Callback.MIPSOL:
        selected = [(i, j) for i in range(n) for j in range(n) if model.cbGetSolution(model._x[i, j]) > 0.5]
        _, tour = gp.tsp.getTSPRoute(selected)
        if len(tour) < n:
            model.cbLazy(gp.quicksum(model._x[i, j] for i, j in permutations(tour, 2)) <= len(tour) - 1)

# Link max_dist with distance variables
m.addConstrs((x[i, j] * dist[i][j] <= max_dist for i in range(n) for j in range(n)), name="link_max_distance")

m._x = x
m.Params.lazyConstraints = 1
m.optimize(subtour_elimination)

# Retrieve solution
if m.status == GRB.OPTIMAL:
    tour = []
    next_city = 0
    for _ in range(n+1):
        tour.append(next_city)
        next_city = [j for j in range(n) if x[next_city, j].X > 0.5][0]

    max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No optimal solution found.")