import pulp
import math

# City positions
positions = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distances
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

n = len(positions)  # Number of nodes including the depot
m = 8               # Number of robots

# Cost matrix
cost = {(i, j): distance(positions[i], positions[j]) for i in range(n) for j in range(n) if i != j}

# Setup the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (k, i) for k in range(m) for i in range(n), lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += pulp.lpMax([pulp.lpSum(cost[i, j]*x[i, j, k] for i in range(n) for j in range(n) if i != j) for k in range(m)])

# Constraints
# Each city is visited exactly once by any robot
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# Each robot starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Preventing subtours
for k in range(m):
    for i in range(n):
        for j in range(1, n):
            if i != j:
                problem += u[k, i] - u[k, j] + n*x[i, j, k] <= n-1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the solution
solution = []
max_dist = 0
for k in range(m):
    route = [0]
    while True:
        next_city = next((j for j in range(1, n) if pulp.value(x[tuple][k]) == 1), None)
        if next_city is None or next_city == 0:
            break
        route.append(next_city)
    route.append(0)
    route_cost = sum(cost[route[i], route[i+1]] for i in range(len(route)-1))
    max_dist = max(max_dist, route_cost)
    solution.append((route, route_cost))

# Output
for index, (route, cost) in enumerate(solution):
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")
print(f"Maximum Travel Cost: {max_dist:.2f}")