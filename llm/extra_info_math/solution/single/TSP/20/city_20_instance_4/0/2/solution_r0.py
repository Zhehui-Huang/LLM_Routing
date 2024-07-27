import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value, LpBinary

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities)
cost = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Setting up the problem
prob = LpProblem("TSP", LpMinimize)
x = LpVariable.dicts('x', cost.keys(), 0, 1, LpBinary)

# Objective Function: Minimize the total cost of the tour
prob += lpSum(x[(i, j)] * cost[(i, j)] for (i, j) in cost.keys())

# Constraints
for i in cities:
    prob += lpSum(x[(i, j)] for j in cities if (i, j) in x) == 1 # leave each city only once
    prob += lpSum(x[(j, i)] for j in cities if (j, i) in x) == 1 # enter each city only once

# Subtour elimination constraints
for i in range(2, n+1):  # from size 2 up to size n
    for S in itertools.combinations(cities, i):
        prob += lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
while True:
    tour.append(current)
    current = [j for j in cities if (current, j) in x and x[(current, j)].varValue == 1][0]
    if current == 0:
        break

# Calculate total travel cost
total_cost = sum(cost[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Results
print("Tour:", tour + [0])
print("Total travel, cost:", total_cost)