#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:51:14 2024

@author: shiguangyao
"""

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 15 # number of nodes (including depot)
m = 3  # number of salesmen
K = 2  # minimum number of nodes a salesman must visit
L = np.ceil(n/m)+1  # maximum number of nodes a salesman may visit

# Randomly generate node locations
np.random.seed(0)
locations = np.random.rand(n, 2) * 100

# Compute the Euclidean distance matrix
c = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        c[i][j] = np.linalg.norm(locations[i] - locations[j])

# Create a new model
model = gp.Model("mTSP")

# Create variables
x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
u = model.addVars(n, vtype=GRB.INTEGER, name="u")

# Set objective function
model.setObjective(gp.quicksum(c[i][j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

# Add constraints
# Flow conservation at the depot
model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == m, "c1")
model.addConstr(gp.quicksum(x[j, 0] for j in range(1, n)) == m, "c2")

# Node degree constraints
model.addConstrs((gp.quicksum(x[i, j] for i in range(n) if i!=j) == 1 for j in range(1, n)  ), "c3")
model.addConstrs((gp.quicksum(x[i, j] for j in range(n) if j!=i) == 1 for i in range(1, n) ), "c4")

# Bounding constraints
model.addConstrs((u[i] + (L - 2) * x[0, i] - x[i, 0] <= L - 1 for i in range(1, n)), "c5")
model.addConstrs((u[i] + x[0, i] + (2 - K) * x[i, 0] >= 2 for i in range(1, n)), "c6")

# Single visit restriction
model.addConstrs((x[0, i] + x[i, 0] <= 1 for i in range(1, n)), "c7")

# Subtour elimination constraints (SECs)
model.addConstrs((u[i] - u[j] + L * x[i, j] + (L - 2) * x[j, i] <= L - 1 for i in range(1, n) for j in range(1, n) if i != j), "c8")

# Optimize model
model.optimize()

# Print the results
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    print("Objective value:", model.objVal)
    routes = []
    for i in range(n):
        for j in range(n):
            if x[i, j].X > 0.5:  # if x[i, j] is 1
                print(f"x[{i},{j}] = 1")
                routes.append((i, j))
    for i in range(n):
        print(f"u[{i}] = {u[i].X}")
else:
    print("No optimal solution found")

# Visualization
plt.figure(figsize=(10, 10))
plt.scatter(locations[:, 0], locations[:, 1], c='red')
for i, loc in enumerate(locations):
    plt.text(loc[0], loc[1], f'{i}', fontsize=12, ha='right')

# Plot the routes
for i, j in routes:
    plt.plot([locations[i][0], locations[j][0]], [locations[i][1], locations[j][1]], 'b-')

plt.title('Routes of Salesmen')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()

# Clean up
model.dispose()
