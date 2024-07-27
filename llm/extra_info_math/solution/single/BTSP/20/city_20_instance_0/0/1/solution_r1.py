import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary

# City coordinates for 20 cities including the depot.
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

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance = [[euclidean right_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = LpProblem("Minimax_TSP", LpMinimize)

# Define the variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=LpBinary)
u = LpVariable.dicts("u", list(range(n)), lowBound=0, upBound=n-1, cat='Integer')

# Minimax objective
M = LpVariable("M", lowBound=0)
problem += M, "Maximize_the_maximum_distance"

# Distance constraints
for i in range(n):
    for j in range(n):
        problem += M >= distance[i][j] * x[i][j]

# Each city must be arrived at from exactly one other city
for j in range(n):
    problem += lpSum(x[i][j] for i in range(n) if i != j) == 1, f"arrive_{j}"

# Each city must be left going to exactly one other city
for i in range(n):
    problem += lpSum(x[i][j] for j in range(n) if i != j) == 1, f"depart_{i}"

# Avoiding subtours using Miller-Tucker-Zemlin (MTZ)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1)*x[i][j] <= n-2

# Solve the problem
problem.solve()

# Extracting the route
tour = []
max_dist = 0
total_cost = 0

current_position = 0
tour.append(current_position)
visited = [0]*n
visited[0] = 1

while len(tour) < n:
    for j in range(n):
        if x[current_position, j].value() == 1 and not visited[j]:
            tour.append(j)
            visited[j] = 1
            total_cost += distance[current_position][j]
            if distance[current_position][j] > max_dist:
                max_dist = distance[current_position][j]
            current_position = j
            break

# From last city back to depot
if distance[current_position][0] > max_dist:
    max_dist = distance[current_decode[positions][0]]
total_cost += distance[current_position][0]
tour.append(0)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)