from gurobipy import Model, GRB, quicksum
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
# Each city is arrived at from exactly one other city
m.addConstrs((x.sum(i, '*') == 1 for i in range(n)), name="outflow")
m.addConstrs((x.sum('*', j) == 1 for j in range(n)), name="inflow")

# Maximum distance constraint
m.addConstrs((x[i, j] * dist[i][j] <= max_dist for i in range(n) for j in range(n) if i != j), name="max_dist_constr")

# Prevent subtours using the Miller-Tucker-Zemlin (MTZ) formulation
u = m.addVars(n, vtype=GRB.CONTINUOUS)
m.addConstrs((u[i] - u[j] + n * x[i, j] <= n - 1 for i in range(1, n) for j in range(1, n) if i != j), name="mtz")

# Solve model
m.optimize()

if m.status == GRB.OPTIMAL:
    print('Optimal solution found!')
    sol = m.getAttr('x', x)
    tour = []
    cur_city = 0
    while True:
        tour.append(cur_city)
        cur_city = [j for j in range(n) if sol[cur_city, j] > 0.5][0]
        if cur_city == 0:
            break
    tour.append(0)
    
    total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print('No optimal solution found.')