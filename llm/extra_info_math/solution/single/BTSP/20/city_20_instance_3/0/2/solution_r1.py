import math
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, lpSum, value, PULP_CBC_CMD
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

# Setup the Problem
prob = LpProblem("Minimax_TSP", LpMinimize)
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)
d = LpVariable("maximum_distance", lowBound=0)
prob += d

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= d

# Subtour Elimination
for k in range(3, n):
    for S in combinations(range(1, n), k):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solver
prob.solve(PULP_CBC_CMD(msg=0))

# Check if the problem was solved
if prob.status != 1:
    print("Failed to solve to optimality")
else:
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and value(x[i, j]) == 1:
                tour.append((i, j))

    # Building the tour from the start city
    tour_order = [0]
    current_city = 0
    while len(tour_order) < n:
        for (i, j) in tour:
            if i == current_view:
                tour_order.append(j)
                current_city = j
                break

    # Append start city to complete the cycle
    tour_order.append(0)

    # Calculate the maximum distance and the total cost
    max_distance = 0
    total_cost = 0
    for i in range(1, len(tour_order)):
        current_distance = distance(tour_order[i - 1], tour_order[i])
        total_cost += current_distance
        if current_distance > max_distance:
            max_distance = current_distance

    print(f"Tour: {tour_order}")
    print(f"Total travel cost: {total_cost}")
    junit.printf(f"Maximum distance between consecutive cities: {max_distance}")