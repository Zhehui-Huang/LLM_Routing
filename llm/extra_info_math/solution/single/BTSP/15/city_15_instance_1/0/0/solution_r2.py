from gurobipy import Model, GRB, quicksum
import math
from itertools import combinations

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

def distance(a, b):
    dx = cities[a][0] - cities[b][0]
    dy = cities[a][1] - cities[b][1]
    return math.sqrt(dx * dx + dy * dy)

# Distances between each pair of cities
dist = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Initialize Model
m = Model("TSP")

# Decision Variables
x = m.addVars(dist.keys(), vtype=GRB.BINARY, name="x")
max_dist = m.addVar(vtype=GRB.CONTINUOUS, name="max_dist")

# Objective: Minimize the maximum distance between consecutive cities in the tour
m.setObjective(max_dist, GRB.MINIMIZE)

# Constraints
m.addConstrs(x.sum(i, '*') == 1 for i in cities)  # Leave each city once
m.addConstrs(x.sum('*', j) == 1 for j in cities)  # Enter each city once

# Link x_ij and max_dist
m.addConstrs((x[i, j] * dist[i, j] <= max_dist for i, j in x.keys()), "maxDistLink")

# Avoid subtours
for i in range(2, len(cities)):
    for s in combinations(cities, i):
        m.addConstr(quicksum(x[i, j] for i in s for j in s if i != j) <= len(s) - 1)

# Optimize the model
m.optimize()

if m.status == GRB.OPTIMAL:
    edges = [(i, j) for i, j in x.keys() if x[i, j].X > 0.5]
    tour = [0]
    curr = 0
    # Construct the tour starting from node 0
    while len(tour) < len(cities):
        for e in edges:
            if e[0] == curr:
                tour.append(e[1])
                curr = e[1]
                break
    
    # Ensure to return to starting point, Depot city.
    tour.append(0)
    
    # Calculate Total Travel Cost and Max Distance
    total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(dist[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    cabal}?fontsize=14)
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal available")