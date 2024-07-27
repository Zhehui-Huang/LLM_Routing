import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary

# Data: City coordinates excluding the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), 
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), 
    (139, 182)
]

# Number of robots
m = 4

# Total number of nodes including the depot
n = len(coordinates)

# Calculate Euclidean distance between each pair of nodes
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the LP problem
problem = LpProblem("VRP_with_Multiple_Robots", LpMinimize)

# Define variables
x = [[LpVariable(f"x_{i}_{j}_{k}", cat=LpBinary) for k in range(m)] for j in range(n) for i in range(n)]
u = [LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(n)]

# Objective function
problem += lpSum(c[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city (except the depot) is visited exactly once by one salesperson
for j in range(1, n):
    problem += lpSum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Flow conservation for each robot and each city
for k in range(m):
    # Depot constraints
    problem += lpSum(x[0][j][k] for j in range(1, n)) == 1  # leaving depot
    problem += lpSum(x[j][0][k] for j in range(1, n)) == 1  # returning to depot
    for j in range(1, n):
        problem += lpSum(x[i][j][k] for i in range(n)) == lpSum(x[j][i][k] for i in range(n))

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * lpSum(x[i][j][k] for k in range(m)) <= n - 1

# Solve the problem
status = problem.solve()

# Extract results
tours = [[[] for _ in range(n)] for _ in range(m)]
costs = [0] * m

for k in range(m):
    for i in range(n):
        for j in range(n):
            if x[i][j][k].varValue > 0.5:
                tours[k][i].append(j)
                costs[k] += c[i][j]

# Output tour results
overall_cost = 0
for k in range(m):
    tour_path = [0]
    next_city = tours[k][0][0]
    while next_city != 0:
        tour_path.append(next_city)
        next_city = tours[k][next_city][0] if tours[k][next_city] else 0
    tour_path.append(0)
    print(f"Robot {k} Tour: {tour_path}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
    overall_cost += costs[k]

print(f"Overall Total Travel Cost: {overall_url_cost}")