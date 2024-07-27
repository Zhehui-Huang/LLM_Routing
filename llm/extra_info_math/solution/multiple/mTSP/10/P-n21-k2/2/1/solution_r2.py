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
    20: (45, 35)
}

# Number of salesmen (robots)
m = 2
# Total number of nodes (cities)
n = len(cities)

# Euclidean distance calculator
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Initialize problem
problem = LpProblem("VRP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 0, 1, LpBinary)
u = LpVariable.dicts("u", [i for i in range(1, n)], 0, n-1, LpContinuous)

# Objective function
problem += lpSum(x[i, j, k] * euclidean_distance(i, j) for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each salesman departs from and arrives at the depot
for k in range(m):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Flow conservation
for j in range(1, n):
    for k in range(m):
        problem += lpSum(x[i, j, k] for i in range(n) if i != j) == lpSum(x[j, i, k] for i in range(n) if i != j)

# Problem solving
problem.solve()

# Output the results and ensure tours are closed by returning to the depot
overall_cost = 0
for k in range(m):
    tour = [0]
    current_city = 0
    while True:
        next_city = None
        for j in range(n):
            if j != current_city and x[current_city, j, k].varValue == 1:
                next_city = j
                break
        if next_city == 0:  # If we loop back to depot
            tour.append(0)
            tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
            overall_cost += tour_cost
            print(f"Robot {k} Tour: {tour}")
            print(f"Robot {k} Total Travel Cost: {tour_cost}")
            break
        elif next_city is not None:
            tour.append(next_city)
            current_city = next_city

print(f"Overall Total Travel Cost: {overall_cost}")