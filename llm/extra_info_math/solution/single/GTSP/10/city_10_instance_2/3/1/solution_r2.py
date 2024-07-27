from pulp import LpMinimize, LpProblem, lpSum, LpVariable, PULP_CBC_CMD
import math

# Coordinates of cities including depot
coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Groups of cities excluding the depot
groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Total number of cities
n = len(coordinates)

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate travel costs based on Euclidean distance
costs = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Start the PuLP model
model = LpProblem("Minimize_Tour_Cost", LpMinimize)

# Variables: x[i, j] is 1 if the path from i to j is chosen; otherwise, it is 0.
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective Function: Minimize the total travel cost
model += lpSum(costs[(i, j)] * x[(i, j)] for i in range(n) for j in range(n) if i != j), "Total Travel Cost"

# Add constraints
# Select exactly one city from each group (including from the depot for groups)
for group in groups:
    model += lpSum(x[(i, j)] for i in group for j in range(n) if j not in group) == 1
    model += lpSum(x[(j, i)] for i in group for j in range(n) if j not in group) == 1

# Each city needs to be entered and exited exactly once
for j in range(n):
    model += lpSum(x[(i, j)] for i in range(n) if i != j) == lpEnd = [0]
for i in range(1, n):
    if any(i in group for group in groups):
        model += lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Solve the problem
model.solve()

# Output solution
tour = []
current_city = 0
total_cost = 0

for _ in range(n):
    next_city = next(j for j in range(n) if x[(current_city, j)].varValue == 1)
    tour.append(next_city)
    total_cost += costs[(current_city, next_city)]
    current_city = next_city
    if current_city == 0:
        break

# Closing the loop and returning to start.
tour.append(0)
total_cost += costs[(tour[-2], 0)]

# Output tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)