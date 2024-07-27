import math
import pulp

# City coordinates
coordinates = [
    (84, 67), # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Number of cities
n = len(coordinates)

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cost dictionary
cost = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", cost.keys(), cat=pulp.LpBinary)

# Objective
prob += pulp.lpSum([cost[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j]), "Total Travel Cost"

# Constraints
# Each city is arrived at from exactly one other
for j in range(n):
    prob += pulp.lpSum([x[i, j] for i in range(n) if i != j]) == 1

# Each city is left by exactly one other
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1

# Subtour elimination constraints (SECs)
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum([x[i, j] for i in S for j in S if i != j]) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current = 0
while len(tour) < n:
    tour.append(current)
    # Find next city having x[current,next] == 1
    nexts = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if not nexts:
        break
    current = nexts[0]

# Complete the tour (return to depot)
tour.append(0)

# Calculate total cost
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")