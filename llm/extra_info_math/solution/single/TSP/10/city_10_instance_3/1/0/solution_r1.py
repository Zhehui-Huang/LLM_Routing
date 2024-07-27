import pulp
import math
import itertools

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Coordinates for the cities
coordinates = [
    (84, 67),  # Depot City 0
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

n = len(coordinates)
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat=pulp.LpBinary)

# Objective Function
prob += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leave city i exactly once
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # Enter city i exactly once

# Subtour elimination constraints
for s in range(2, n):  # Size of the subset
    for subset in itertools.combinations(range(1, n), s):  # Consider subsets that do not include depot
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j and i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
steps = 0
while steps < n:
    next_city = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if next_city:
        tour.append(current)
        current = next_city[0]
        steps += 1
    else:
        break
tour.append(0)  # Completing the tour returning to the depot

# Calculate total travel cost
total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")