import math
from itertools import product
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

# City coordinates
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Define groups with adjusted index for 0-based array
groups = [
    [3, 9, 12, 16], [5, 6, 13], [8, 11, 15], 
    [1, 4, 14], [0, 2, 18], [7, 10, 17]
]

# Number of cities including depot
num_cities = len(coordinates)

# Calculate Euclidean distance
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# LP model
model = LpProblem("Minimize_Tour_Distance", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], cat=LpBinary)

# Objective function
model += lpSum(distance(i, j) * x[i, j] for i, j in x)

# Constraint for exactly one city from each group must be visited
for group in groups:
    model += lpSum(x[i, j] for i in group for j in range(num_cities) if i != j) == 1, f"exit_{group}"
    model += lpSum(x[j, i] for i in group for j in range(num_cities) if i != j) == 1, f"enter_{group}"

# Only one edge in/out from the depot
model += lpSum(x[0, j] for j in range(1, num_cities)) == 1, "Depot_out"
model += lpSum(x[j, 0] for j in range(1, num_cities)) == 1, "Depot_in"

# Continuity constraint to eliminate subtours
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            model += lpSum(x[k, j] for k in range(num_cities) if k != j) - lpSum(x[j, k] for k in range(num_cities) if k != j) == 0, f"continuity_{i}_{j}"

# Solve the problem
model.solve(PULP_CBC_ CMD(msg=False))

# Reconstruct tour based on variables
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_city = None
    for j in range(num_cities):
        if j != current_city and x[current_city, j].varValue == 1:
            next_city = j
            break
    if next_city is None:
        break
    current_city = next_city
    if current city == 0:
        break

# Calculate the trip total_distance
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Print output
print("Tour:", tour)
print("Total travel cost:", total_distance)