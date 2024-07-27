import pulp
import math

# Cities and their coordinates
cities = {
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
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Number of cities and Robots
n = len(cities)
m = 8  # Number of robots

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Travel cost matrix
c = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize LP problem
prob = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
prob += pulp.lpSum(c[i][j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# Each salesman leaves and enters the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Each salesman must leave and enter every other city
for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Subtour Elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
prob.solve()

# Processing the output
tours = {k: [0] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    start = 0
    while True:
        found_next = False
        for j in range(n):
            if x[start, j, k].varValue == 1:
                tours[k].append(j)
                costs[k] += c[start][j]
                start = j
                found_next = True
                break
        if not found_next or start == 0:
            break

# Output display
total_cost = sum(costs.values())
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {total_cost}")