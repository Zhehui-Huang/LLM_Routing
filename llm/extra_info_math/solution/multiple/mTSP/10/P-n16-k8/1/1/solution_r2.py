import pulp
import math

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

n = len(coordinates)  # Include depot
m = 8  # Number of robots

# Euclidean distance function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance (cost) matrix
cost_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the problem
prob = pulp.LpProblem("VRP_Multiple_Robots", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j),
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-1, cat=pulp.LpContinuous)

# Objective function
prob += pulp.lpSum(cost_matrix[i][j] * x[i,j,k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Each city is visited exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each city has exactly one departure per vehicle
for k in range(m):
    for i in range(n):
        prob += pulp.lpSum(x[i, j, k] for j in range(n) if i != j) == pulp.lpSum(x[j, i, k] for j in range(n) if i != j)

# Each robot leaves the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
prob.solve()

# Extract and print the solution
total_cost = 0
for k in range(m):
    tour = [0]
    current = 0
    while True:
        next_city = next(j for j in range(n) if pulp.value(x[current, j, k]) == 1)
        if next_city == 0:
            tour.append(next_city)
            break
        tour.append(next_city)
        current = next_city
    tour_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour['cost']

print(f"Overall Total Travel Cost: {total_cost}")