import pulp as pl
import math

# City coordinates
coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Calculate euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Constructing distance matrix
n = len(coords)
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[(i, j)] = euclidean_data(coords[i], coords[j])

# Model
model = pl.LpProblem("TSP_Groups", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", distance_matrix, 0, 1, pl.LpBinary)
u = pl.LpVariable.dicts("u", range(1, n), 0, None)

# Objective
model += pl.lpSum([distance_matrix[i, j] * x[i, j] for i, j in distance_matrix])

# Constraints
for group in groups.values():
    model += pl.lpSum(x[i, j] for i in group for j in range(n) if j not in group) == 1
    model += pl.lpSum(x[j, i] for i in group for j in range(n) if j not in group) == 1

for i in range(n):
    model += pl.lpSum(x[i, j] for j in range(n) if i != j) == pl.lpSum(x[j, i] for j in range(n) if i != j)

for p in groups:
    for q in groups:
        if p != q:
            model += u[p] - u[q] + n * pl.lpSum(x[i, j] for i in groups[p] for j in groups[q]) + (n-1) * pl.lpSum(x[j, i] for i in groups[q] for j in groups[p]) <= n-1

# Solve model
model.solve()
tour = [0]
total_cost = 0

while len(tour) < len(groups) + 1:
    for i, j in distance_matrix:
        if pl.value(x[i, j]) == 1 and i == tour[-1]:
            tour.append(j)
            total_cost += distance_matrix[(i, j)]
            break

# Close the tour
tour.append(0)
total_cost += distance_matrix[(tour[-2], 0)]

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)