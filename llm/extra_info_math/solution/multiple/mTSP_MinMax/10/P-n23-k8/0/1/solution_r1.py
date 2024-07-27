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
u = pulp.LpVariable.dicts('u', (i for i in range(1, n)), lowBound=1, upBound=n-1, cat='Continuous')

# Objective
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')
prob += z

# Cost calculation and constraints linkage to z
for k in range(m):
    prob += pulp.lpSum(c[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= z

# Constraints
# Each city visited exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Start and return to depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += (pulp.lpSum(x[i, p, k] for i in range(n) if i != p) - pulp.lpSum(x[p, j, k] for j in range(n) if j != p)) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n) * x[i, j, k] <= n - 1

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Output the solution
tours = {k: [0] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    sequence = []
    next_city = 0
    while True:
        next_city = [j for j in range(n) if pulp.value(x[next_city, j, k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        if next_city == 0:
            break
        costs[k] += c[sequence[-1], next_city] if sequence else 0
        sequence.append(next

        _city)

    sequence.append(0)  # return to depot
    tours[k] = sequence

# Display tours
max_cost = max(costs.values())
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    if tours[k]:
        print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Maximum Travel Monitored Cost: {pulp.value(z)}")