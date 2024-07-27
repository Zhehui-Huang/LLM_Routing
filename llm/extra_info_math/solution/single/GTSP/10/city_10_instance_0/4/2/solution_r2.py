import math
from itertools import product
from mip import Model, BINARY, xsum, minimize

# City coordinates and city groups
coordinates = {0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
               5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)}
groups = {0: [1, 2, 6], 1: [3, 7, 8], 2: [4, 5, 9]}

# Compute Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((coordinates[c1][0] - coordinates[c2][0])**2 + (coordinates[c1][1] - coordinates[c2][1])**2)

# Model initialization
model = Model()

# Variables
n = len(coordinates)
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]

# Objective: Minimize the distance
model.objective = minimize(xsum(distance(i, j) * x[i][j] for i in range(n) for j in range(n)))

# Constraints
# Each group must have exactly one outgoing edge to a node outside the group and vice versa
for members in groups.values():
    model += xsum(x[i][j] for i in members for j in range(n) if j not i) == 1
    model += xsum(x[j][i] for i in members for j in range(n) if j not i) == 1

# Each node must be exited and entered exactly once
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if j != i) == 1
    model += xsum(x[j][i] for j in range(n) if j != i) == 1

# Subtour elimination
for (i, j) in product(range(1, n), repeat=2):
    if i != j:
        model += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the model
model.optimize()

# Retrieve results
tour = []
visited = [0]
current = 0

while True:
    next_city = [j for j in range(n) if j != current and x[current][j].x >= 0.99]
    if not next_city:
        break
    next_city = next_city[0]
    visited.append(next_city)
    current = next_city
    if current == 0:
        break

total_cost = sum(distance(visited[i], visited[i+1]) for i in range(len(visited)-1))

# Output results
print("Tour:", visited)
print("Total travel cost:", total_cost)