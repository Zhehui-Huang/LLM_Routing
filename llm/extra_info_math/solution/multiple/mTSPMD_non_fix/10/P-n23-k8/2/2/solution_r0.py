import pulp
import math
from itertools import product

# Coordinates of depots and cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Calculate Euclidean distance between any two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize LP problem
problem = pulp.LpProblem("Open_mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
problem += pulp.lpSum([distances[i][j] * x[i, j] for i in range(n) for j in range(n)])

# Constraints

# Every city being arrived at exactly once
for j in range(1, n):
    problem += pulp.lpSum([x[i, j] for i in range(n) if i != j]) == 1

# Start at the main depot and distribute robots
problem += pulp.lpSum([x[0, j] for j in range(1, n)]) == num_robots

# Every city must be departed exactly once (no need to return to the start depot)
for i in range(1, n):
    problem += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1

# Subtour elimination via sequential node visiting constraints
u = pulp.LpVariable.dicts('u', range(1, n), lowBound=0, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve problem
problem.solve()

# Extract tour information
tours = {}
for r in range(num_robots):
    tours[r] = []

current_location = [0]*num_robots
visited = set([0])
while len(visited) < n:
    for r in range(num_robots):
        for j in range(n):
            if j not in visited and pulp.value(x[current_location[r], j]) == 1:
                tours[r].append(j)
                current_location[r] = j
                visited.add(j)
                break

# Output results
total_cost = sum(distances[i][j] * pulp.value(x[i, j]) for i in range(n) for j in range(n))
for r in range(num_robots):
    print(f"Robot {r} Tour: {tours[r]}")
    robot_cost = sum(distances[tours[r][k]][tours[r][k + 1]] for k in range(len(tours[r]) - 1))
    print(f"Robot {r} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_cost}")