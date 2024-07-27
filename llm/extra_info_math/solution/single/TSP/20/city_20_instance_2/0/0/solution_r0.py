import math
from pulp import LpMinimize, LpProblem, LpVariable, LpBinary, lpSum

# Coordinates of the cities including the depot
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def euclidean_dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

n = len(cities)
cost = [[euclidean_dist(i, j) for j in range(n)] for i in range(n)]

# Create the problem
prob = LpProblem("TSP", LpMinimize)

# Variables: x[i,j] is 1 if the tour goes from city i to city j
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat=LpBinary)

# Objective function: minimize the total travel cost
prob += lpSum(x[(i, j)] * cost[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leave each city only once
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints (using lifted constraints - lazy constraints method)
for i in range(2, n):
    for S in combinations(range(1, n), i):
        prob += lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Output the result
tour = []
active_edges = [(i, j) for i in range(n) for j in range(n) if x[(i,j)].varValue == 1]
current_city = 0
while len(active_edges) > 0:
    for i, j in active_edges:
        if i == current_city:
            tour.append(i)
            current_city = j
            active_edges.remove((i, j))
            break
tour.append(0)  # append the return to the depot

# Calculate total travel cost
total_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)