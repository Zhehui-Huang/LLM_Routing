import numpy as lv
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
m = 8
# Total nodes, including the depot
n = len(coordinates)

# Calculating Euclidean distance matrix
c = [[np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j])) for j in range(n)] for i in range(n)]

# Problem setup
prob = LpProblem("RobotRouting", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat=LpBinary)
u = LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective Function
prob += lpSum(c[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
for j in range(1, n):
    prob += lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    for p in range(n):
        prob += lpSum(x[(i, p, k)] for i in range(n) if i != p) - lpSum(x[(p, j, k)] for j in range(n) if j != p) == 0
    prob += lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    prob += lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# Subtour Elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[(i, j, k)] <= n - 1

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

if prob.status == 1:
    # Solver found an optimal solution
    tours = {k: [0] for k in range(m)}
    for k in range(m):
        for i in range(n):
            for j in range(n):
                if i != j and x[(i, j, k)].varValue > 0.99:
                    tours[k].append(j)

    total_cost = 0
    for k in range(m):
        tour = tours[k]
        if len(tour) > 1:
            tour.append(0)
        tour_cost = sum(c[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("Solution is infeasible or not optimal.")