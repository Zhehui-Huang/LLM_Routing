import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
m = 8
# Number of nodes including the depot
n = len(coordinates)

# Calculate distances
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distance = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create problem
problem = pulp.LpProblem("MultiRobotTSP", pulp.LpMinimize)

# Variables
x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for k in range(m)] for j in range(n)] for i in range(n)]
u = [pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(2, n)]

# Objective function
problem += pulp.lpSum(x[i][j][k] * distance[i][j] for i in range(n) for j in range(n) for k in range(m))

# Each city visited exactly once minus the depot
for j in range(1, n):
    problem += pulp.lpSum(x[i][j][k] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) - pulp.lpSum(x[j][i][k] for i in range(n) if i != j) == 0

# Leaving and returning to the depot
for k in range(m):
    problem += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination (MTZ constraints)
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                problem += u[i-2] - u[j-2] + n * x[i][j][k] <= n - 1

# Solve the problem
problem.solve()

# Gathering results and outputting tours and their costs
tours = [[] for _ in range(m)]
for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                tours[k].append(j)

# Calculate total travel cost per tour
costs = []
for k in range(m):
    cost = sum(distance[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k])-1))
    costs.append(cost)

max_cost = max(costs)

# Outputting results
for k in range(m):
    print(f"Robot {k} Tour: [0, " + ", ".join(str(city) for city in tours[k][1:]) + ", 0]")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Maximum Travel Cost: {max_cost}")