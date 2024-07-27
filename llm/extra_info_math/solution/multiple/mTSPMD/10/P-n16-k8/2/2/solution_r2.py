import pulp
import math

# Data Initialization
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64),  
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
depots = list(range(8))  # Depots are the first 8 indices
num_robots = 8

# Function to calculate Euclidean distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Define distance matrix
n = len(coordinates)
cost = [[calc_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat=pulp.LpBinary) 
     for i in range(n) for j in range(n) if i != j for k in depots}

# Objective function to minimize the total travel cost
problem += pulp.lpSum(cost[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in depots)

# Constraints
# Each robot must leave its depot and return to its depot
for k in depots:
    problem += pulp.lpSum(x[k, j, k] for j in range(n) if j != k) == 1
    problem += pulp.lpSum(x[j, k, k] for j in range(n) if j != k) == 1

# Each other city visited exactly once
for j in range(n):
    if j not in depots:
        problem += pulp.lpSum(x[i, j, k] for k in depots for i in range(n) if i != j) == 1

# Continuity within a route for each robot
for k in depots:
    for i in range(n):
        if i != k:
            problem += (pulp.lpSum(x[i, j, k] for j in range(n) if j != i) - 
                        pulp.lpSum(x[j, i, k] for j in range(n) if j != i) == 0)

# Solve the problem
problem.solve()

# Gather results
tours = {k: [] for k in depots}
total_cost = 0

for k in depots:
    current_location = k
    tour_cost = 0
    while True:
        tours[k].append(current_location)
        next_step_found = False
        for j in range(n):
            if j != current_location and pulp.value(x[current_location, j, k]) == 1:
                tour_cost += cost[current_location][j]
                current_location = j
                next_step_found = True
                break
        if not next_step_found or current_location == k:
            if current_location != k:  # Ensure we close the tour if not already at the depot
                tours[k].append(k)
                tour_cost += cost[current_location][k]
            break

    total_cost += tour_cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")