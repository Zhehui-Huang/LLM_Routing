import pulp
import math

# City coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Compute Euclidean distances between all pairs of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup problem
problem = pulp.LpProblem("Min-Max_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
U = pulp.LpVariable.dicts("U", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

# Objective: Minimize the maximum distance traveled between consecutive cities
max_dist = pulp.LpVariable("maximum_distance")
problem += max_dist

# Minimize the maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[i][j] * x[i, j] <= max_dist

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination
for i in range(n):
    for j in range(1, n):
        if i != j:
            problem += U[i] - U[j] + n*x[i, j] <= n-1

# Solve the problem
problem.solve()

# Get the results
tour = []
current = 0
visited = set([0])
tour.append(current)

while True:
    for j in range(n):
        if current != j and pulp.value(x[current, j]) == 1:
            max_dist_consec = distances[current][j]
            current = j
            tour.append(current)
            visited.add(current)
            break
    if current == 0:
        break

total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", pulp.value(max_dist))