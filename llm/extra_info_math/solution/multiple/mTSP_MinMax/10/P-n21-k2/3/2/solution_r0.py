import pulp
import math

# Define the cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

n = len(coordinates)  # Number of nodes
m = 2  # Number of salesmen

# Define the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum travel cost
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(1, n):
        problem += pulp.lpSum(x[p, j, k] for j in range(n) if p != j) == pulp.lpSum(x[i, p, k] for i in range(n) if i != p)

# Each salesman leaves the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# Each salesman returns to the depot
for k in range(m):
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Minimize maximum distance traveled by any robot
for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j:
                problem += distance(i, j) * x[i, j, k] <= max_distance

# Solve the problem
problem.solve()

# Extract the tours
tours = [[0] for _ in range(m)]
costs = [0] * m
for k in range(m):
    curr_location = 0
    while True:
        next_step = [(j, x[curr_location, j, k].varValue) for j in range(n) if j != curr_location and x[curr_location, j, k].varValue > 0.5]
        if not next_step:
            break
        next_location = next_step[0][0]
        costs[k] += distance(curr_location, next_location)
        tours[k].append(next_location)
        curr_location = next_id[0]
    tours[k].append(0)  # Return to depot
    costs[k] += distance(curr_location, 0)

# Display the results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_distance.value()}")