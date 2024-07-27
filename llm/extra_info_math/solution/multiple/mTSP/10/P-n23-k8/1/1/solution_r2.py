import pulp
import math

# Define the problem parameters
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
n = len(coordinates)  # Total number of nodes including depot
m = 8  # Number of robots/salesmen

# Calculate the Euclidean distance between any two cities
def calc_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create the distance matrix
distance_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem solver
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision Variables
x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for k in range(m)] for j in range(n)] for i in range(n)]
u = [pulp.LpVariable(f"u_{j}", lowBound=1, upBound=n-1, cat='Continuous') for j in range(1, n)]

# Objective function
prob += pulp.lpSum(distance_matrix[i][j] * x[i][j][k] for k in range(m) for i in range(n) for j in range(n))

# Constraints
# Each city is visited exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Each robot starts and ends at the depot.
for k in range(m):
    prob += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[i][0][k] for i in range(1, n)) == 1

# Subtour elimination constraints
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i-1] - u[j-1] + (n - 1) * x[i][j][k] <= n - 2

# Flow conservation
for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum(x[i][j][k] for i in range(n)) == pulp.lpSum(x[j][i][k] for i in range(n))

# Solve the problem
prob.solve()

# Collect results
overall_cost = 0
for k in range(m):
    tour = [0]
    for i in range(n - 1):
        next_city = next(j for j in range(n) if x[tour[-1]][j][k].value() == 1)
        tour.append(next_city)
        if next_city == 0:
            break
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")