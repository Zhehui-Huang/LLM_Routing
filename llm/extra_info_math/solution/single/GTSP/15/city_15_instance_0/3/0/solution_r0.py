import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Define the locations of cities and groups
locations = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

groups = [
    [0, 2, 7, 10, 11, 14],   # Group 0 including depot
    [0, 1, 3, 5, 8, 13],     # Group 1 including depot
    [0, 4, 6, 9, 12]         # Group 2 including depot
]

# Calculate distance between any two cities
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

# Create cost matrix
n = len(locations)
cost = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Create the LP model
model = LpProblem("VRP_with_city_groups", LpMinimize)

# Variables: x_ij - 1 if travel from city i to city j, 0 otherwise
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=LpBinary)

# Objective function: minimize total distance traveled
model += lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraint: enter and leave each group exactly once
for group in groups:
    model += lpSum(x[0, j] for j in group if j != 0) == 1
    model += lpSum(x[j, 0] for j in group if j != 0) == 1

# Flow conservation constraints
for k in range(1, n):
    model += lpSum(x[i, k] for i in range(n) if i != k) - lpSum(x[k, j] for j in range(n) if j != k) == 0

# Solve the model
model.solve()

# Extract the solution
visited = []
for i in range(n):
    for j in range(n):
        if i != j and x[i, j].varValue == 1:
            visited.append((i, j))

# Create a tour from the solution
current_city = 0
tour = [0]
while len(tour) < 5:
    for (_, j) in visited:
        if _ == current_city:
            tour.append(j)
            current_city = j
            break

# Calculate total travel cost for the tour
total_travel_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the tour and the total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")