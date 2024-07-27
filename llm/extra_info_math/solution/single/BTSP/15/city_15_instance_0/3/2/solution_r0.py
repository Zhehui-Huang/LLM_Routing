from pulp import LpProblem, LpVariable, lpSum, LpMinimize
import math

# City coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65),
    (11, 40), (3, 21), (60, 55), (4, 39)
]

# Number of cities including depot
n = len(coordinates)

# Distance function
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
distances = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize LP Problem
model = LpProblem("TSP", LpMinimize)

# Variables
x = [[LpVariable(f"x({i},{j})", cat='Binary') if i != j else None for j in range(n)] for i in range(n)]
z = LpVariable("z", lowBound=0)

# Objective
model += z, "Maximization of the longest path"

# Constraints
for i in range(n):
    model += lpSum(x[i][j] for j in range(n) if i != j) == 1, f"Departure from {i}"
    model += lpSum(x[j][i] for j in range(n) if i != j) == 1, f"Arrival to {i}"

# Subtour elimination and z-constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += z >= distances[i][j] * x[i][j], f"Z update for edge ({i},{j})"

# Solving the problem
model.solve()

# Extracting the solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and x[i][j].value() == 1:
            tour.append((i, j))

# Construct an ordered tour starting and ending at the depot (0)
ordered_tour = []
current_location = 0
while len(ordered_tour) < n:
    for trip in tour:
        if trip[0] == current_location:
            ordered_tour.append(current_location)
            current_location = trip[1]
            break
ordered_tour.append(0)  # Append the return to depot city

# Calculate the tour cost and max distance
total_cost = sum(distances[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))
max_distance = max(distances[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))

result = {
    "Tour": ordered_tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": z.varValue
}

# Output result
result