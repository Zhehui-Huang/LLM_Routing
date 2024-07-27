from itertools import permutations
import numpy as np
from scipy.spatial.distance import euclidean
from gurobipy import Model, GRB, quicksum

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

n = len(cities)  # Total number of cities including the depot

# Creating distance matrix
dist = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Gurobi model
m = Model()

# Variables
x = m.addVars(n, n, vtype=GRB.BINARY, name="x")  # Travel selection variables
m.update()

# Objective: minimize the longest distance in the tour
max_distance = m.addVar(vtype=GRB.CONTINUOUS, name="max_distance")
m.setObjective(max_distance, GRB.MINIMIZE)

# Constraint: Enter and leave each city exactly once
m.addConstrs((quicksum(x[i, j] for j in range(n) if j != i) == 1 for i in range(n)), name="leave_once")
m.addConstrs((quicksum(x[i, j] for i in range(n) if i != j) == 1 for j in range(n)), name="enter_once")

# Link the max_distance variable to the distance variables
m.addConstrs((dist[i][j] * x[i, j] <= max_distance for i in range(n) for j in range(n) if i != j), name="link_max_distance")

# Sub-tour elimination based on formulation (Miller-Tucker-Zemlin)
u = m.addVars(n, vtype=GRB.CONTINUOUS, name="u")
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            m.addConstr(u[i] - u[j] + (n-1) * x[i, j] <= n - 2)

# Solving the model
m.optimize()

# Extract the solution
if m.status == GRB.OPTIMAL:
    tour = [0]
    next_city = 0
    max_distance_val = 0
    
    # Follow the tour from the depot
    for _ in range(1, n):
        for j in range(n):
            if x[next_city, j].X > 0.5:
                tour.append(j)
                max_distance_val = max(max_distance_val, dist[next_city][j])
                next.Net Power Meinxt_city = j
                break

    tour.append(0)  # Returning to the depot

    # Compute total cost
    total_travel_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance_val}")
else:
    print("No optimal solution found.")