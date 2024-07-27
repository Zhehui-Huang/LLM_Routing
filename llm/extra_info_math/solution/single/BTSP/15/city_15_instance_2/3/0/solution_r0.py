import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary, LpStatus, value

# Coordinates of cities including the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Number of cities (including the depot)
n = len(coordinates)

# Function to calculate Euclidean distance
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distances = [[euclidean_dist(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = LpProblem("TSP_Minimax", LpMinimize)

# Variables: x_ij (1 if travel from i to j, 0 otherwise)
x = LpVariable.dicts("x", (range(n), range(n)), 0, 1, LpBinary)

# Constraint: Enter and leave each city exactly once
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1, f"Enter_{i}"
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1, f"Leave_{i}"

# Artificial variable for minimizing the maximum distance
max_distance = LpVariable("max_distance", lowBound=0)

# Objective: Minimize the maximum distance between consecutive cities
prob += max_distance

# Constraints to bound the distances by the maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[i][j] <= max_distance, f"MaxDist_{i}_{j}"

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_location = 0
while True:
    tour.append(current_location)
    next_location = None
    for j in range(n):
        if value(x[current_location][j]) == 1:
            next_location = j
            break
    if next_location == 0:
        break
    current_location = next_location

# Append the depot to complete the tour
tour.append(0)

# Calculate the total travel cost and maximum distance
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance_travel = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_travel:.2f}")