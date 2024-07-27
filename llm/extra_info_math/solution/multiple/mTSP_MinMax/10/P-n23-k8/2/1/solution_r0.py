import pulp
import math

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Coordinates for each city, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

n = len(coordinates)
m = 8  # number of robots

# Calculate distances between all pairs of nodes
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create a problem instance
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables: x[i][j][k] is 1 if robot k travels from i to j
x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for k in range(m)] for j in range(n)] for i in range(n)]

# Continuous variable to eliminate sub-tours
u = [pulp.LpVariable(f"u_{i}", lowBound=0) for i in range(n)]

# Objective: Minimize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Constraints
for j in range(1, n):  # Ensure each city is visited exactly once
    prob += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):  # Flow conservation for each robot and each city
    for j in range(1, n):
        prob += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) - pulp.lpSum(x[j][i][k] for i in range(n) if i != j) == 0

for k in range(m):  # Each robot leaves from and returns to the depot
    prob += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

# Sub-tour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

# Distance constraints linked to the objective
for k in range(m):
    prob += pulp.lpSum(distances[i][j] * x[i][j][k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
prob.solve()

# Output the results
max_travel_cost = pulp.value(max_distance)
print(f"Maximum Travel Cost: {max_travel_cost}")

for k in range(m):
    tour = [0]
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                if j != 0:
                    tour.append(j)

    tour.append(0) # back to depot
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")