import math
from itertools import combinations
from pulp import LpProblem, lpSum, LpVariable, LpBinary, LpMinimize, PULP_CBC_CMD

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76),
    17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distance
def dist(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Total number of cities including the depot
n = len(cities)

# Create the problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat=LpBinary)
d_max = LpVariable("d_max")

# Objective function: Minimize the maximum distance in the tour
prob += d_max

# Constraints:
# Every city must be entered and left exactly once
for i in cities:
    prob += lpSum(x[(i, j)] for j in cities if i != j) == 1, f"Enter_{i}"
    prob += lpSum(x[(j, i)] for j in cities if i != j) == 1, f"Leave_{i}"

# Maximum distance variable constraint
for i in cities:
    for j in cities:
        if i != j:
            prob += x[(i, j)] * dist(i, j) <= d_max

# Sub-tour elimination constraints
subsets = range(2, n)  # Excluding full set and single-node subsets for efficiency
for s in subsets:
    for S in combinations(cities, s):
        prob += lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = prob.solve(PULP_CBC_CMD(msg=0))

# Extract the solution
tour = []
if status == 1:  # Check if the problem is solved optimally
    current = 0
    while True:
        next_city = [j for j in cities if j != current and x[(current, j)].varValue > 0.5]
        if not next_city:
            break
        next_city = next_city[0]
        tour.append(next_city)
        current = next_city
        if current == 0:
            break

# Append depot to complete circuit
tour = [0] + tour

# Calculate cost details
total_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)