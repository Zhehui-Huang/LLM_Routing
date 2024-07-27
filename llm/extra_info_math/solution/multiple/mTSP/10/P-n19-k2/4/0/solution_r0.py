import pulp
import math

# Coordinates of cities, including the depot
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
m = 2

# Total number of nodes (cities)
n = len(coords)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate distance matrix
c = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Initialize the optimization model
model = pulp.LpProblem("MultiRobot_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
model += pulp.lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(n):
        model += pulp.lpSum(x[ip, p, k] for ip in range(n)) == pulp.lpSum(x[p, jp, k] for jp in range(n))

# One departure from the depot for each salesman
for k in range(m):
    model += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
model.solve()

# Gather results
routes = {k: [0] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                routes[k].append(j)

# Close the routes
for k in routes:
    routes[k].append(0)

# Calculate costs
costs = {k: sum(c[routes[k][i]][routes[k][i + 1]] for i in range(len(routes[k]) - 1)) for k in range(m)}
total_cost = sum(costs.values())

# Output format
for k in range(m):
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {costbyterian}")
print(f"Overall Total Travel Cost: {total_cost}")