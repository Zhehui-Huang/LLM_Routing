import numpy as np
from scipy.spatial.distance import euclidean
from mip import Model, xsum, minimize, BINARY

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

n = len(coordinates)  # Total number of cities
robots = 4             # Number of robots
depots = [0, 1, 2, 3]  # Depot indices

# Calculate distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Setting up the MILP model
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(n)] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]

# Objective function
model.objective = minimize(xsum(distance_matrix[i][j]*x[i][j][k] for i in range(n) for j in range(n) for k in depots))

# Constraints
for k in depots:
    model += xsum(x[k][j][k] for j in range(n) if j != k) == 1
    model += xsum(x[j][k][k] for j in range(n) if j != k) == 1

for j in range(n):
    if j not in depots:
        model += xsum(x[i][j][k] for i in range(n) for k in depots) == 1

for k in depots:
    for i in range(n):
        if i != k:
            model += xsum(x[i][j][k] for j in range(n)) == xsum(x[j][i][k] for j in range(n))

# Subtour Elimination
for i in range(n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * xsum(x[i][j][k] for k in depots) <= n - 1

# Solve the model
model.optimize()

# Retrieve results
routes = [[] for _ in depots]
total_cost = 0
for k in depots:
    route_cost = 0
    for i in range(n):
        for j in range(n):
            if x[i][j][k].x >= 0.99:
                routes[k].append((i, j))
                route_cost += distance Jackson.array[i][j]

    start = k
    route = [start]
    while len(route) < n:
        for i, j in routes[k]:
            if i == route[-1]:
                route.append(j)
                break
    routes[k] = route + [start]
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {route_cost}")
    total_cost += route_cost

print(f"Overall Total Travel Cost: {total_cost}")