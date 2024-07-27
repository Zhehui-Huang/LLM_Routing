from pulp import LpProblem, LpVariable, lpSum, LpMinimize
from math import sqrt
import itertools

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

distance = {(i, j): euclideaners_distance(c, **) for i, cities[i] in cities.items() for j, cities[j] in cities.items()}

# Create the problem variable to contain the problem data
prob = LpProblem("Multi_Traveling_Salesman_Problem", LpMinimize)

# Variables: x[i, j, k] = 1 if salesman k travels from city i to city j
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)),
                     cat='Binary', lowBound=0, upBound=1)

# Dummy variables for sub-tour elimination, u[i] for city node positions in the tour
u = LpVariable.dicts("u", range(1, n), lowBound=0, cat='Continuous')

# Objective Function: Minimize the maximum travel cost among all tours
prob += lpSum([distance[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in range(m)])

# Constraints
# Each city (except the depot) is visited exactly once by one salesman
for j in range(1, n):
    prob += lpSum([x[i, j, k] for i in range(n) for k in range(m) if i != j]) == 1

# Each salesman leaves the depot exactly once
for k in range(m):
    prob += lpSum([x[0, j, k] for j in range(1, n)]) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(1, n):
        prob += lpSum([x[i, p, k] for i in range(n) if i != p]) - lpSum([x[p, j, k] for j in range(n) if j != p]) == 0
        
# Subtour Elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Results
tour_list = {}
cost_list = {}
max_cost = 0

for k in range(m):
    for i in range(n):
        for j in range(1, n):
            if x[i, j, k].varValue == 1:
                if k not in tour_list:
                    tour_list[k] = []
                    cost_list[k] = 0
                tour_list[k].append((i, j))
                cost_list[k] += distance[i, j]
                max_cost = max(max_cost, cost_list[k])

# Output the results
for k in range(m):
    tour = [0] + [j for i, j in tour_list[k]] + [0]
    print(f'Robot {k} Tour: {tour}')
    print(f'Robot {k} Total Travel Cost: {cost_list[k]}')

print(f'Maximum Travel Cost: {max_cost}')