import pulp
import math

# Coordinates of the cities including the depot
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

n = len(coordinates)

# Set up the problem: Minimize total distance
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] = 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: minimize the total traveled distance
prob += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city is arrived at from exactly one other city
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Each city is departed to exactly one other city
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour elimination
for size in range(2, n):
    for subset in itertools.combinations(range(1, n), size):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
visited = [0]
current = 0
while len(visited) < n:
    for j in range(n):
        if j != current and pulp.value(x[current, j]) == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break

# Adding the return to depot city
tour.append(0)

# Calculate total distance of the tour
total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")