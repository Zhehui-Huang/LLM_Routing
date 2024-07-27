import math
import pulp

# Define the coordinates of the cities (depot + 14 other cities)
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]
n = len(coordinates)

# Distance function
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i, j] = 0

# TSP Model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if route goes from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective - Minimize distance
model += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave i
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter i

# Solve the problem
model.solve()

# Extract tour
tour = []
current_location = 0
while len(tour) < n:
    for j in range(n):
        if j != current_location and pulp.value(x[current_location, j]) == 1:
            tour.append(j)
            current_location = j
            break

# Ensure tour returns to the starting point (depot)
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Results
print("Tour:", tour)
print("Total travel cost:", total_cost)