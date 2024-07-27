from itertools import combinations
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

n = len(cities)  # Number of cities

# Distance matrix calculation
dist = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Model setup
m = Model()

# Variables
x = m.addVars(n, n, vtype=GRB.BINARY, name="x")
u = m.addVars(n, vtype=GRB.CONTINUOUS, name="u")  # Helper variable for subtour elimination

# Objective: minimize the largest distance traveled between consecutive cities
max_distance = m.addVar(vtype=GRB.CONTINUOUS, name="max_distance")
m.setObjective(max_distance, GRB.MINIMIZE)

# Constraints
# Ensure each city is entered and left exactly once
m.addConstrs((quicksum(x[i, j] for j in range(n) if j != i) == 1 for i in range(n)), "leave_each_city")
m.addConstrs((quicksum(x[i, j] for i in range(n) if i != j) == 1 for j in range(n)), "enter_each_city")

# Subtour elimination constraints (Miller-Tucker-Zemlin formulation)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            m.addConstr(u[i] - u[j] + n * x[i, j] <= n-1)

# Maximize the smallest distance constraints
m.addConstrs((x[i, j] * dist[i][j] <= max_distance for i in range(n) for j in range(n) if i != j), "max_distance_constr")

# Solve model
m.optimize()

# Extract tour and calculate statistics
if m.status == GRB.OPTIMAL:
    tour = [0]
    next_city = 0
    total_cost = max_dist = 0
    while True:
        for j in range(n):
            if x[next_city, j].X > 0.5 and j not in tour:
                tour.append(j)
                total_cost += dist[next_city][j]
                max_dist = max(max_dist, dist[next_city][j])
                next_city = j
                break
        if next_city == 0:  # Back to the starting point
            break
            
    tour.append(0)  # Complete the tour by returning to the depot
    total_cost += dist[tour[-2]][0]  # Add cost to return to the depot
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("No solution found")