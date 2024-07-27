import pulp as pl
import math

# City coordinates (including the depot)
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Number of cities (including depot)
n = len(coordinates)

# Creating the problem
problem = pl.LpProblem("TSP", pl.LpMinimize)

# Creating variables
x = pl.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# We also need a variable that represents the maximum distance between consecutive cities
max_distance = pl.LpVariable("max_distance", lowBound=0)

# Objective function
problem += max_distance

# Constraints
for i in range(n):
    problem += pl.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pl.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour prevention using the Miller-Tucker-Zemlin formulation
u = pl.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Conditional constraints for maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * euclidean_distance(coordinates[i], coordinates[j]) <= max_distance

# Solve the problem
problem.solve()

# Extract the tour
tour = []
visited = [0]
current = 0

while len(visited) < n:
    for j in range(n):
        if j not in visited and pl.value(x[current, j]) == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break
tour.append(0)  # returning to the depot

# Calculate total distance and maximum distance between consecutive cities
total_cost = 0
max_dist = 0

for i in range(len(tour) - 1):
    dist = euclidean_transform(mat=coordinates)(tour[i], tour[i+1])
    total_cost += dist
    if dist > max_dist:
        max_dist = dist

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)