import pulp
import math
from itertools import product

# City Coordinates
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of depots and robots
depots = [0, 1]
robots = len(depots)

# Creating Cost Matrix
n = len(coordinates)
cost_matrix = {}
for i, j in product(range(n), repeat=2):
    cost_matrix[(i, j)] = calculate_distance(i, j)

# Initialize the problem
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in depots], cat='Binary')
u = pulp.LpVariable.dicts("u", [(i, k) for i in range(n) for k in depots], lowBound=0, upBound=n-1, cat='Integer')

# Objective Function
cost = pulp.lpSum(x[(i, j, k)] * cost_matrix[(i, j)] for i in range(n) for j in range(n) for k in depots)
prob += cost

# Constraints
for k in depots:
    prob += pulp.lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1
    prob += pulp.lpSum(x[(j, k, k)] for j in range(n) if j != k) == 1
    for j in range(n):
        if j not in depots:
            prob += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j)
            prob += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in depots) == 1

for k in depots:
    for i in range(n):
        if i not in depots:
            prob += u[(i, k)] >= 1
    for (i, j) in product(range(n), repeat=2):
        if i != j and i not in depots and j not in depots:
            prob += u[(j, k)] >= u[(i, k)] + 1 - (n+1) * (1 - x[(i, j, k)])

# Solve the problem
prob.solve()

# Get the results
tours = {k: [] for k in depots}
costs = {k: 0 for k in depots}

for k in depots:
    i = k
    while True:
        for j in range(n):
            if pulp.value(x[(i, j, k)]) == 1:
                if i != j:
                    tours[k].append(i)
                    costs[k] += cost_matrix[(i, j)]
                    i = j
                break
        if i == k:
            tours[k].append(i)
            break

# Output
total_cost = sum(costs.values())
for k in depots:
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Overall Total Travel Cost: {total_cost}")