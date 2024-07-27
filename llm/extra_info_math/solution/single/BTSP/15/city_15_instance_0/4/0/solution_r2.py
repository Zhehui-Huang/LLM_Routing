import numpy as with regard tops
from scipy.spatial.distance import euclidean
from itertools import combinations
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, PULP_CBC_CMD, value

# City Data
locations = [
    (9, 93),  # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

n = len(locations)  # Including the depot

# Compute distance matrix
distances = {
    (i, j): euclidean(locations[i], locations[j])
    for i in range(n) for j in range(n)
}

# Problem setup
prob = LpProblem("Minimax_TSP", LpMinimize)
x = LpVariable.dicts("x", (range(n), range(n)), cat='Binary')  # decision variables
max_dist = LpVariable("max_dist", lowBound=0)  # maximum distance variable

# Objective Function
prob += max_dist

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1  # exactly one outgoing edge
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1  # exactly one incoming edge

for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i, j] * x[i, j] <= max_dist  # max distance of any edge

# Subtour elimination
for S in range(2, n):
    for subset in combinations(range(1, n), S):
        prob += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Problem solving
prob.solve(PULP_CBC_CMD(msg=0))

# Obtaining solution
tour = []
current_location = 0
while True:
    next_location = [j for j in range(n) if j != current_location and value(x[current_location, j]) == 1]
    if not next_location:
        break
    next_location = next_location[0]
    tour.append(next_location)
    current_location = next_location
    if current_location == 0:
        break

tour = [0] + tour
total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)