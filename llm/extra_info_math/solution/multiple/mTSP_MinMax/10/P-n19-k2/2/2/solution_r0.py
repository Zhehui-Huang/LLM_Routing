import numpy as np
from scipy.spatial.distance import euclidean
from mip import Model, xsum, minimize, BINARY

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

# Problem parameters
n = len(coordinates) # number of nodes including the depot
m = 2 # number of robots

# Calculating the Euclidean distances between every pair of cities
c = [[euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create a model
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]

# Objective: minimize the maximum travel distance amongst all robots
max_travel = model.add_var()
model.objective = minimize(max_travel)

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(1, n):
        model += xsum(x[p][j][k] for j in range(n) if j != p) - xsum(x[i][p][k] for i in range(n) if i != p) == 0

# Each salesman leaves and enters the depot exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1  # leave depot
    model += xsum(x[i][0][k] for i in range(1, n)) == 1  # enter depot

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * xsum(x[i][j][k] for k in range(m)) <= n - 1

# Assignment constraints: ensuring that each leg's travel cost does not exceed maximum travel
for k in range(m):
    model += xsum(x[i][j][k] * c[i][j] for i in range(n) for j in range(n) if i != j) <= max_travel

# Solving the model
model.optimize()

# Outputting the solution
tours = [[0] for _ in range(m)]
total_costs = [0] * m

# Building the tours for output
for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j and model.vars[x[i][j][k].ix].x >= 0.99:
                if i == 0 or j == 0:
                    # Only consider trips that start or end from the depot for starting a route trace
                    current_city = j
                    tours[k].append(current_city)
                    total_costs[k] += c[i][j]
                    while current_city != 0:
                        for l in range(n):
                            if l != current_city and model.vars[x[current_city][l][k].ix].x >= 0.99:
                                tours[k].append(l)
                                total_costs[k] += c[current_city][l]
                                current_city = l
                                break

# Append the depot to the end of each tour for returning
for k in range(m):
    tours[k].append(0)

# Display the computed tours and costs
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]:.2f}")

# Getting the maximum travel cost
max_cost = max(total_costs)
print(f"Maximum Travel Cost: {max_cost:.2f}")