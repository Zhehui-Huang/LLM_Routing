import math
from pulp import *

# Coordinates of cities
coordinates = [
    (26, 60),  # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2), (47, 50),
    (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), (75, 9),
    (52, 54), (64, 72), (14, 89)
]

n = len(coordinates)  # Total cities including depot

# Calculate Euclidean distance
def euclidean_dist(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj)**2 + (yi - yj)**2)

# Problem setup
prob = LpProblem("Minimax_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)
max_dist = LpVariable('max_dist', lowBound=0)

# Objective
prob += max_dist

# Constraints
# Each city must be entered and exited exactly once
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Eliminate subtours
for S in range(3, n):  # Subsets must exclude the depot
    for subset in itertools.combinations(range(1, n), S):
        prob += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * euclidean_dist(i, j) <= max_dist

# Solve the problem
prob.solve()

# Extract tour
tour = [0]
while len(tour) < n:
    for j in range(n):
        if j not in tour and x[(tour[-1], j)].varValue == 1:
            tour.append(j)
            break
tour.append(0)  # Return to the depot

# Calculate distances
total_distance = sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_edge_distance = max(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_edge_distance}")