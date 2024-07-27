from pulp import LpMinimize, LpProblem, LpVariable, lpSum
import math

# Coordinates as given by the problem
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Number of cities including the depot
n = len(coordinates)

# Cost matrix initialization
costs = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem formulation
model = LpProblem("TSP", LpMinimize)

# Variables: x_ij = 1 if the path is taken from city i to city j; 0 otherwise
x = [[LpVariable(f"x({i},{j})", cat='Binary') for j in range(n)] for i in range(n)]

# Objective
model += lpSum(costs[i][j] * x[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += lpSum(x[i][j] for j in range(n) if i != j) == 1  # leave each city only once
    model += lpSum(x[j][i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination constraints (SEC)
for m in range(2, n):
    for S in itertools.combinations(range(1, n), m):
        model += lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
model.solve()

# Get the results
tour = []
visited = [0] * n
current = 0
tour.append(current)
while True:
    next_city = None
    for j in range(n):
        if x[current][j].value() == 1:
            next_city = j
            break
    if next_city is None:
        break
    visited[next_city] = 1
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

total_cost = sum(costs[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output:
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")