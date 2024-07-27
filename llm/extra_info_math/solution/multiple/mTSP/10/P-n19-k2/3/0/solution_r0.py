import pulp
import math

# City coordinates (including depot as city 0)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)  # number of nodes including the depot
m = 2  # number of robots

# Distance matrix
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

cost = [[distance(i, j) for j in range(n)] for i in range(n)]

# PuLP model
model = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), 
                          cat=pulp.LpBinary)  # travel from i to j by salesman k
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), 
                          lowBound=0, cat=pulp.LpContinuous)  # position in the tour

# Objective: minimize the total distance traveled by all salesmen
model += pulp.lpSum(cost[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
for j in range(1, n):
    model += sum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1  # each city is visited exactly once

for k in range(m):
    model += sum(x[0, j, k] for j in range(1, n)) == 1  # each salesman leaves the depot
    model += sum(x[j, 0, k] for j in range(1, n)) == 1  # each salesman returns to the depot
    
for k in range(m):
    for i in range(1, n):
        model += sum(x[i, j, k] for j in range(n) if i != j) - sum(x[j, i, k] for j in range(n) if i != j) == 0  # flow conservation
        
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + n * x[i, j, k] <= n - 1  # subtour elimination

# Solve the model
model.solve()

# Output results
for k in range(m):
    tour = [0]
    next_city = 0
    while True:
        next_city = next((j for j in range(n) if pulp.value(x[next_city, j, k]) == 1), None)
        if next rotatelock.array