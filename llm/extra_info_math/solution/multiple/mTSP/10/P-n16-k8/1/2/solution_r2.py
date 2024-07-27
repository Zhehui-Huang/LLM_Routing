import numpy as np
from scipy.spatial import distance
from mip import Model, xsum, minimize, BINARY, INTEGER

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Total nodes including the depot
n = len(coordinates)
# Number of robots
m = 8

# Euclidean distance matrix
c = [[distance.euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

model = Model()

# Variables: x[i][j][k] is 1 if robot k travels from i to j
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=INTEGER) for i in range(1, n)]

# Objective: minimize total travel cost
model.objective = minimize(xsum(c[i][j]*x[i][j][k] for i in range(n) for j in range(n) for k in range(m)))

# Constraints
# Each city is visited exactly once by exactly one robot
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Each robot leaves and re-enters the depot exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[j][0][k] for j in range(1, n)) == 1

# Continuity of visit for each city by each robot
for k in range(m):
    for j in range(1, n):
        model += xsum(x[i][j][k] for i in range(n)) - xsum(x[j][i][k] for i in range(n)) == 0

# Subtour elimination constraints
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i-1] - u[j-1] + (n-1) * xsum(x[i][j][k] for k in range(m)) <= n-2

# Solve the model
model.optimize()

# Retrieving and displaying the results
# Extract tours and compute the costs
tours = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    for i in range(n):
        for j in range(n):
            if x[i][j][k].x >= 0.99:
                tours[k].append((i, j))
                costs[k] += c[i][j]

# Reformatting the output
for k in tours:
    print(f"Robot {k} Tour:")
    tour_sequence = [0]  # initialize starting at the depot
    while len(tours[k]) > 0:
        for i, (origin, destination) in enumerate(tours[k]):
            if tour_sequence[-1] == origin:
                tour_sequence.append(destination)
                tours[k].pop(i)
                break
    print(f"Tour: {tour_sequence}")
    print(f"Total Travel Cost: {costs[k]}")

total_travel_cost = sum(costs.values())
print(f"Overall Total Travel Cost: {total_travel_total}")