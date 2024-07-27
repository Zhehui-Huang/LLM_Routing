import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

# Coordinates of the cities including the depot
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distance between two cities
def euclidean_dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

n = len(cities)
cost = [[euclidean_dist(i, j) for j in range(n)] for i in range(n)]

# Create the problem
prob = LpProblem("TSP", LpMinimize)

# Variables: x[i,j] is 1 if the tour goes from city i to city j
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function: minimize the total travel cost
prob += lpSum(x[(i, j)] * cost[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for i in range(2, n):
    for S in combinations(range(1, n), i):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem using CBC solver
prob.solve(PULP_CBC_CMD(msg=True))

# Determine the tour from the variables
tour = [0]
for _ in range(n - 1):
    next_city = [j for j in range(n) if x[(tour[-1], j)].varValue == 1][0]
    tour.append(next_city)

# Including return to the depot
tour.append(0)

# Calculate total cost
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))