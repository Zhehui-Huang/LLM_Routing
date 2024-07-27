import numpy as np
from scipy.spatial.distance import euclidean
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary

# Define cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities
n = len(cities)

# Calculate distance matrix
distances = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean(cities[i], cities[j])
        distances[i, j] = dist
        distances[j, i] = dist

# Integer programming model
model = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpBinary)
dt_max = LpVariable("dt_max")

# Objective
model += dt_max

# Constraints
for i in range(n):
    model += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    model += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Sub-tour Elimination (using the Miller-Tucker-Zemlin formulation)
u = LpVariable.dicts("u", list(range(n)), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[(i, j)] <= n-1

# Maximizing distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[(i, j)] <= dt_max

# Solve the model
model.solve()

# Output settings
tour = []
max_distance = 0
current = 0

for _ in range(n):
    next_city = next(j for j in range(n) if x[(current, j)].varValue == 1)
    tour.append(current)
    max_distance = max(max_distance, distances[current][next_city])
    current = next_city

tour.append(0)  # Back to depot
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")