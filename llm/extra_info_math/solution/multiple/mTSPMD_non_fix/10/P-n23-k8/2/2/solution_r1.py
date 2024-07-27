import pulp
import math

# Coordinates of depots and cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Number of robots
num_robots = 8
depot = 0

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
# Exactly one exit from each non-depot city
for j in range(1, n):
    problem += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1

# Exactly one entry to each non-depot city
for i in range(1, n):
    problem += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1

# Number of robots who start the tour
problem += pulp.lpSum(x[depot][j] for j in range(n) if j != depot) == num_robots

# Number of robots who end the tour
problem += pulp.lpSum(x[i][depot] for i in range(n) if i != depot) == num_robots

# Avoid subtours by creating a dummy constraint for each combination of cities
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += pulp.lpSum(x[i][k] * n + x[k][j] - x[i][j] for k in range(1, n) if k != i and k != j) >= 0

# Solve problem
problem.solve()

# Extract tour information
tours = {i: [depot] for i in range(num_robots)}
current_nodes = [depot] * num_robots
finished = [False] * num_robots

while not all(finished):
    for r in range(num_robots):
        if not finished[r]:
            next_node = -1
            for j in range(n):
                if j != current_nodes[r] and pulp.value(x[current_nodes[r]][j]) == 1:
                    tours[r].append(j)
                    current_nodes[r] = j
                    if j == depot:
                        finished[r] = True
                    break

# Calculate and print the results
overall_cost = 0
for r in range(num_robots):
    tour_cost = sum(distances[tours[r][i]][tours[r][i + 1]] for i in range(len(tours[r]) - 1))
    overall_cost += tour_cost
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")