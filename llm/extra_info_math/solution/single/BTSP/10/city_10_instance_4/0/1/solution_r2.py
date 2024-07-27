import math
from pulp import *

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
coords = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

n = len(coords)
distances = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Decision variables
prob = LpProblem("Minimax_TSP", LpMinimize)
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')
M = LpVariable("M", lowBound=0)

# Objective
prob += M

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distances[i][j] <= M

# Subtour constraint
for i in range(2, n):
    for subset in itertools.combinations(range(1, n), i):
        prob += lpSum(x[i][j] + x[j][i] for i, j in itertools.permutations(subset, 2)) <= len(subset) - 1

# Solve
prob.solve()

# Extract solution
tour = []
current = 0
steps = 0

while steps < n:
    tour.append(current)
    for next_city in range(n):
        if x[current][next_city].varValue == 1.0:
            current = next_city
            break
    steps += 1
tour.append(0)  # returning to the depot

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']}")
print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive__[i}]}")