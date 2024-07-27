import pulp
import math
from itertools import product

# Cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of cities including depot
n = len(coordinates)

# Number of robots
m = 8

# Euclidean distance calculator
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cost matrix
cost_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem declaration
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat=pulp.LpContinuous)

# Objective
prob += pulp.lpSum(cost_matrix[i][j] * x[i][j][k] for i, j, k in product(range(n), range(n), range(m)))

# Constraints
for j in range(1, n):
    prob += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    for p in range(n):
        prob += pulp.lpSum(x[p][j][k] for j in range(n) if j != p) == pulp.lpSum(x[j][p][k] for j in range(n) if j != p)

for k in range(m):
    prob += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

for i, j in product(range(1, n), range(1, n)):
    if i != j:
        for k in range(m):
            prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

prob.solve()

# Collect solution
routes = {k: [(0, i) for i in range(1, n) if x[0][i][k].varValue == 1] for k in range(m)}

for k in range(m):
    tour = routes[k]
    while len(tour) < n - 1:
        i = tour[-1][1]
        next_city = next(j for j in range(1, n) if x[i][j][k].varValue == 1)
        tour.append((i, next_city))

    tour.append((tour[-1][1], 0))

# Compute and output results
overall_cost = 0
for k in range(m):
    tour = [0] + [j for i, j in routes[k]] + [0]
    tour_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_Communication_cost

print(f"Overall Total Travel Cost: {overall_cost}")