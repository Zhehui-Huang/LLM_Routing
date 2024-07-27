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
# Number of nodes
n = len(coordinates)

# Calculate distances
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distance = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("MultiRobotTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), cat=pulp.LpBinary)

# Objective
problem += pulp.lpSum(x[i, j, k] * distance[i][j] for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints

# Each city is visited exactly once by one salesman
for j in range(1, n):  # skip the depot
    problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Each salesman must leave each city including depot exactly once and enter each city once
for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Each salesman starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Solve the problem
problem.solve()

# Output tours for each robot
tours = [[] for _ in range(m)]
for k in range(m):
    tour = [0]  # start at depot
    next_city = 0
    while True:
        next_city = next(j for j in range(n) if pulp.value(x[next_city, j, k]) == 1)
        if next_city == 0:
            break
        tour.append(next_city)
    tour.append(0)  # return to depot
    tours[k] = tour

# Calculate travel cost for each tour
costs = []
for k in range(m):
    cost = sum(distance[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    costs.append(cost)
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {cost}")

# Maximum travel cost
max_cost = max(costs)
print(f"Maximum Travel Cost: {max_cost}")