import numpy as np
from scipy.spatial.distance import euclidean
from mip import Model, xsum, minimize, BINARY, optimize

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

n = len(coordinates)  # number of nodes including depot
m = 2  # number of robots

# Calculating Euclidean distances between all pairs of cities
c = [[euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(1, n)]

# Maximize the maximum of the minimum tour lengths
max_distance = model.add_var()
model.objective = minimize(max_distance)

# Constraints
# Each city visited exactly once
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation for each robot and each city
for k in range(m):
    for j in range(1, n):
        model += xsum(x[i][j][k] for i in range(n) if i != j) == xsum(x[j][i][k] for i in range(n) if i != j)

# Each robot leaves depot exactly once and returns exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i-1] - u[j-1] + (n-1) * x[i][j][k] <= n-2

# Max	distance constraint
for k in range(m):
    model += xsum(x[i][j][k] * c[i][j] for i in range(n) for j in range(n)) <= max_distance

# Solving
model.optimize()

print("Optimal solution found with objective value:", model.objective_value)

# Extracting tours
for k in range(m):
    tour = []
    for i in range(n):
        for j in range(n):
            if x[i][j][k].x >= 0.99:
                tour.append((i, j))
    print(f"Robot {k} Tour (edges): {tour}")