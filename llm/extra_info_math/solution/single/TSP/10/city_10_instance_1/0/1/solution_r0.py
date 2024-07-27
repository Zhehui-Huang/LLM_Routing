import pulp
import math
from itertools import combinations

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of cities
n = len(cities)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Retrieve the solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Determine the order starting from depot 0
order = [0]
while len(order) < n:
    for (i, j) in tour:
        if order[-1] == i:
            order.append(j)
            break

# Append the start city to the end to complete the tour
order.append(0)

# Calculate total tour cost
total_cost = sum(distance(order[i], order[i+1]) for i in range(len(order)-1))

# Output the result
print("Tour:", order)
print("Total travel cost:", total_cost)