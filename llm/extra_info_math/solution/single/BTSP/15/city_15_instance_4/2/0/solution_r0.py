import pulp
import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Input data
positions = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
             (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
             (53, 80), (21, 21), (12, 39)]

n = len(positions)  # Number of cities

# Calculate distances
distances = {(i, j): euclidean_distance(positions[i], positions[j]) for i in range(n) for j in range(n)}

# Setup the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Integer')

# Objective
M = pulp.LpVariable("M", lowBound=0, cat='Continuous')
prob += M

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(1, n):
        if i != j:
            prob += M >= distances[i, j] * x[i, j]

# Subtour elimination: Miller-Tucker-Zemlin constraint
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

# Output results
tour = []
visited = [0]
current = 0

while True:
    next_city = [j for j in range(n) if pulp.value(x[current, j]) == 1][0]
    if next_city == 0:
        break
    visited.append(next_city)
    tour.append((current, next_city))
    current = next_city

visited.append(0)
tour.append((current, 0))

# Compute the tour cost and maximim segment distance
tour_cost = sum(distances[tour[i]] for i in range(len(tour)))
max_distance = max(distances[tour[i]] for i in range(len(tour)))

print("Tour:", visited)
print("Total travel cost:", round(tour_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))