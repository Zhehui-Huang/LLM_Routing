import math
from itertools import combinations
from pulp import LpProblem, lpSum, LpVariable, LpBinary, LpMinimize, PULP_CBC_CMD

# Coordinates of cities
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

# Total number of cities
n = len(cities)

# Problem definition
prob = LpProblem("TSP_Min_Max_Distance", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], 0, 1, LpBinary)
d_max = LpVariable("d_max", lowBound=0)

# Objective function
prob += d_max

# Adding constraints
for i in cities:
    prob += lpSum(x[i, j] for j in cities if i != j and j in cities) == 1
    prob += lpSum(x[j, i] for j in cities if j != i and j in cities) == 1

# Maximum distance constraint
for i in cities:
    for j in cities:
        if i != j:
            prob += x[i, j] * dist(i, j) <= d_max

# Subtour elimination constraints
for m in range(3, n + 1):
    for S in combinations(cities, m):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
solver = PULC_CBC_CMD(msg=False)
prob.solve(solver)

# Extracting tour from solution
tour = []
visited = set()
current = 0
while True:
    tour.append(current)
    visited.add(current)
    possibilities = [j for j in cities if j != current and x[current, j].value() == 1]
    if not possibilities:
        break
    current = possibilities[0]

# Calculate tour details
tour.append(tour[0])
max_distance_tour = max(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
total_cost_tour = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost_tour)
print("Maximum distance between consecutive cities:", max_distance_tour)