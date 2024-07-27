import math
from pulp import LpProblem, LpMinimize, LpVariable, LpBinary, lpSum

# Define city coordinates including the depot
coordinates = [
    (9, 93),  # Depot city (index 0)
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Function to compute Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Initialize variables
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]
indexes = list(range(n))

# Create the problem
problem = LpProblem("TSP", LpMinimize)

# Variables: x[i][j] = 1 if the path is taken from i to j, 0 otherwise.
x = LpVariable.dicts("x", ((i, j) for i in indexes for j in indexes if i != j), cat=LpBinary)

# Auxiliary variable
z = LpVariable("z", lowBound=0)

# Objective: Minimize the maximum edge length in the path
problem += z, "Minimize the maximum length of any edge in the tour"

# Constraints

# Each city is left only once
for i in indexes:
    problem += lpSum(x[i, j] for j in indexes if i != j) == 1, f"leave_city_{i}"

# Each city is entered only once
for j in indexes:
    problem += lpSum(x[i, j] for i in indexes if i != j) == 1, f"enter_city_{j}"

# Subtour elimination
u = LpVariable.dicts("u", indexes[1:], lowBound=0, cat="Continuous")  # We don't create a u[0] to avoid a dummy variable issue
for i in indexes[1:]:
    for j in indexes[1:]:
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n - 2

# Limit z to be at least the length of each edge used in the solution
for i in indexes:
    for j in indexes:
        if i != j:
            problem += x[i, j] * distances[i][j] <= z, f"max_edge_{i}_{j}"

# Solve the problem
problem.solve()

# Retrieve the solution
tour = [0]
current = 0
for _ in indexes[:-1]:
    next_city = [j for j in indexes if j != current and x[current, j].value() == 1][0]
    tour.append(next_city)
    current = next_city

# Close the tour
tour.append(0)

# Calculate the maximal edge length in the tour
max_len = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Display outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_len)