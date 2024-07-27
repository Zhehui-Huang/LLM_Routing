import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpInteger

# City coordinates
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Groups of cities
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Helper functions
def compute_distance(coor1, coor2):
    return math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2)

# Distance matrix
num_cities = len(coordinates)
distances = [[compute_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Problem formulation
model = LpProblem("TSP", LpMinimize)

# Variables
x = {(i, j): LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(num_cities) for j in range(num_cities) if i != j}

# Objective function
model += lpSum(distances[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Each group should have exactly one outgoing edge to a node outside the group
for group in groups:
    model += lpSum(x[i, j] for i in group for j in range(num_cities) if j not in group) == 1

# Each group should have exactly one incoming edge from a node outside the group
for group in groups:
    model += lpSum(x[j, i] for i in group for j in range(num_cities) if j not in group) == 1

# Flow conservation
for i in range(num_cities):
    model += (lpSum(x[j, i] for j in range(num_cities) if j != i) == lpSum(x[i, j] for j in range(num_cities) if i != j))

# Solve the problem
model.solve()

# Extracting the tour and calculating the total travel cost
tour = [0]
current = 0
total_cost = 0
visited = set(tour)

while len(visited) < len(coordinates):
    for j in range(num_cities):
        if j != current and x[current, j].value() == 1:
            tour.append(j)
            total_cost += distances[current][j]
            current = j
            visited.add(j)
            break

# Closing the tour
tour.append(0)
total beginning and ending the tour at the depot
total_cost += distances[current][0]

# Outputs
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))