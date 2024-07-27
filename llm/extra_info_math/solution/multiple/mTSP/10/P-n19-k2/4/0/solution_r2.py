import pulp
import math

# Coordinates of cities, including the depot
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots (salesmen)
m = 2
# Total number of nodes (including depot)
n = len(coords)

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the cost matrix (distance)
c = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Define the problem
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables: x[i, j, k] = 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')

# Position helper variables for subtour elimination (Eliminate subtours within the tour itself)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective function: minimize the total travel cost
model += pulp.lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints

# Each city is visited exactly once
for j in range(1, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

# Each robot starts and ends at the depot
for k in range(m):
    model += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Each robot leaves and enters each city only once
for k in range(m):
    for i in range(1, n):
        model += pulp.lpSum(x[i, j, k] for j in range(n)) == pulp.lpSum(x[j, i, k] for j in range(n))

# Subtour elimination constraints 
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve the problem
model.solve()

# Output results
for k in range(m):
    route = [0]
    while True:
        i = route[-1]
        j = next(j for j in range(n) if pulp.value(x[i, j, k]) == 1)
        if j == 0:
            break
        route.append(j)
    route.append(0)
    route_cost = sum(c[route[i]][route[i+1]] for i in range(len(route)-1))
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {k} Total Travel Cost: {route_cost}")

overall_cost = sum(sum(c[route[i]][route[i+1]] for i in range(len(route)-1)) for route in routes)
print(f"Overall Total Travel Cost: {overall_cost}")