import pulp
from math import sqrt

# City coordinates (city index starting from 0 including the depot)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and cities
m = 2  # Robots
n = len(coordinates)  # Cities including depot

# Calculate Euclidean distances between each pair of cities
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# VARIABLES
# Binary variable x[i][j][k]: 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j], cat='Binary')
# Continuous variable u[i] for Subtour Elimination
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# PROBLEM
problem = pulp.LpProblem("Multiple_TSP_Problem", pulp.LpMinimize)

# OBJECTIVE FUNCTION
problem += pulp.lpSum([distances[i, j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n) if i != j])

# CONSTRAINTS
# Each city (except depot) must be visited exactly once by all robots
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation: enter and exit each city
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Departure and arrival at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour Elimination Constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve the problem
problem.solve()

# Extract routes
tours = {k: [] for k in range(m)}
for k in range(m):
    link = {i: j for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j, k]) == 1}
    start = 0  # starting at depot
    while start in link:
        tours[k].append(start)
        start = link[start]

    tours[k].append(start)  # Ending at the depot

# Calculate travel costs
for k in range(m):
    tour_distance = sum(distances[tours[k][i], tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_distance}")

# Calculate the maximum distance traveled by the robots
max_distance = max(sum(distances[tours[k][i], tours[k][i + 1]] for i in range(len(tours[k]) - 1)) for k in range(m))
print(f"Maximum Travel Cost: {max_distance}")