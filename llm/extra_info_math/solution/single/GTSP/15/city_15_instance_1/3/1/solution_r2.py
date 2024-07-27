from math import sqrt
import pulp

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Group definitions (not including the depot city 0)
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distances between all pairs
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Define the problem
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Variable x[i][j] is 1 if the path goes from i to j, else 0; excluding self-loop
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), cat='Binary')

# Objective Function
objective = pulp.lpSum(x[(i, j)] * distances[i][j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)
model += objective

# Each group must have exactly one node visited and must connect exactly once to another node
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if i != j) == 1  # exactly one exiting
    model += pulp.lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if i != j) == 1  # exactly one entering

# Each city must be left and entered exactly once (except depot which gets entered last)
for k in range(1, len(coordinates)):
    model += pulp.lpSum(x[(k, j)] for j in range(len(coordinates)) if j != k) == pulp.lpSum(x[(i, k)] for i in range(len(coordinates)) if i != k)

# Ensuring depot links
model += pulp.lpSum(x[(0, j)] for j in range(1, len(coordinates))) == 1  # one exit from depot
model += pulp.lpSum(x[(j, 0)] for j in range(1, len(coordinates))) == 1  # one entry to depot

# Solve the model
model.solve()

# Computing the output tour and total travel cost
tour = [0]
current = 0
while True:
    next_city = [j for j in range(len(coordinates)) if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_city:
        break
    next_city = next_this[0]
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

# Compute the total distance of the tour
total_travel_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)