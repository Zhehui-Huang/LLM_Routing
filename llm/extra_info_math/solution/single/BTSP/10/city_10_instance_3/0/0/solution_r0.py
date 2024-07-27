import math
import mip
from itertools import combinations

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

n = len(cities)

# Calculate Euclidean distance between two cities
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Distance matrix
d = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Model setup
model = mip.Model()

# Variables
x = [[model.add_var(var_type=mip.BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]  # For subtour elimination
z = model.add_var()  # Maximum distance variable

# Objective: minimize the maximum distance in the tour
model.objective = mip.minimize(z)

# Constraints
for i in range(1, n):
    model += mip.xsum(x[i][j] for j in range(n) if j != i) == 1

for j in range(1, n):
    model += mip.xsum(x[i][j] for i in range(n) if i != j) == 1

# Subtour elimination
for S in combinations(range(1, n), 2):
    for i, j in combinations(S, 2):
        model += u[i] - u[j] + (n - 1) * x[i][j] + (n - 3) * x[j][i] <= n - 2

# Link the max distance variable
for i in range(n):
    for j in range(n):
        if i != j:
            model += z >= d[i][j] * x[i][j]

# Solve model
model.optimize()

# Extract tour
tour = [0]
for _ in range(n-1):
    prev = tour[-1]
    for j in range(n):
        if x[prev][j].x >= 0.99:
            tour.append(j)
            break

# End at the depot
tour.append(0)

# Compute tour statistics
total_cost = sum(d[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(d[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))