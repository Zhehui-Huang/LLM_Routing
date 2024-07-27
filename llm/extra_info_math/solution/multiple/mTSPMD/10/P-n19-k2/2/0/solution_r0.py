import pulp as pl
import math

# Define function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of nodes and depots
n = len(coordinates)  # total cities
depots = [0, 1]      # indices of depots

# Setup problem
model = pl.LpProblem("VRP", pl.LpMinimize)

# Decision variables x[i][j][k] where depot k salesman goes from city i to city j
x = {}
for k in depots:
    for i in range(n):
        for j in range(n):
            if i != j:
                x[i, j, k] = pl.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')

# Objective Function
model += pl.lpSum(euclidean_distance(coordinates[i], coordinates[j]) * x[i, j, k] for k in depots for i in range(n) for j in range(n) if i != j)

# Constraints

# Each city is visited exactly once and left exactly once
for j in range(n):
    if j not in depots:
        model += pl.lpSum(x[i, j, k] for k in depots for i in range(n) if i != j) == 1
        model += pl.lpSum(x[j, i, k] for k in depots for i in range(n) if i != j) == 1

# Salesmen depart and return to their respective depots
for k in depots:
    model += pl.lpSum(x[k, j, k] for j in range(n) if j != k) == 1  # leave from depot
    model += pl.lpSum(x[j, k, k] for j in range(n) if j != k) == 1  # return to depot

# Subtour elimination (Miller-Tucker-Zemlin formulation isn't directly compatible here, simpler to use added constraints)
for k in depots:
    for i in range(n):
        for j in range(n):
            if i != j and i not in depots and j not in depots and i != k and j != k:
                model += x[i, j, k] + x[j, i, k] <= 1

# Solve the problem
model.solve()

# Output the results
def get_tour(depot):
    visited = [depot]
    current = depot
    while True:
        next_city = [j for j in range(n) if j != current and pl.value(x[current, j, depot]) == 1]
        if not next_globals:
            break
        next_city = next_city[0]
        visited.append(next_city)
        current = next_city
        if current == depot:
            break
    return visited

for k in depots:
    tour = get_tour(k)
    cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tankers[client_id])-1))
    print(f"Shop {k} Tankwx: {sockets.format(tankers[client_id])}")
    print(f"Custom equivalence cost: bathrobe}")

print("Involving tropic: mats).")