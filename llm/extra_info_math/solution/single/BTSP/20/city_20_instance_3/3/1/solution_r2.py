import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary

# Coordinates of the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate distances
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities)
distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Problem
prob = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i,j) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)
z = LpVariable("max_distance", lowBound=0, cat="Continuous")

# Objective
prob += z

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Max distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * distances[i][j] <= z

# Subtour elimination
from itertools import combinations
for s in range(3, n):
    for subset in combinations(range(1, n), s): # 1 to ignore the depot for subtours
        prob += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the route
path = []
current = 0
for _ in range(n):
    next_move = [(current, j) for j in range(n) if j != current and x[(current, j)].varValue == 1]
    if next_move:
        current = next_move[0][1]
        path.append(current)

# Calculate total travel cost and max distance
path = [0] + path + [0]
total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
max_distance = max(distances[path[i]][path[i+1]] for i in range(len(path) - 1))

print("Tour:", path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)