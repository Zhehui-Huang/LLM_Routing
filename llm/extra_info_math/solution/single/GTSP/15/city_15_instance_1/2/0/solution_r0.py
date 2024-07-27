import math
from itertools import product
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Define cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Grouping of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Compute Euclidean distances between all pairs
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Cost matrix for edges
costs = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Problem setup
prob = LpProblem("TSP_variant_min_cost_path", LpMinimize)

# Variables
x = LpVariable.dicts("edge", ((i, j) for i in cities for j in cities if i != j), cat=LpBinary)

# Objective Function
prob += lpSum(x[(i, j)] * costs[(i, j)] for i in cities for j in cities if i != j), "Total_Travel_Cost"

# Constraints
# Each group must have exactly one exit and one enter
for g in groups.values():
    prob += lpSum(x[(i, j)] for i in g for j in cities if i != j) == 1, f"One_outgoing_from_group_{g}"
    prob += lpSum(x[(j, i)] for i in g for j in cities if i != j) == 1, f"One_incoming_to_group_{g}"

# Entrances to and exits from depot city
prob += lpSum(x[(0, j)] for j in cities if j != 0) == len(groups), "Exiting_depot"
prob += lpSum(x[(j, 0)] for j in cities if j != 0) == len(groups), "Entering_depot"

# Flow conservation constraint for each city not in depot
for c in cities:
    if c != 0:
        prob += (lpSum(x[(j, c)] for j in cities if j != c) ==
                 lpSum(x[(c, j)] for j in cities if j != c)), f"Flow_conservation_{c}"

# Solve the problem
prob.solve()

# Collect results
tour = [0]
current = 0
while True:
    next_city = [j for j in cities if j != current and x[(current, j)].varValue == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

# Calculate the total cost of the tour
total_cost = sum(costs[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)