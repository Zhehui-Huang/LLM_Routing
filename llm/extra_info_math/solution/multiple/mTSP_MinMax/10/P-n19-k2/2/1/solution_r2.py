import math
import pulp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distances between each pair of nodes
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

n = len(coordinates)  # Including the depot
m = 2  # Number of robots

# Creating distance matrix
dist = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Problem instantiation
problem = pulp.LpProblem("MRTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j),
                           cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Define a big M variable to minimize the max of the distances
M = pulp.LpVariable("M", lowBound=0, cat='Continuous')
problem += M

# Each non-depot city must be visited exactly once by exactly one robot
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation constraints for each robot at each city
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Minimize the maximum distance traveled
for k in range(m):
    problem += pulp.lpSum(dist[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= M

# Solve the problem
problem.solve()

# Print the output
routes = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j, k]) == 1:
                routes[k].append((i, j))
                costs[k] += dist[i, j]

# Display the results
for k in range(m):
    print(f"Robot {k} Tour: [0, " + ', '.join(f"{j}" for _, j in routes[k]) + ", 0]")
    print(f"Robot {k} Total Travel Cost: {costs[k]:.2f}")

print(f"Maximum Travel Cost: {pulp.value(M):.2f}")