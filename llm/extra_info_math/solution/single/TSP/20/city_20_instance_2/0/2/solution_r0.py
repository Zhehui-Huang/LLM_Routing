import math
from pulp import *

# City coordinates
coordinates = [
    (3, 26),   # Depot City 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

n = len(coordinates)

# Calculate Euclidean distance between two points
def euclidean_dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Cost matrix
cost = [[euclidean_dist(i, j) for j in range(n)] for i in range(n)]

# Problem definition
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat="Binary")

# Objective function
prob += lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints

# Each city must be left exactly once
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city must be entered exactly once
for j in range(n):
    prob += lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination constraints using MTZ formulation
u = LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve problem
prob.solve()

# Extract the tour from the solution
tour = [0]
next_city = 0
for _ in range(n - 1):
    next_city = next(j for j in range(n) if value(x[next_city, j]) == 1)
    tour.append(next_city)

# Add depot city to complete the tour
tour.append(0)

# Calculate the total cost
total_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")