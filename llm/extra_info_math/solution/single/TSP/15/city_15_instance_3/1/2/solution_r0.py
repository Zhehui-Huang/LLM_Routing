import pulp
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates: city index mapped to (x, y)
coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),  # although same coordinates with city 5 given, treat separately
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

n = len(coordinates)
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective
prob += pulp.lpSum(cost[i, j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += (pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1)  # leave i exactly once
    prob += (pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1)  # enter i exactly once

# Subtour elimination
for i in range(2, n):
    for S in itertools.combinations(range(1, n), i):
        prob += (pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

# Solve the problem
prob.solve()

# Extract tour
tour = []
visited = 0
while True:
    for i in range(n):
        if x[visited, i].varValue == 1:
            tour.append(visited)
            visited = i
            break
    if visited == 0:
        break

# Adding the depot return
tour.append(0) 

# Calculate the total travel cost
total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")