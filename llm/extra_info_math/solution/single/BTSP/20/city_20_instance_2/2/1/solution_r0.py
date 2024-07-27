import math
from itertools import combinations
from mip import Model, xsum, minimize, BINARY

# City coordinates
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of Cities
n = len(coords)

# Distance calculation using Euclidean distance
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Create a model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
d = model.add_var()

# Objective: minimize the maximum distance d
model.objective = minimize(d)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination
for S in range(2, n):
    for subset in combinations(range(1, n), S):
        model += xsum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
       if i != j:
           model += x[i][j] * distance(i, j) <= d

# Solve the model
model.optimize()

# Extract the tour
tour = []
if model.num_solutions:
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                tour.append((i, j))
                break

# Start from the depot
start = 0
cur = start
visited = [False]*n
final_tour = [start]
while len(final_tour) < n:
    visited[cur] = True
    for i, j in tour:
        if i == cur and not visited[j]:
            final_tour.append(j)
            cur = j
            break
final_tour.append(start)  # returning to depot

# Calculate cost and maximum path length
total_cost = 0
max_dist = 0
for i in range(len(final_tour) - 1):
    dist = distance(final_tour[i], final_tour[i+1])
    total_cost += dist
    max_dist = max(max_dist, dist)

# Outputs
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")