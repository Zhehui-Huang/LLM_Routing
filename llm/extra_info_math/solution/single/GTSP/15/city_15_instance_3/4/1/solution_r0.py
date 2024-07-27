import pulp
import math

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# City Groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Number of groups
k = len(groups)

# Calculate Euclidean distance between cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Configure the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(x[(i, j)] * distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), "Total_Distance"

# Constraints
# Constraint 2 & 3: Each cluster must have exactly one outgoing and incoming edge
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Constraint 4: Flow conservation
for i in range(1, len(coordinates)):
    problem += pulp.lpSum(x[(j, i)] for j in range(len(coordinates)) if i != j) == pulp.lpSum(x[(i, j)] for j in range(len(coordinates)) if i != j)

# Constraint 6: Subtour elimination
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0) for i in range(1, len(coordinates))}
for i in range(2, len(coordinates)):
    for j in range(2, len(coordinates)):
        if i != j:
            problem += u[i] - u[j] + k * x[(i, j)] + (k-2) * x[(j, i)] <= k-1

# Solve the model
problem.solve()

# Output results
tour = [0]
current = 0
visited = set([0])
total_cost = 0

while len(visited) < len(groups) + 1:
    for j in range(len(coordinates)):
        if j not in visited and pulp.value(x[(current, j)]) == 1:
            tour.append(j)
            total_cost += distance(current, j)
            current = j
            visited.add(j)
            break
tour.append(0)
total_cost += distance(current, 0)

print("Tour:", tour)
print("Total travel cost:", total_cost)