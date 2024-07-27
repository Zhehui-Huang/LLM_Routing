import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

# Coordinates of cities, including the depot
coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

n = len(coords)  # Number of cities including the depot

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Construct distance matrix
dist_matrix = [[distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Define the model
model = LpProblem("TSP Model", LpMinimize)

# Variables: decision variable x[i][j] is 1 if the path from i to j is taken
x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(n)] for i in range(n)]

# Add objective to minimize the maximum distance between consecutive cities on the tour
max_distance = LpVariable("max_distance", lowBound=0)
model += max_distance

# Constraints
# 1. Ensure exactly one outgoing and one incoming connection for each city
for i in range(n):
    model += lpSum(x[i][j] for j in range(n) if i != j) == 1  # exactly one outgoing edge
    model += lpSum(x[j][i] for j in range(n) if i != j) == 1  # exactly one incoming edge

# 2. Maximum distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += max_distance >= dist_matrix[i][j] * x[i][j]

# Subtour elimination constraints (using Miller-Tucker-Zemlin formulation or equivalent)
u = [LpVariable(f"u_{i}", lowBound=0) for i in range(n)]  # Position variables for subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the model
status = model.solve(PULP_CBC_CMD(msg=False))

# Extract solution if optimal
if status == 1:
    tour = []
    current_city = 0
    added_cities = set([0])
    remaining_cities = set(range(n)) - added_cities

    while len(added_cities) < n:
        for next_city in range(n):
            if x[current_city][next_city].varValue == 1:
                tour.append(next_city)
                added_cities.add(next_city)
                current_city = next_city
                break

    # Add the return path to depot
    tour.append(0)

    # Calculate total travel cost
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    # Calculate the maximum distance between consecutive cities
    max_consecutive_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")
else:
    print("The problem could not be solved to optimality.")