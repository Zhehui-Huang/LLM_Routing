import pulp
from math import sqrt
import itertools

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

def distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

n = len(cities)

# Create the problem variable:
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Create variables:
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, pulp.LpBinary)
d = pulp.LpVariable("d", lowBound=0, cat='Continuous')

# Objective function:
prob += d, "Minimized Maximum Distance Between Any Two Consecutive Cities"

# Constraints:
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Sum of X(i,j) from city {i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Sum of X(j,i) to city {i}"

# Subtour elimination constraints (SECs):
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Distance constraints for the objective:
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distance(i, j) * x[i, j] <= d

# Solve the problem:
prob.solve()

# Output solution:
tour = []
current = 0
while True:
    next_city = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if next_city == [0]:
        tour.append(0)
        break
    else:
        tour.append(next_city[0])
        current = next_city[0]

total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)