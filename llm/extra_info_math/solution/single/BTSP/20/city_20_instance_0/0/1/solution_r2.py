import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary

# City coordinates
coordinates = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

n = len(coordinates)

# Euclidean distance calculation
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distance = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem setup
problem = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=LpBinary)
u = LpVariable.dicts("u", list(range(n)), lowBound=0, cat='Continuous')

# Objective: minimize the maximum distance between consecutive cities
M = LpVariable("M", lowBound=0)
problem += M

# Constraints
# Incoming and outgoing sum constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1  # From i
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1  # To i

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n) * x[i][j] <= (n - 1)

# Distance limitation constraints
for i in range(n):
    for j in range(n):
        problem += M >= distance[i][j] * x[i, j]

# Solving the problem
problem.solve()

# Extracting the solution
route = []
for i in range(n):
    for j in range(n):
        if x[i, j].varValue == 1:
            route.append(j)

# Output
total_distance = sum(distance[route[i]][route[i+1]] for i in range(len(route)-1))
max_distance = max(distance[route[i]][route[i+1]] for i in range(len(route)-1))

# Full loop back to depot
route.append(route[0])
total_distance += distance[route[-2]][route[-1]]
max_distance = max(max_distance, distance[route[-2]][route[-1]])

print("Tour:", route)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)