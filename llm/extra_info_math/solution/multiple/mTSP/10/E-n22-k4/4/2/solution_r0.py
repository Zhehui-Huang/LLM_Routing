import numpy as np
import pulp
from math import sqrt

# City coordinates
coords = {
    0: (145, 215),
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239),
    9: (163, 236), 10: (148, 232), 11: (128, 231), 12: (156, 217),
    13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206),
    17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

# Distance matrix calculation
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coords)  # Total cities including depot
m = 4  # Number of robots

# Distance matrix
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])

# PuLP Problem setup
problem = pulp.LpProblem("MDTSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(dist_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Visit each city exactly once
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        problem += pulp.lpSum(x[i, p, k] for i in range(n) if i != p) - pulp.lpSum(x[p, j, k] for j in range(n) if j != p) == 0

# One departure from depot for each robot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# No subtour formation
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * pulp.lpSum(x[i, j, k] for k in range(m)) <= n - 1

# Solve problem using PuLP solver
solver = pulp.getSolver("PULP_CBC_CMD", msg=0)
problem.solve(solver)

# Output tours and costs
overall_cost = 0
for k in range(m):
    print(f"Robot {k} Tour:")
    tour = [0]
    next_city = tour[-1]
    while True:
        found = False
        for j in range(n):
            if j != next_city and x[next_city, j, k].varValue == 1:
                tour.append(j)
                next_city = j
                found = True
                break
        if not found or next_city == 0:
            break
    tour.append(0)
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += tour_cost
    print(f"{tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")