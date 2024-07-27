from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
import math

# City coordinates
cities = {
    0: (16, 90),  1: (43, 99), 2: (80, 21),  3: (86, 92),
    4: (54, 93),  5: (34, 73), 6: (6, 61),   7: (86, 69),
    8: (30, 50),  9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of cities
n = len(cities)

# Create the problem variable:
prob = LpProblem("TSP", LpMinimize)

# Decision variables:
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpBinary)

# Objective function:
prob += lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints:
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1      # leave each city only once
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1      # enter each city only once

# Subtour elimination constraints:
from itertools import combinations
for S in range(2, n):
    for subset in combinations(range(1, n), S):
        prob += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
total_cost = 0

# Start at the depot city 0
current_city = 0
visited = [False]*n
visited[0] = True

for _ in range(n):
    for j in range(n):
        if j != current city and not visited[j] and x[current_city, j].varValue == 1:
            tour.append(j)
            total_cost += distance(current_city, j)
            current_city = j
            visited[j] = True
            break

# Close the tour by returning to the depot
tour.append(0)
total_cost += distance(current_city, 0)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")