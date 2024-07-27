import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Calculate Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix creation
n = len(coordinates)
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Constants
num_robots = 8

# Problem setup
problem = pulp.LpProblem("min_cost_multiple_tsp", pulp.LpMinimize)

# Variables
x = {
    (i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary', lowBound=0, upBound=1)
    for i in range(n) for j in range(n) for k in range(num_robots) if i != j
}
u = {
    i: pulp.LpVariable(f"u_{i}", cat='Continuous', lowBound=0)
    for i in range(1, n)
}

# Objective
problem += pulp.lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(num_robots) if i != j), "Total Travel Cost"

# Constraints
# Each city except the depot is visited exactly once
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(num_robots) if i != j) == 1

# Flow conservation
for k in range(num_robots):
    for p in range(1, n):
        problem += pulp.lpSum(x[i, p, k] for i in range(n) if i != p) - pulp.lpSum(x[p, j, k] for j in range(n) if p != j) == 0

# Each robot leaves the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# Each robot returns to the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Get results
tours = [[] for _ in range(num_robots)]
costs = [0] * num_robots

for k in range(num_robots):
    tour = [0]
    current_location = 0
    while True:
        next_location = None
        for j in range(n):
            if j != current_location and pulp.value(x[current_location, j, k]) == 1:
                next_location = j
                costs[k] += c[current_location][j]
                tour.append(j)
                break
        current_location = next_location
        if current_location == 0:
            break
    tours[k] = tour + [0]

# Display results
total_cost = sum(costs)
for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Core: {total_cost}")