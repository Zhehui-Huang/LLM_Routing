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

# Number of cities including depots
n = len(city_coords)

# Create the cost matrix
cost_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i][j] = euclidean_distance(*city_coords[i], *city_coords[j])
        else:
            cost_matrix[i][j] = float('inf')  # No loops

# Optimization problem
problem = pulp.LpProblem("VRP_with_Multiple_Depots", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')

# Objective Function
problem += pulp.lpSum(cost_matrix[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(2))

# Constraints
# Departures from depots
for k in range(2):
    problem += pulp.lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1

# Arrivals to depots
for k in range(2):
    problem += pulp.lpSum(x[(i, k, k)] for i in range(n) if i != k) == 1

# Each node is visited exactly once by any robot
for j in range(2, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(2)) == 1

# Ensuring route continuity
for j in range(n):
    for k in range(2):
        if j != k:  # Exclude depot itself
            problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j)

# Sub-tour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(2):
                problem += u[i] - u[j] + n * x[(i, j, k)] <= n - 1

# Solve the problem
problem.solve()

# Collect the results
tours = [[], []]
for k in range(2):
    # Start from the depot
    next_visit = k
    while True:
    found_next_visit = False
    for j in range(n):
        if pulp.value(x[(next_visit, j, k)]) == 1:
        tours[k].append(next_visit)
        next_visit = j
        found_next_visit = True
        break
    if not found_next_visit or next_visit == k:
        tours[k].append(next_visit)
        break

# Calculate travel costs for each robot
costs = [0, 0]
for k in range(2):
    for i in range(len(tours[k]) - 1):
        costs[k] += cost_matrix[tours[k][i]][tours[k][i + 1]]

# Outputs
print("Robot 0 Tour:", tours[0])
print("Robot 0 Total Travel Cost:", costs[0])

print("Robot 1 Tour:", tours[1])
print("Robot 1 Total Travel Cost:", costs[1])

print("Overall Total Travel Cost:", sum(costs))