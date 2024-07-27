from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, PULP_CBC_CMD
import math

# Coordinates of the cities
coordinates = [
    (3, 26),   # Depot City 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Grouping of cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Calculate Euclidean distance between two cities
def calculate_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Prepare the optimization model
model = LpProblem("TSP", LpMinimize)

# Create variables: x[i][j] = 1 if the path is traveled from city i to j
n = len(coordinates)
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=LpBinary)

# Objective function: Minimize the sum of travel costs
model += lpSum(x[i, j] * calculate_distance(i, j) for i in range(n) for j in range(n))

# Each group must have one node connected to the tour
for group in groups:
    model += lpSum(x[i, j] for i in group for j in range(n) if j not in group) == 1
    model += lpSum(x[j, i] for i in group for j in range(n) if j not in group) == 1

# Flow conservation constraints
for k in range(1, n):
    model += lpSum(x[i, k] for i in range(n) if i != k) == lpSum(x[k, j] for j in range(n) if j != k)

# Solve the model
model.solve(PULV_CBC_CMD(msg=1))

# Extract the tour
tour = [0]
visited = set()
current = 0
while True:
    next_city = None
    for j in range(n):
        if x[current, j].varValue == 1 and j not in visited:
            next_city = j
            break
    if next_city is None or next_city == 0:
        break
    tour.append(next_city)
    visited.add(next_city)
    current = next_city
tour.append(0)  # return to the depot

# Calculate the total cost of the tour
total_cost = sum(calculate_distancnce(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output formatted results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")