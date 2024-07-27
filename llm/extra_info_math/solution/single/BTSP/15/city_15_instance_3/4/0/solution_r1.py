from gurobphys import Model, GRB, quicksum
import math

# Cities coordinates with depot
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Number of cities
n = len(coordinates)

# Euclidean distance between cities
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
dist = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create model
m = Model()

# Decision variables: x[i, j] equals 1 if the road from i to j is in the tour, otherwise 0
x = m.addVars(n, n, vtype=GRB.BINARY, name="x")

# Objective: minimize the maximum traveled distance between two consecutive cities in the tour
max_dist = m.addVar(name="max_dist")
m.setObjective(max_dist, GRB.MINIMIZE)

# Add constraints
for i in range(n):
    m.addConstr(quicksum(x[i, j] for j in range(n) if i != j) == 1)
    m.addConstr(quicksum(x[j, i] for j in range(n) if i != j) == 1)

# Maximum distance constraint
m.addConstrs((x[i, j] * dist[i][j] <= max_dist for i in range(n) for j in range(n) if i != j), name="max_dist_constr")

# Subtour elimination
u = m.addVars(n, vtype=GRB.CONTINUOUS, name='u')
m.addConstrs((u[i] - u[j] + n * x[i, j] <= n - 1 for i in range(1, n) for j in range(1, n)), "subtour")

# Optimize
m.optimize()

# Extract solution
if m.status == GRB.OPTIMAL:
    print('Optimal solution found!')
    tour = []
    for i in range(n):
        for j in range(n):
            if x[i,j].X > 0.9:
                tour.append((i, j))
    path = [0]
    current = 0
    while len(tour) > 0:
        for i,j in tour:
            if i == current:
                path.append(j)
                current = j
                tour.remove((i,j))
                break
    path.append(0)

    total_travel_cost = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))
    max_travel_dist = max(dist[path[i]][path[i+1]] for i in range(len(path)-1))

    print("Tour:", path)
    print("Total travel cost:", total_travel_cost)
    print("Maximum distance between consecutive cities:", max_travel_dist)
else:
    print('No optimal solution found or there are still other issues.')