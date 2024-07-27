from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, PULP_CBC_CMD
import math

# City coordinates
cities = {
    0: (16, 90),  1: (43, 99), 2: (80, 21),  3: (86, 92),
    4: (54, 93),  5: (34, 73), 6: (6, 61),   7: (86, 69),
    8: (30, 50),  9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Number of cities
n = len(cities)

# Create the problem variable:
prob = LpProblem("TSP", LpMinimize)

# Decision variables:
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpBinary)

# Objective function:
prob += lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Leave and enter constraints:
for k in range(n):
    prob += lpSum(x[(k, j)] for j in range(n) if k != j) == 1  # leave each city only once
    prob += lpSum(x[(i, k)] for i in range(n) if i != k) == 1  # enter each city only once

# Subtour elimination constraints:
from itertools import combinations
for s in range(2, n):
    for S in combinations(range(1, n), s):  # Ensure not including the depot in subtour constraints
         prob += lpRowSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

# Extract the tour starting from the depot
tour = [0]
visited = [False] * n
visited[0] = True
current_city = 0

for _ in range(n-1):
    for j in range(n):
        if j != current_city and x[(current_city, j)].value() == 1:
            tour.append(j)
            visited[j] = True
            current_city = j
            break

# Closing the tour by returning to the depot
tour.append(0)

# Calculate the travel cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")