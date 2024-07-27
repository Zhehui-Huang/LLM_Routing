import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

n = len(coordinates)
dist = { (i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Number of robots
m = 2

# Problem formulation
problem = pulp.LpProblem("Multiple_Robots_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective
M = pulp.LpVariable("M", lowBound=0, cat='Continuous')
problem += M, "Maximize the max traveled cost by any robot"

# Constraints

# Every city must be visited exactly once by any robot
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# Conservation constraints for robots
for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Each robot must leave the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Connection of the max constraint with the distances being traveled
for k in range(m):
    problem += pulp.lpSum(x[i, j, k] * dist[i, j] for i in range(n) for j in range(n) if i != j) <= M

# Solve the problem
problem.solve()

# Output results
tours = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                tours[k].append((i, j))
                costs[k] += dist[i, j]

for k in tours:
    tour = []
    current_location = 0
    while len(tours[k]) > 0:
        next_step = next((step for step in tours[k] if step[0] == current_location), None)
        if next_step:
            current_location = next_step[1]
            tours[k].remove(next_step)
            tour.append(current_location)
    print(f"Robot {k} Tour: {[0] + tour + [0]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Maximum Travel Cost: {pulp.value(M)}")