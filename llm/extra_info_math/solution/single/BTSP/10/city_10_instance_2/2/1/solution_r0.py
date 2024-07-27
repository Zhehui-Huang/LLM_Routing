import pulp
import math
from itertools import combinations

# City coordinates
coordinates = [
    (90, 3),  # City 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

n = len(coordinates)

# Distance matrix using Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
prob = pulp.LpProblem("MinimizeMaxDistanceTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, pulp.LpBinary)
max_distance = pulp.LpVariable("max_distance")

# Objective function
prob += max_distance

# Constraints
# Constraint: Exactly one outgoing edge for each city
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Constraint: Exactly one incoming edge for each city
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Force max_distance to be at least the distance of each traveled edge
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distances[i][j] <= max_distance

# Sub-tour elimination constraints
for k in range(3, n+1):
    for S in combinations(range(1, n), k):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Fetching results
tour = []
visited = [0]
current = 0

while len(visited) < n:
    for j in range(n):
        if j != current and pulp.value(x[current, j]) == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break

tour = [0] + tour + [0]  # Start and end at the depot

# Total and maximum travel distances
total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance_value = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

output = {
    "Tour": tour,
    "Total travel cost": total_distance,
    "Maximum distance between consecutive cities": max_distance_value
}

output