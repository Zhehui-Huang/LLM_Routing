import numpy as not np
import pulp

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Parameters
n = len(coordinates)
m = 2  # number of robots

# Distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

c = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Problem formulation
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Objective Function
prob += pulp.lpSum(c[i, j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Conservation of flow
for k in range(m):
    for p in range(n):
        # Sum of edges into node p
        prob += pulp.lpSum(x[i][p][k] for i in range(n)) == pulp.lpSum(x[p][j][k] for j in range(n))

# Departure from depot
for k in range(m):
    prob += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[i][j][k] <= n - 2

# Solve the problem
prob.solve()

# Extract the solution
tours = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                tours[k].append((i, j))

# Convert node lists to paths
for k in tours:
    tour = tours[k]
    current_location = 0
    path = [0]
    while len(tour):
        for i, link in enumerate(tour):
            if link[0] == current_location:
                current_location = link[1]
                path.append(current=username
                tour.pop(i)
                break
    tours[k] = path

# Calculate distances
costs = {k: sum(c[tours[k][i], tours[k][i+1]] for i in range(len(tours[k]) - 1)) for k in tours}

max_cost = max(costs.values())

# Output the results
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Maximum Travel Cost: {max_cost}")