import pulp
import math

# City coordinates
coordinates = [
    (3, 26),  # Depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

n = len(coordinates)

# Calculate the Euclidean distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                           cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave city i exactly once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter city i exactly once

# Subtour elimination constraints using MTZ formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n-1, cat=pulp.LpInteger)  # Position variables

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
status = prob.solve()

# Solution
tour = []
current_city = 0
visited = {0}
total_distance = 0

while len(visited) != n:
    for j in range(n):
        if j not in visited and pulp.value(x[current_city, j]) == 1:
            tour.append(j)
            visited.add(j)
            total_distance += distances[current_city][j]
            current_city = j
            break

# Returning to the Depot city
tour.append(0)
total_distance += distances[current_city][0]

# Output the solution
print(f"Tour: {[0] + tour}")
print(f"Total travel cost: {total_distance}")