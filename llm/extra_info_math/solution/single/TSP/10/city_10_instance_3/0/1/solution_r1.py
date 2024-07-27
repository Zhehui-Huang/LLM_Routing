import math
import pulp
import itertools

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

# Create cost dictionary
cost = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the decision variables
x = pulp.LpVariable.dicts("x", cost.keys(), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([cost[i, j] * x[i, j] for i, j in cost.keys()]), "Total Travel Cost"

# Constraints for entering and leaving each city
for j in range(n):
    prob += pulp.lpSum([x[i, j] for i in range(n) if i != j]) == 1, f"Enter_{j}"
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1, f"Leave_{i}"

# Subtour elimination constraints using SECs
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):  # Exclude the depot (0) in subtour constraints
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve problem
status = prob.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Generate tour list
tour = []
current = 0
visited = [False]*n
count = 0

# Extract tour visiting order
while count < n:
    visited[current] = True
    tour.append(current)
    next_city = None
    for i in range(n):
        if i != current and not visited[i] and pulp.value(x[current, i]) == 1:
            next_city = i
            break
    count += 1
    if next_city is None:
        break
    current = next_city

tour.append(0)  # Return to depot

# Calculate total travel distance
total_distance = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")