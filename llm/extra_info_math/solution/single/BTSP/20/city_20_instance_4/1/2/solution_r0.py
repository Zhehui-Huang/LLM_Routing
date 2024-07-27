import numpy as as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
from itertools import combinations
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
x = LpVariable.dicts("x", (range(n), range(n)), cat=LpBinary)

# Objective function: minimize the maximum distance in the tour
prob += lpSum([distances[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j])

# Constraints
# Each city must be entered and left only once
for i in range(n):
    prob += lpSum([x[i][j] for j in range(n) if i != j]) == 1
    prob += lpSum([x[j][i] for j in range(n) if i != j]) == 1

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        prob += lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
visited = [0]
current = 0
while len(visited) < n:
    for j in range(n):
        if x[current][j].varValue == 1 and j not in visited:
            tour.append(j)
            visited.append(j)
            current = j
            break
tour.append(0)  # return to the depot

# Calculate the max distance and total cost
max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output
print("Tour:", [0] + tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)