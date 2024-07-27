import numpy as no
from scipy.spatial.distance import euclidean
from mip import Model, xsum, minimize, BINARY, INTEGER

# Coordinates of cities, including the depot city 0
coordinates = [
    (30, 40),
    (37, 52),
    (49, 43),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 27),
    (37, 69),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

# Parameters
n = len(coordinates)  # Including the depot city
m = 2  # number of robots

# Distance calculation (Euclidean)
c = [[euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create a model
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var(lb=0, var_type=INTEGER) for i in range(n)]

# Objective: Minimize the maximum travel distance amongst all robots
max_travel = model.add_var()
model.objective = minimize(max_travel)

# Constraints
# Every city visited exactly once by one salesman
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        model += xsum(x[p][j][k] for j in range(n) if j != p) == xsum(x[i][p][k] for i in range(n) if i != p)

# Each robot leaves and returns to the depot exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += (u[i] - u[j] + (n - 1) * xsum(x[i][j][k] for k in range(m))) <= n - 2

# Assigning the maximum distance variable
for k in range(m):
    model += xsum(c[i][j] * x[i][j][k] for i in range(n) for j in range(n)) <= max_travel

# Optimize the model
model.optimize()

# Retrieve the solution
tours = {k: [0] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    for i in range(n):
        for j in range(n):
            if x[i][j][k].x >= 0.99:
                if tours[k][-1] == i:
                    tours[k].append(j)
                    costs[k] += c[i][j]

# Append depot return
for k in range(m):
    tours[k].append(0)
    costs[k] += c[tours[k][-2]][0]

# Output results
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]:.2f}")

max_cost = max(costs.values())
print(f"Maximum Travel Cost: {max_cost:.2f}")