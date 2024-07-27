import math
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, lpSum, value
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

# Calculate Euclidean distances
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)
d = LpVariable("maximum_distance", lowBound=0)

# Objective function
prob += d

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1  # exactly one outgoing arc from each city
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1  # exactly one incoming arc to each city

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= d

# Subtour elimination
for k in range(3, n+1):
    for S in combinations(range(1, n), k):  # city 0 must be in the tour, and we start from 1 to avoid subtours involving the depot
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract tour
tour = [0]
current_city = 0
for _ in range(n - 1):
    next_city = [j for j in range(n) if j != current_city and value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    current_city = next_city
tour.append(0)  # return to the depot

# Calculate maximum distance and total cost
max_dist = 0
total_cost = 0
for i in range(len(tour) - 1):
    dist = distance(tour[i], tour[i + 1])
    total_cost += dist
    if dist > max_dist:
        max_dist = dist

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")