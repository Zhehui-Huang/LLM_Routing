import pulp
import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}
n = len(cities)
m = 2  # Number of robots

# Create the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Cost matrix
cost = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Objective function
prob += pulp.lpSum(x[i, j, k] * cost[i][j] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Salesmen leave from and return to the depot
for k in range(m):
    prob += pulp.lpSum(x[0][j][k] for j in range(n) if j != 0) == 1
    prob += pulp.lpSum(x[j][0][k] for j in range(n) if j != 0) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += pulp.lpSum(x[i][p][k] for i in range(n) if i != p) == pulp.lpSum(x[p][j][k] for j in range(n) if j != p)

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

# Solve the problem
prob.solve()

# Solution extraction
routes = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                routes[k].append((i, j))
                costs[k] += cost[i][j]

# Reconstruct the routes from the tuples
for k in routes:
    route = routes[k]
    start = 0
    ordered_route = [0]
    while route:
        for i, (s, d) in enumerate(route):
            if s == start:
                ordered_route.append(d)
                start = d
                route.pop(i)
                break
    if ordered_route[-1] != 0:
        ordered_route.append(0)  # Make sure to return to depot
        costs[k] += cost[start][0]

# Output the results
overall_cost = sum(costs.values())
for k in routes:
    print(f"Robot {k} Tour: {ordered_route}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Overall Total Travel coerce it to float to ensure correct calculation Cost: {overall_cost}")