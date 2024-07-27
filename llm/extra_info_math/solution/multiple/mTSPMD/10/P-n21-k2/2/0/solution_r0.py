import math
from itertools import product
from mip import Model, xsum, minimize, BINARY

# Define the cities and their coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Number of nodes and depots
n = len(coordinates)
depots = [0, 1]
V_prime = list(set(range(n)) - set(depots))

# Calculate Euclidean distance between every pair of nodes
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create model
model = Model()

# Decision variables: x[i][j][k] = 1 if travel from i to j by a robot starting at depot k
x = [[[model.add_var(var_type=BINARY) for k in depots] for j in range(n)] for i in range(n)]

# Auxiliary variables to eliminate subtours: position of node i in the tour
u = [model.add_var() for i in range(n)]

# Objective: Minimize total distance traveled by all robots
model.objective = minimize(xsum(c[i][j] * x[i][j][k] for i, j, k in product(range(n), repeat=2, depots)))

# Constraints
# Each city is visited exactly once by exactly one robot
for j in V_prime:
    model += xsum(x[i][j][k] for i in range(n) for k in depots) == 1

# Each robot leaves its depot
for k in depots:
    model += xsum(x[k][j][k] for j in range(n) if j != k) == 1

# Each robot returns to its depot
for k in depots:
    model += xsum(x[j][k][k] for j in range(n) if j != k) == 1

# Flow conservation: amount leaving a node must equal amount entering it
for j in range(n):
    for k in depots:
        model += xsum(x[i][j][k] for i in range(n)) == xsum(x[j][i][k] for i in range(n))

# Subtour elimination constraints
for i in V_prime:
    for j in V_prime:
        if i != j:
            for k in depots:
                model += u[i] - u[j] + (n - 1) * x[i][j][k] <= n - 2

# Solve the problem
model.optimize()

# Extracting the solution
tours = {k: [] for k in depots}
for k in depots:
    # Start from the depot
    cur = k
    while True:
        next_city = next(j for j in range(n) if x[cur][j][k].x >= 0.99)
        if next_city == k:
            break
        tours[k].append(next_city)
        cur = next_city
    tours[k] = [k] + tours[k] + [k]  # Complete the tour by returning to the depot

# Calculate costs of the tours
tour_costs = {}
total_cost = 0
for k in depots:
    tour_costs[k] = sum(c[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    total_cost += tour_costs[k]
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]}")

print(f"Overall Total Travel Cost: {total_cost}")