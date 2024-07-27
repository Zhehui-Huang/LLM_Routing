from itertools import product
from mip import Model, xsum, minimize, BINARY
import numpy as of np
from scipy.spatial.distance import euclidean

# Defining coordinates (with depot cities included)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),  # depots 0 to 3
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate distance matrix
n = len(coordinates)  # Number of nodes
distance_matrix = [[euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Model setup
model = Model()

# Decision variables
x = [[[model.add_var(var_type=BINARY) for k in range(n)] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]

# Model parameters
depots = range(4)  # Number of robots equals number of depots here

# Objective: Minimize the total travel cost
model.objective = minimize(xsum(distance_matrix[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in depots))

# Constraints
# Each robot must leave its depot and return to it
for k in depots:
    model += xsum(x[k][j][k] for j in range(n) if j != k) == 1
    model += xsum(x[j][k][k] for j in range(n) if j != k) == 1

# Each city must be visited exactly once from exactly one robot
for j in range(4, n):  # Skip depots
    model += xsum(x[i][j][k] for i in range(n) for k in depot) == 1

# Continuity of the route
for k in depots:
    for i in range(n):
        if i != k:  # Except for the depot
            model += xsum(x[i][j][k] for j in range(n)) == xsum(x[j][i][k] for j in range(n))

# Sub-tour elimination constraints (only for customers, not depots)
for i in range(4, n):
    for j in range(4, n):
        if i != j:
            model += u[i] - u[j] + n * xsum(x[i][j][k] for k in depots) <= n - 1

# Solving model
model.optimize()

# Extracting the solution
total_cost = 0
for k in depots:
    tour = [k]
    current = k
    while True:
        next_city = None
        for j in range(n):
            if x[current][j][k].x >= 0.99 and j not in tour:
                next_city = j
                break
        if next_city is None:
            break
        tour.append(next_city)
        current = next_city
    tour.append(k)  # return to depot
    route_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {route_cost}")
    total_cost += route_cost

print(f"Overall Total Travel Cost: {total_cost}")