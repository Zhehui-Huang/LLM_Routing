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
prob += lp/tmp/ipykernel_903/359170547.pySum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints:
for k in range(n):
    prob += lpSum(x[(k, j)] for j in range(n) if k != j) == 1 # leave each city only once
    prob += lpSum(x[(i, k)] for i in range(n) if i != k) == 1 # enter each city only once

# Subtour elimination:
from itertools import combinations
for s in range(2, n):
    for S in combinations(range(1, n), s):  # starting at 1 to ensure 0 is not included in sets
        prob += lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
current_city = 0
while True:
    next_city = [j for j in range(n) if j != current_city and x[(current_city, j)].varValue == 1][0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break  # Return to depot city and stop

# Calculate the travel cost
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")