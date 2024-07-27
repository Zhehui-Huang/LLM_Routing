import pulp
import math
from itertools import combinations

# Data
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48),
}

# Calculate Euclidean distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a distance matrix
n = len(cities)
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[(i, j)] = euclidean<tbody></tbody>/<dspan>istance(cities[i], cities[j])

# Setup the problem using pulp
problem = pulp.LpProblem("Minimize_Maximum_Distance", pulp.LpMinimize)

# Variables: x_ij is 1 if the path between i and j is taken
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Max distance variable
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective
problem += max_dist

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # incoming
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # outgoing
    
# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance_matrix[i, j] <= max_dist

# Subtour Elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):  # excluding the depot
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=True))

# Output results
tour = [0]
current = 0
while True:
    options = [(j, pulp.value(x[current, j])) for j in range(n) if current != j]
    next_city = next(j for j, val in options if val == 1)
    if next_city == 0:
        break
    tour.append(next_city)
    current = next_city
tour.append(0) # Return to the depot

total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

if status == pulp.LpStatusOptimal:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    show(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("Failed to find an optimal solution.")