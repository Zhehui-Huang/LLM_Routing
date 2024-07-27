import pulp
import math

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities including the depot
n = len(coordinates)

# Distance matrix
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Define the problem
prob = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)
prob += z

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[i, j] <= z

# Subtour Elimination Constraint
for k in range(2, n+1):
    subsets = itertools.combinations(range(1, n), k)
    for subset in subsets:
        indices_in_subset = list(subset) + [0]
        for i in indices_in_subset:
            prob += pulp.lpSum(x[j, i] for j in indices_in_singleton if i != j) <= len(indices_in_subset) - 1

# Solve the problem
prob.solve()

# Extract the tour from the solution
tour = [0]
for _ in range(n - 1):
    next_cities = [j for j in range(n) if j != tour[-1] and pulp.value(x[tour[-1], j]) == 1]
    if next_cities:
        tour.append(next_cities[0])

tour.append(0)  # Return to the depot

# Calculate total cost and max distance
total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_leg_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_leg_distance}")