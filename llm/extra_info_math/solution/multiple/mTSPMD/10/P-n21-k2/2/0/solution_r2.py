import math
from itertools import product
from mip import Model, xsum, minimize, BINARY

# Coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Number of cities
n = len(coordinates)
depots = [0, 1]
V_prime = list(set(range(n)) - set(depots))

# Distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create model
model = Model()

# Decision variables: x[i][j][k] = 1 if travel from i to j by a robot starting at depot k, and u for subtour avoidance
x = [[[model.add_var(var_type=BINARY) for k in depots] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]

# Objective function
model.objective = minimize(xsum(c[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in depots))

# Constraints
for j in V_prime:
    model += xsum(x[i][j][k] for i in range(n) for k in depots) == 1

for k in depots:
    model += xsum(x[k][j][k] for j in range(n) if j != k) == 1
    model += xsum(x[j][k][k] for j in range(n) if j != k) == 1

for k in depots:
    for i in range(n):
        model += xsum(x[i][j][k] for j in range(n)) == xsum(x[j][i][k] for j in range(n))

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * xsum(x[i][j][k] for k in depots) <= n-1

# Solve model
model.optimize()

# Extract solution
tours = {k: [] for k in depots}
for k in depots:
    next_loc = k
    tour = [k]
    while True:
        next_loc = next(j for j in range(n) if x[next_loc][j][k].x >= 0.99 and j not in tour)
        tour.append(next_loc)
        if next_loc in depots:
            break
    tours[k] = tour

# Print solution
total_cost = 0
for k in depots:
    cost = sum(c[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")