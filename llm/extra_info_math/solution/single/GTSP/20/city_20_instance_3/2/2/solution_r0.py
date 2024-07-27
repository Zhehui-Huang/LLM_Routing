import pulp
import math

# Coordinates of the depot and each city
coordinates = [
    (30, 56),  # Depot
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16),
    (4, 43), (53, 76), (19, 72)
]

# City groups - each sublist represents a group
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Calculating Euclidean distances between all pairs of nodes (cities + depot)
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distances matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Create the linear programming problem
prob = pulp.LpProblem("MinimizeRouteCost", pulp.LpMinimize)

# Variables x_ij where i, j are cities + depot; x_ij = 1 if the path i->j is part of the route
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j}

# Objective: Minimize the sum of distances for the selected paths
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints
# Visit exactly one city from each group
for group in groups:
    prob += pulp.lpSum(x[0, j] for j in group) == 1
    prob += pulp.lpSum(x[j, 0] for j in group) == 1

# Flow conservation at each city
for j in range(1, len(coordinates)):
    prob += pulp.lpSum(x[i, j] for i in range(len(coordinates)) if i != j) - pulp.lpSum(x[j, k] for k in range(len(coordinates)) if k != j) == 0

# Solve the problem
prob.solve()

# Extract the path from the solution
path = []
current_position = 0
path.append(current_position)
next_position = None

# Construct the tour sequence
while True:
    next_position = next(j for j in range(len(coordinates)) if pulp.value(x[current_position, j]) == 1)
    path.append(next_position)
    if next_position == 0:
        break
    current_position = next_position

# Calculate the total cost of the tour
total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))

# Output the results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost}")