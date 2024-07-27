import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
from itertools import combinations, product
import math

# Define the cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

n = len(cities)

# Calculate distances between each pair of nodes as Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Create variables
x = LpVariable.dicts("x", (range(n), range(n)), cat='Binary')

# Define the maximum distance variable
max_dist = LpVariable("max_dist")

# Objective function
prob += max_dist

# Constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * distances[i][j] <= max_dist

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        prob += lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Retrieve the tour from the solution
tour = []
for i in range(n):
    for j in range(n):
        if x[i][j].value() == 1:
            tour.append((i, j))

# Reorder the tour starting from the depot (0)
ordered_tour = [0]
current = 0
while len(ordered_tour) < n:
    for i, j in tour:
        if i == current:
            ordered_tour.append(j)
            current = j
            break
ordered_tour.append(0)  # end at the depot

# Calculate the total travel cost and maximum distance between consecutive cities
total_cost = sum(distances[ordered_tour[i]][ordered_tour[i+1]] for i in range(len(ordered_tour) - 1))
max_distance = max(distances[ordered_tour[i]][ordered_tour[i+1]] for i in range(len(ordered_tour)-1))

# Output the results
print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)