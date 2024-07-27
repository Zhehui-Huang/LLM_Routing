import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Given data
coordinates = [
    (84, 67),  # Depot
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

groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Calculate Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the problem
model = LpProblem("VRP", LpMinimize)

# Define variables
x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(n)] for i in range(n)]
u = [LpVariable(f"u_{i}", lowBound=0) for i in range(1, len(groups) + 1)]

# Objective function
model += lpSum(distances[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each select one city from each group and ensure it is visited
for group in groups:
    model += lpSum(x[i][j] for i in group for j in range(n) if j not in group) == 1  # outgoing
    model += lpSum(x[i][j] for j in group for i in range(n) if i not in group) == 1  # incoming

# Flow conservation
for i in range(n):
    model += lpSum(x[j][i] for j in range(n) if j != i) == lpSum(x[i][j] for j in range(n) if i != j)

# Subtour elimination
k = len(groups)
for p in range(1, k):
    for q in range(1, k):
        if p != q:
            model += u[p] - u[q] + k * lpSum(x[i][j] for i in groups[p] for j in groups[q]) \
                     + (k - 2) * lpSum(x[i][j] for i in groups[q] for j in groups[p]) <= k - 1

# Solve the model
model.solve()

# Extract the solution
tour = []
visited = [0]  # start at depot
while len(visited) < len(groups) + 1:
    for j in range(n):
        if x[visited[-1]][j].value() == 1:
            tour.append(j)
            visited.append(j)
            break
tour.append(0)  # return to depot

total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)