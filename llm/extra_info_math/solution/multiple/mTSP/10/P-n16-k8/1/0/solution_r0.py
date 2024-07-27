import pulp
import math

# Coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(coord1, coord2):
    """ Euclidean distance calculation """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix creation
n = len(coordinates)
c = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem parameters
m = 8  # number of salesmen, i.e., robots

# PuLP model setup
prob = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in range(m) for i in range(n) for j in range(n)],
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", [i for i in range(1, n)], lowBound=0, cat=pulp.LpContinuous)

# Objective Function
prob += pulp.lpSum([c[i][j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n)])

# Constraints  

# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    prob += pulp.lpSum([x[i, j, k] for k in range(m) for i in range(n) if i != j]) == 1

# Saleman leaves and enters each city
for k in range(m):
    for p in range(1, n):
        prob += pulp.lpSum([x[p, j, k] for j in range(n) if j != p]) - \
                pulp.lpSum([x[i, p, k] for i in range(n) if i != p]) == 0

# Each salesman leaves the depot
for k in range(m):
    prob += pulp.lpSum([x[0, j, k] for j in range(1, n)]) == 1
    
# Each salesman returns to the depot
for k in range(m):
    prob += pulp.lpSum([x[j, 0, k] for j in range(1, n)]) == 1
    
# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve the problem
prob.solve()

# Output the solution
overall_cost = 0
for k in range(m):
    tour = [0]
    for i in range(n):
        if pulp.value(x[0, i, k]) == 1:
            j = i
            break
    while j != 0:
        tour.append(j)
        next_city = next(i for i in range(n) if pulp.value(x[j, i, k]) == 1 and i != j)
        j = nextcity if nextcity != 0 else 0
        if j == 0:
            tour.append(0)
    tour_length = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += tour_length
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_length}\n")

print(f"Overall Total Travel Travel Cost: {overall_cost}")