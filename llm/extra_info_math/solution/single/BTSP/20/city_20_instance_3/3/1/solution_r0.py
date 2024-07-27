import math
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, lpSum, PULP_CBC_CMD

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between cities
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

n = len(cities)
dist = [[distance(i, j) for j in range(n)] for i in range(n)]

# Create the problem
problem = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = LpVariable("z", lowBound=0, cat='Continuous')

# Objective: minimize the maximum distance
problem += z

# Constraints
for i in range(n):
    problem += lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"outflow_{i}"
    problem += lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"inflow_{i}"

# Max distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[(i, j)] * dist[i][j] <= z, f"max_dist_{i}_{j}"

# Subtour elimination
from itertools import combinations
for s in range(2, n):
    for subset in combinations(range(1, n), s):  # 1 to ignore depot
        problem += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
solver = PULP_CBC_CMD(msg=False)
problem.solve(solver)

# Retrieve results
tour = []
visited = [0]
while len(visited) < n:
    for j in range(n):
        if x[(visited[-1], j)].value() == 1:
            visited.append(j)
            tour.append(j)
            break
tour.append(0)  # Return to depot

# Compute total cost and max distance
total_distance = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_dist = max(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_dist)