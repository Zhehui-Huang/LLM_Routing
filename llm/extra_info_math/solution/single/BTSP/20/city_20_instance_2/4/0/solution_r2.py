import pulp
import math
from itertools import combinations, product

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

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(cities)
distance_matrix = {
    (i, j): euclidean_distance(cities[i], cities[j])
    for i, j in product(range(n), range(n)) if i != j
}

problem = pulp.LpProblem("Minimize_Maximum_Distance", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j) for i, j in product(range(n), range(n)) if i != j), cat='Binary')
max_dist = pulp.LpVariable("max_dist", lowBound=0)

problem += max_dist

for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Maximum distance constraint
for i, j in product(range(n), range(n)):
    if i != j:
        problem += x[i, j] * distance_matrix[i, j] <= max_dist

# Subtour Elimination (SEC)
for s in range(2, n):
    for S in combinations(range(1, n), s):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

status = problem.solve(pulp.PULP_CBC_CMD(msg=True))

if status == pulp.LpStatusOptimal:
    # Extract solution
    tour = []
    current = 0
    visited = set()
    visited.add(current)
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[current, j]) == 1]
        if next_cities:
            next_city = next_cities[0]
            tour.append(current)
            if next_city in visited:
                break
            visited.add(next_city)
            current = next_city
        else:
            break
    tour.append(0)

    # Calculate metrics
    total_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("Failed to find an optimal solution.")