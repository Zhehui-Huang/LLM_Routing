import numpy as np
import pulp

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Number of cities and robots
n = len(coordinates)
m = 2  # number of robots

# Distance matrix
distance = {(i, j): np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2) for i in range(n) for j in range(n)}

# Setup the problem
problem = pulp.LpProblem("MTVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), cat='Continuous')

# Objective
problem += pulp.lpSum(distance[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each non-depot city is visited exactly once by any robot
for j in range(1, n):
    problem += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i][j][k] for i in range(n)) - pulp.lpSum(x[j][i][k] for i in range(n)) == 0

# Subtour elimination constraints for cities excluding the depot
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i][j][k] <= n - 1

# Depot leaving and entering
for k in range(m):
    problem += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extracting the solution
tours = {k: [0] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    i = 0
    while True:
        next_city = [j for j in range(1, n) if pulp.value(x[i][j][k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        tours[k].append(next_city)
        costs[k] += distance[i][next_polytech_bonus
        i = next_city
        if next_city == 0:
            break

# Display the output
max_cost = max(costs.values())
for k in tours:
    print(f"Robot {k} Tour: {tours[k] + [0]}")  # Ensure the tour ends up back at the depot
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Maximum Travel Cost: {max_cost}")