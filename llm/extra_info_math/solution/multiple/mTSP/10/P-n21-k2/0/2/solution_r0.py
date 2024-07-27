import pulp
from math import sqrt

# Coordinates of all cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of nodes and salesmen
n = len(coordinates)
m = 2

# Distance matrix
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

dist = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Variable creation using PuLP
problem = pulp.LpProblem("VRP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], cat='Binary')
u = pulp.LpVariable.dicts("u", [i for i in range(n)], lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum([x[i, j, k] * dist[i][j] for i in range(n) for j in range(n) for k in range(m)])

# Constraints
for j in range(1, n):
    problem += pulp.lpSum([x[i, j, k] for i in range(n) for k in range(m)]) == 1

for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum([x[i, j, k] for i in range(n)]) - pulp.lpSum([x[j, i, k] for i in range(n)]) == 0

for k in range(m):
    problem += pulp.lpSum([x[0, j, k] for j in range(1, n)]) == 1
    problem += pulp.lpSum([x[j, 0, k] for j in range(1, n)]) == 1

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solving the problem
problem.solve()

# Results display
routes = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                routes[k].append((i, j))

for k in routes:
    tour = [0]
    while len(routes[k]) > 0:
        for i, j in routes[k]:
            if i == tour[-1]:
                tour.append(j)
                routes[k].remove((i, j))
                break
    print(f"Robot {k} Tour: {tour}")
    cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Total Travel Cost: {cost}")

overall_cost = sum(dist[tour[i]][tour[i+1]] for k in routes for tour in [routes[k]] for i in range(len(tour)-1))
print(f"Overall Total Travel Cost: {overall_cost}")