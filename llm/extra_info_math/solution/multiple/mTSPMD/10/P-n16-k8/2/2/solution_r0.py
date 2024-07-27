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

# Distance matrix
n = len(coordinates)
cost = [[calc_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem definition
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision Variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat="Binary") 
     for i in range(n) for j in range(n) if i != j for k in depots}

# Objective Function
problem += pulp.lpSum(cost[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in depots), "Total Cost"

# Constraints
for j in range(8, n):
    problem += sum(x[i, j, k] for k in depots for i in range(n) if i != j) == 1, f"Visit_{j}"

for k in depots:
    problem += sum(x[k, j, k] for j in range(n) if j != k) == 1, f"Leave_{k}"
    problem += sum(x[j, k, k] for j in range(n) if j != k) == 1, f"Return_{k}"
    for i in range(n):
        if i != k:
            problem += sum(x[i, j, k] for j in range(n) if j != i) == sum(x[j, i, k] for j in range(n) if j != i), f"Continuity_{i}_{k}"

# Solve the problem
problem.solve()

# Output tours and costs
total_cost = 0
tours = [[] for _ in range(num_robots)]

for k in depots:
    current_node = k
    start_node = k
    tours[k].append(start_node)
    while True:
        next_node_found = False
        for j in range(n):
            if j != current_node and pulp.value(x[current_node, j, k]) == 1:
                tours[k].append(j)
                current_node = j
                next_node_found = True
                break
        if not next_node_it and current_node == start_node:
            break

for index, tour in enumerate(tours):
    tour_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")