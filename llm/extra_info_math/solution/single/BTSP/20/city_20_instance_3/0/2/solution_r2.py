import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary, value, PULP_CBC_CMD
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

n = len(cities)

# Euclidean distance function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Setting up the problem
prob = LpProblem("Minimax_TSP", LpMinimize)
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d = LpVariable("d", lowBound=0)
prob += d

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * distance(i, j) <= d

# Subtour elimination
for m in range(2, n):
    for S in combinations(range(1, n), m):
        prob += lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Problem solving
solver = PULP_CBC_CMD(msg=False)
prob.solve(solver)

# Extracting the solution
tour = [0]
for _ in range(n - 1):
    next_cities = [j for j in range(n) if value(x[(tour[-1], j)]) > 0.9]
    if not next_cities:
        # if no next city, break the loop to prevent infinite loops
        break
    tour.append(next_cities[0])
tour.append(0)  # Return to depot

# Calculation of the cost and max distance
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")