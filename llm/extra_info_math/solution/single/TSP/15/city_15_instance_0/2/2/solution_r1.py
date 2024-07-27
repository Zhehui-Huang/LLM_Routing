import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD

# Cities coordinates
coordinates = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Number of cities
n = len(coordinates)

# Cost matrix computation
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
prob += lpSum(x[(i, j)] * cost[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

# Extracting the solution
tour = []
for i in range(n):
    for j in range(n):
        if x[(i, j)].varValue == 1:
            tour.append((i, j))

# Resolving order of the tour
visited = set()
current = 0
ordered_tour = [0]
while len(ordered_tour) < n:
    visited.add(current)
    for _, next_city in tour:
        if next_city not in visited and _ == current:
            ordered_tour.append(next_city)
            current = next_city
            break

ordered_tour.append(0)  # Completing the tour back to the depot city

# Calculating the total cost of the highly corrected tour
total_travel_cost = sum(cost[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))

print(f"Tour: {ordered_tour}")
print(f"Total travel cost: {total_travel_cost}")