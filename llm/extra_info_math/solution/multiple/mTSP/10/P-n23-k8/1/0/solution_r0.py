from pulp import *
import math

# Define the cities and their coordinates
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
n = len(cities)
m = 8  # Number of robots

# Calculate costs (Euclidean distances)
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

costs = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Problem model
model = LpProblem("mTSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')

# Objective
model += lpSum(costs[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    model += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Salesmen leave and enter the depot
for k in range(m):
    model += lpSum(x[0, j, k] for j in range(1, n)) == 1
    model += lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        model += lpSum(x[i, p, k] for i in range(n) if i != p) - lpSum(x[p, j, k] for j in range(n) if j != p) == 0

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + n*x[i, j, k] <= n-1

# Solve the problem
model.solve()

# Output the tours and costs
overall_total_cost = 0
for k in range(m):
    tour = [0]
    while True:
        found_next = False
        for j in range(n):
            if x[tour[-1], j, k].varValue == 1:
                tour.append(j)
                found_next = True
                break
        if not found_next or tour[-1] == 0:
            break
    tour_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour
print(f"Overall Total Travel Cost: {overall_total_count}")