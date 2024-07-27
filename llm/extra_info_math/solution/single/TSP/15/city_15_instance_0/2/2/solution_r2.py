import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD

# Define city coordinates
coordinates = [
    (9, 93),    # Depot city 0
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

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Number of cities
n = len(coordinates)

# Cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem configuration
prob = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective: Minimize total travel cost
prob += lpSum(cost[i][j] * x[(i, j)] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Solve problem
prob.solve(PULP_CBC_CMD(msg=0))

# Extracting results
tour = []
for i in range(n):
    for j in range(n):
        if x[(i, j)].value() == 1:
            tour.append((i, j))

# Retrieve tour and calculate total travel cost
visited = set()
current_city = 0
final_tour = [current_city]
while len(visited) < n - 1:
    for next_city in range(n):
        if x[(current_city, next_city)].value() == 1 and next_city not in visited:
            final_tour.append(next_city)
            visited.add(next_city)
            current_city = next_city
            break

final_tour.append(0)  # Return to depot

# Calculate total cost
total_cost = sum(cost[final_tour[i]][final_tour[i + 1]] for i in range(len(final_tour) - 1))

# Printing results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")