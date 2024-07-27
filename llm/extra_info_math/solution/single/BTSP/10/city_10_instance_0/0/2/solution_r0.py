import pulp
import math

# City coordinates
coordinates = [
    (50, 42),  # Depot
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities
n = len(coordinates)

# Calculate distances between every pair of nodes
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Create the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables x_ij: 1 if travel from i to j, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Variable d (maximum distance of any arc in the solution)
d = pulp.LpVariable("d", lowBound=0, cat='Continuous')

# Objective: Minimize the maximum distance
problem += d

# Constraints:

# Exactly one outgoing arc from each node
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Exactly one incoming arc to each node
for j in range(n):
    problem += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Subtour elimination
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        problem += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[(i, j)] * x[(i, j)] <= d

# Solve the problem
status = problem.solve()

# Extract the tour
tour = [0]
current = 0
while True:
    next_city = [j for j in range(n) if j != current and pulp.value(x[(current, j)]) == 1][0]
    if next_city == 0:
        break
    tour.append(next_city)
    current = next_city
tour.append(0)  # returning to the depot

# Calculate tour cost and maximum distance between consecutive cities
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")