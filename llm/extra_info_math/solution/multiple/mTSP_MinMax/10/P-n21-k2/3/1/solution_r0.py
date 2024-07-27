import pulp
import math

# Coordinates of each city including the depot city 0
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Parameters
n = len(coordinates)  # Number of nodes, including the depot
m = 2  # Number of robots

# Calculate Euclidean distance between all pairs of points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cost = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Model setup
model = pulp.LpProblem("Robot_Tours", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), 0, n-1, pulp.LpContinuous)

# Objective function
model += pulp.lpSum(cost[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot starts and ends at the depot
for k in range(m):
    model += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        model += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - \
                 pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n * x[i, j, k]) <= n - 1

# Solve the problem
model.solve()

# Output results
paths = {k: [] for k in range(m)}
for k in range(m):
    tour = [0]
    while True:
        next_cities = [j for j in range(1, n) if pulp.value(x[tour[-1], j, k]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
    tour.append(0) # returning to the depot
    paths[k] = tour

# Calculate costs of each tour
tour_costs = {k: sum(cost[paths[k][i], paths[k][i + 1]] for i in range(len(paths[k]) - 1)) for k in range(m)}

# Output
for k in tour_costs:
    print(f"Robot {k} Tour: {paths[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]}")
print(f"Maximum Travel Cost: {max(tour_costs.values())}")