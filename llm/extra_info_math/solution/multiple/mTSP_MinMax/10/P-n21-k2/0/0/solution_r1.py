from pulp import LpProblem, LpVariable, lpSum, LpMinimize, PULP_CBC_CMD
from math import sqrt

# Define the coordinates for the depot and the cities
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
n = len(cities)  # Total nodes
m = 2  # Number of salesmen

# Calculate euclidean distances between each pair of nodes
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distance = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Problem
prob = LpProblem("VRP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary', lowBound=0, upBound=1)
u = LpVariable.dicts("u", range(1, n), lowBound=0, cat='Continuous')

# Objective: Minimize the maximum travel cost among all the robots
max_distance = LpVariable("max_distance", lowBound=0, cat='Continuous')
prob += max_distance

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation for each salesman and each city
for k in range(m):
    prob += lp_vaSum(x[0, j, k] for j in range(1, n)) == 1  # leaving the depot
    prob += lpSum(x[j, 0, k] for j in range(1, n)) == 1  # returning to the depot
    for j in range(1, n):
        prob += lpSum(x[i, j, k] for i in range(n) if i != j) - lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Only one tour leaves from the depot
for j in range(1, n):
    prob += lpSum(x[0, j, k] for k in range(m)) == 1

# Subtour prevention
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] >= -n * (1 - x[i, j, k]) + 1

# Distance constraints to set the max_distance value
for k in range(m):
    prob += lpSum(distance[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
solver = PULP_CBC_CMD(msg=True)
prob.solve(solver)

# Extract tours
tours = {k: [] for k in range(m)}
for k in range(m):
    tour_sequence, cur_city = [], 0
    while True:
        next_cities = [(j, x[cur_city, j, k].varValue) for j in range(n) if j != cur_city and x[cur_city, j, k].varValue > 0.9]
        if not next_cities:
            break
        next_city = next_cities[0][0]
        tour_sequence.append(next_city)
        cur_city = next_city
        if cur_city == 0:
            break
    tours[k] = [0] + tour_sequence + [0]

# Calculate costs
costs = {k: sum(distance[tours[k][i], tours[k][i + 1]] for i in range(len(tours[k]) - 1)) for k in tours}

# Print results
for k, tour in tours.items():
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

max_cost = max(costs.values())
print(f"Maximum Travel Cost: {max_cost}")