import pulp
import math

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of cities
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Distance matrix creation using Euclidean distance
n = len(coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Setting up the problem
model = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Variables: x_ij = 1 if the path between i and j is chosen
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: Minimizing the total travel cost
model += pulp.lpSum(x[i, j] * distances[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints to ensure each group has exactly one outgoing edge and one incoming edge
for group in groups:
    model += pulp.lpSum(x[0, j] for j in group) == 1
    model += pulp.lpSum(x[j, 0] for j in group) == 1

# Adding the correct flow conservation constraints
for i in range(1, n):
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) - pulp.lpSum(x[i, j] for j in range(n) if j != i) == 0

# Solve the problem
model.solve()

# Extracting the solution
tour = [0]
current_city = 0

while True:
    next_city = None
    for j in range(n):
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            next_city = j
            break
    if next_city == 0:
        tour.append(0)
        break
    tour.append(next_city)
    current_city = next_city

# Calculate the total travel dist
total_travel_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)