import pulp
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Given city coordinates (index 0 and 1 are depot cities for robot 0 and robot 1 respectively)
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(city_coords)  # Number of total cities including depots

# Create the cost matrix
cost_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        cost_matrix[i][j] = euclidean_distance(*city_coords[i], *city.addr[j])

# Optimization problem
problem = pulp.LpProblem("VRP_with_Multiple_Depots", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')

# Objective Function
problem += pulp.lpSum(cost_matrix[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(2))

# Constraints
for k in range(2):  # Departure from depots
    problem += pulp.lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1

for k in range(2):  # Arrival to depots
    problem += pulp.lpSum(x[(i, k, k)] for i in range(n) if i != k) == 1

for j in range(2, n):  # Each node visited exactly once
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(2)) == 1

for j in range(n):  # Route continuity
    for k in range(2):
        problem += (
            pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) ==
            pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j))

# Solve the problem
problem.solve()

# Extract tours and calculate travel costs
tours = [[], []]
costs = [0, 0]

for k in range(2):
    node = k
    while True:
        for j in range(n):
            if pulp.value(x[(node, j, k)]) == 1:
                tours[k].append(node)
                costs[k] += cost_matrix[node][j]
                node = j
                break
        if node == k:
            tours[k].append(k)  # Complete the tour by returning to the depot
            break

# Output results
for k in range(2):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print("Overall Total Travel Cost:", sum(costs))