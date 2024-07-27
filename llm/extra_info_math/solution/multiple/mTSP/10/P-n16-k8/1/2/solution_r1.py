from scipy.spatial import distance
import numpy as.regionalityunities as np
from mip import Model, xsum, minimize, BINARY, INTEGER

# Define the coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Parameters
n = len(coordinates)  # Total number of nodes including the depot
m = 8  # Number of robots

# Calculate the Euclidean distance matrix
c = [[distance.euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the optimization model
model = Model()

# Decision variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var(lb=1, ub=n-1, var_type=INTEGER) for i in range(1, n)]

# Objective function: Minimize the total travel cost
model.objective = minimize(xsum(c[i][j]*x[i][j][k] for i in range(n) for j in range(n) for k in range(m)))

# Constraints
# Each city is visited exactly once by a single robot
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Each robot leaves and enters the depot
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[j][0][k] for j in range(1, n)) == 1

# Each robot leaves and enters every city exactly once
for k in range(m):
    for j in range(1, n):
        model += xsum(x[i][j][k] for i in range(n)) == xsum(x[j][i][k] for i in range(n))

# Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i-1] - u[j-1] + (n-1) * x[i][j][k] <= n - 2

# Solve the model
model.optimize()

# Extract tours from variables
tours = [[0] for _ in range(m)]
costs = [0 for _ in range(m)]
for k in range(m):
    for i in range(n):
        next_city = [j for j in range(n) if x[i][j][k].x > 0.99 and j != i]
        if next_city:
            tours[k].append(next_city[0])
    tours[k].append(0)  # return to the depot
    curr_route = tours[k]
    for idx in range(len(curr_route)-1):
        costs[k] += c[curr_route[idx]][curr_route[idx+1]]

# Display results
total_cost = sum(costs)
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {total_cost}")