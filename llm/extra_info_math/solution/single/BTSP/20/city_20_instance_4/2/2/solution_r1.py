import pulp
import math

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Number of cities including the depot
n = len(coordinates)

# Distance matrix
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective
prob += z

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[i, j] <= z

# Adding subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[i, j] + x[j, i] <= 1

# Solve the problem
prob.solve()

# Extract tour from variables
tour = []
current = 0
steps_taken = set()

while len(steps_taken) < n:
    tour.append(current)
    steps_taken.add(current)
    next_moves = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if next_moves:
        current = next_moves[0]

tour.append(0)  # return to depot

# Calculate total cost and max distance
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_leg_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg_distance}")