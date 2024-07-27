import pulp
from math import sqrt

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the distance matrix
n = len(coordinates)
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:  # No self-loops
            cost_matrix[(i, j)] = distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[(i, j)] = float('inf')  # No same-node travel

# Problem initialization
prob = pulp.LpProblem("VehicleRoutingProblem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2)),
                          cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(2)), "Total travel cost"

# Constraints

# Each city is visited exactly once by any salesman
for j in range(2, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(2)) == 1, f"One visit city {j}"

# Departure and return for each salesman. Two cities as depots
for k in range(2):
    prob += pulp.lpSum(x[k, j, k] for j in range(n)) == 1, f"Departure from depot {k}"
    prob += pulp.lpSum(x[j, k, k] for j in range(n)) == 1, f"Return to depot {k}"

# Flow conservation for each city and each depot
for k in range(2):
    for i in range(n):
        if i != k:  # ensure not counting depot self-loops
            prob += (pulp.lpSum(x[i, j, k] for j in range(n)) == pulp.lpSum(x[j, i, k] for j in range(n))), f"Flow conservation at city {i} for vehicle {k}"

# Solve the problem
prob.solve()

# Collect results
routes = {0: [], 1: []}
costs = {0: 0, 1: 0}
for k in range(2):
    depot = k
    next_city = depot
    while True:
        next_step = [j for j in range(n) if pulp.value(x[next_city, j, k]) == 1]
        if not next_step:
            break
        next_city = next_step[0]
        routes[k].append(next_city)
        costs[k] += cost_matrix[depot, next_city]
        depot = next_city
        if next_city == k:
            break

# Output results
overall_cost = sum(costs.values())
for k in range(2):
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {overall_cost}")