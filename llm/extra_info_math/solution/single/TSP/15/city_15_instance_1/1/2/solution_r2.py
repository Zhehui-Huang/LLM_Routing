from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpInteger, PULP_CBC_CMD
import math

cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

n = len(cities)
problem = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

# Objective
problem += lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j), "Total_Distance"

# Constraints
for i in range(n):
    problem += lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave i
    problem += lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter i

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n - 1) * x[(i, j)] <= n - 2

# Solve the problem
problem.solve(PULP_CBC_CMD())

# Get the tour
tour = [0]
current = 0
while True:
    for j in range(n):
        if j != current and x[(current, j)].varValue == 1:
            tour.append(j)
            current = j
            break
    if current == 0:
        break

# Calculating the total travel cost
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Print the output
print("Tour:", tour)
print("Total travel cost:", total_cost)