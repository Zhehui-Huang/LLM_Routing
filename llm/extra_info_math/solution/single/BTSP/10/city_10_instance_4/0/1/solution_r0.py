import pulp as pl
import math

# City coordinates
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

n = len(coordinates)

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the problem
prob = pl.LpProblem("Minimax_TSP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function: Minimize the maximum travel distance
M = pl.LpVariable("M")
prob += M

# Constraints
for i in range(n):
    prob += pl.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave city i exactly once
    prob += pl.lpSum(x[j, i] for j in range(n) if i != j) == 1  # arrive in city i exactly once

# Only use the upper bound constraint on the path lengths
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[i][j] <= M

# Restrict sub-tours
for S in range(3, n):
    for subset in pl.get_subsets(range(1, n), S):
        prob += pl.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
visited = [0]  # starting from depot
current = 0
while len(tour) < n:
    for j in range(n):
        if pl.value(x[current][j]) == 1:
            tour.append(j)
            current = j
            break

# Compute outputs
tour.append(0)  # return to the depot
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(result)