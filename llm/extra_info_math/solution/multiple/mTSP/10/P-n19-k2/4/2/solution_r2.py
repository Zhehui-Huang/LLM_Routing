import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary

# Constants and Coordinates
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
               (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
m = 2  # Number of robots
n = len(coordinates)  # Total number of cities including the depot

# Helper function for distances
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem Setup
model = LpProblem("Multiple_TSP", LpMinimize)
x = LpVariable.dicts("x", [(k, i, j) for k in range(m) for i in range(n) for j in range(n) if i != j], cat=LpBinary)
u = LpVariable.dicts("u", (i for i in range(1, n)), lowBound=1, cat='Continuous')

# Objective function
model += lpSum(distance_matrix[i][j] * x[k, i, j] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints
for k in range(m):
    for j in range(1, n):
        model += lpSum(x[k, i, j] for i in range(n) if i != j) == lpSum(x[k, j, i] for i in range(n) if i != j)
    model += lpSum(x[k, 0, j] for j in range(1, n)) == 1
    model += lpSum(x[k, i, 0] for i in range(1, n)) == 1

for j in range(1, n):
    model += lpSum(x[k, i, j] for k in range(m) for i in range(n) if i != j) == 1

for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i] - u[j] + n * x[k, i, j] <= n - 1

# Solve the model
model.solve()

# Output the results
for k in range(m):
    print(f"Robot {k+1} Tour:")
    path = []
    for i in range(n):
        for j in range(n):
            if x[k, i, j].value() == 1:
                path.append((i, j))
    # Rearranging from the depot
    sorted_path = [0]
    next_node = 0
    while len(path) > 1:
        for i in range(len(path)):
            if path[i][0] == next_node:
                next_node = path[i][1]
                sorted_path.append(next_node)
                path.pop(i)
                break
    sorted_path.append(0)  # complete the tour back to the depot
    print(sorted_path)
    print("Tour Cost:", sum(distance_matrix[sorted_path[i]][sorted_path[i+1]] for i in range(len(sorted_path)-1)))