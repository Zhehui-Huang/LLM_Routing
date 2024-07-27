from math import sqrt
import pulp

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Groups, not including the depot (city 0 is always included as depot)
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate distances between all pairs of nodes
n = len(coordinates)
distances = [[euclidean_xyz_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Integer programming model
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables: x[i][j] = 1 if path goes from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Objective: Minimize total travel cost
model += pulp.lpSum(x[i, j] * distances[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city (excl. depot) is visited exactly once
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in range(n) if i != j) == 1

# Flow conservation at each city
for k in range(1, n):
    model += pulp.lpSum(x[i, k] for i in range(n) if i != k) == pulp.lpSum(x[k, j] for j in range(n) if j != k)

# Solve the problem
model.solve()

# Extract the solution
tour = [0]
current = 0
while True:
    for j in range(n):
        if j != current and pulp.value(x[current, j]) == 1:
            tour.append(j)
            current = j
            break
    if current == 0:
        break

# Calculate total distance
total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")