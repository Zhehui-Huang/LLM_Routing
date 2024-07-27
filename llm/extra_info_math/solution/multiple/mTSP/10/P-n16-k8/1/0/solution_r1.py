import pulp
import itertools
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

n = len(coordinates)
m = 8  # Number of robots

# Distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Mathematical model
model = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], cat='Binary')
u = pulp.LpVariable.dicts("u", [i for i in range(1, n)], lowBound=1, upBound=n-1, cat='Continuous')

# Objective
model += pulp.lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints:
# Visit each city exactly once per robot
for j in range(1, n):
    model += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Exactly one entry and exit for each city for each robot
for k in range(m):
    for j in range(1, n):
        model += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) == pulp.lpSum(x[j][i][k] for i in range(n) if i != j)

# Depot constraints
for k in range(m):
    model += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1  # Leave depot
    model += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1  # Enter depot

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n - 1) * x[i][j][k] <= n - 2

# Solve the model
model.solve()

# Outputs
total_cost = 0
for k in range(m):
    tour = []
    for i in range(n):
        if pulp.value(x[0][i][k]) == 1:
            current_city = i
            break
    while current_city != 0:
        tour.append(current_city)
        next_city = next(j for j in range(n) if pulp.value(x[current_city][j][k]) == 1)
        current_city = next_city if next_city != 0 else 0
    if tour:
        tour_cost = sum(c[tour[i-1]][tour[i]] for i in range(1, len(tour)))
        total_cost += tour_cost
        tour.append(0)  # append depot as returning point
        print(f"Robot {k} Tour: [0] + {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}\n")

print(f"Overall Total Travel Cost: {total_cost}")