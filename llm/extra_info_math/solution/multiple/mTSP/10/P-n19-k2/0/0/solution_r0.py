import pulp
import math

# Defining function to calculate Euclidean distance
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
n = len(cities) # Total nodes
m = 2 # Number of salesmen

# Create the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 
                          cat='Binary', lowBound=0, upBound=1)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Objective
cost = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
objective = pulp.lpSum(x[i, j, k] * cost[i][j] for i in range(n) for j in range(n) for k in range(m))
prob += objective

# Constraints
# Each city is visited exactly once by one salesman and only leave the depot if visited
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

# Salesmen must leave from and return to the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(1, n):
        prob += pulp.lpSum(x[i, p, k] for i in range(n) if i != p) - pulp.lpSum(x[p, j, k] for j in range(n) if j != p) == 0

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n*x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Printing the solution
routes = {k: [0] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    current_location = 0
    next_location = None
    while True:
        next_locations = [j for j in range(n) if pulp.value(x[current_location][j][k]) == 1]
        if not next_locations:
            break
        next_location = next_locations[0]
        costs[k] += cost[current_location][next_location]
        if next_location == 0:
            break
        else:
            routes[k].append(next_location)
            current_location = next_location
    routes[k].append(0) # complete the cycle
    costs[k] += cost[current_location][0] # Return cost to depot

# Output the results
overall_cost = sum(costs[k] for k in range(m))
for k in range(m):
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Overall Total Travel Cost: {overall_cost}")