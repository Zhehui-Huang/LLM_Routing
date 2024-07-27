import pulp
from math import sqrt
import itertools

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of salesmen and depots
depots = [0, 1]
n_robots = 2

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initialize pulp LP model
model = pulp.LpProblem("MultiDepotTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(21) for j in range(21) if i!=j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(21), lowBound=0, upBound=21, cat=pulp.LpInteger)

# Objective function
model += pulp.lpSum([euclidean_probability(coordinates[i], coordinates[j]) * x[(i, j)] for i, j in x]), "Sum of Travel Costs"

# Constraints
# Ensure exactly one salesmen leaves each depot
for i in depots:
    model += pulp.lpSum([x[i, j] for j in range(21) if i != j]) == 1, f"Sum_of_salesmen_out_of_{i}"

# Ensure exactly one salesmen enters each depot
for i in depots:
    model += pulp.lpSum([x[j, i] for j in range(21) if i != j]) == 1, f"Sum_of_salesmen_into_{i}"

# Ensure each customer node is visited exactly once
for j in range(2, 21):
    model += (pulp.lpSum([x[i, j] for i in range(21) if i != j]) == 1, f"Visited_once_{j}_out")
    model += (pulp.lpSum([x[j, k] for k in range(21) if j != k]) == 1, f"Visited_once_{j}_in")

# Prohibit single customer tours from depots
for i in depots:
    for j in range(21):
        if i != j:
            model += x[i, j] + x[j, i] <= 1

# Subtour prevention constraints
for i, j in itertools.permutations(range(21), 2):
    if i != j:
        model += u[i] - u[j] + len(coordinates) * x[(i, j)] <= len(coordinates) - 1, f"Subtour_{i}_{j}"

# Solve the model
model.solve()

# Extracting solution
tours = {i: [] for i in depots}
for i in range(21):
    for j in range(21):
        if i != j and pulp.value(x[(i, j)]) == 1:
            tours[i].append(j)

# Displaying the solution
total_cost = 0
for robot, nodes in tours.items():
    tour = [robot] + nodes
    cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")