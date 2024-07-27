import pulp
from math import sqrt

# Node coordinates
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
          (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Parameters
n = len(coords)  # Number of nodes including depot
m = 8  # Number of salesmen (robots)

# Calculate Euclidean distances
def distance(i, j):
    return sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

c = {(i, j): distance(i, j) for i in range(n) for j in range(n) if i != j}

# Problem
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', ((i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts('u', (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective
prob += pulp.lpSum(c[i, j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city visited exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Start at depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += (pulp.lpSum(x[i, p, k] for i in range(n) if i != p) - pulp.lpSum(x[p, j, k] for j in range(n) if j != p)) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve the problem
prob.solve()

# Output the solution
tours = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    tour = []
    i = 0
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[i, j, k]) == 1]
        if not next_cities:
            break
        j = next_cities[0]
        tours[k].append(j)
        costs[k] += c[i, j]
        i = j
        if j == 0:
            break
    tours[k].insert(0, 0)  # Start at depot

# Display tours
max_cost = max(costs.values())
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Maximum Travel Cost: {max_cost}")