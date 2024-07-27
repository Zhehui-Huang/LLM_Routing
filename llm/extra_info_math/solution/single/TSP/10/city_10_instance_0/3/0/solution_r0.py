import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, LpBinary, lpSum
from math import sqrt
from itertools import combinations

# Coordinates for each city including the depot
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Number of cities including the depot
n = len(coordinates)

# Distance cost matrix
cost = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the problem
problem = LpProblem("TSP", LpMinimize)

# Decision variables
x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(n)] for i in range(n)]

# Objective function
problem += lpSum(x[i][j] * cost[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += lpSum(x[i][j] for j in range(n) if i != j) == 1
    problem += lpSum(x[j][i] for j in range(n) if i != j) == 1

# Eliminate subtours
for size in range(2, n):
    for subset in combinations(range(1, n), size):
        problem += lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Extract the tour and calculate total cost
tour = []
current_city = 0
visited = set([0])
total_cost = 0
while len(visited) < n:
    for j in range(n):
        if x[current_city][j].value() == 1:
            total_cost += cost[current_city][j]
            current_city = j
            visited.add(j)
            tour.append(j)
            break

# Closing the loop back to the depot
tour.append(0)
total_cost += cost[current_city][0]

print("Tour:", tour)
print("Total travel cost:", total_math.ceil(total_cost))

# Example output might vary as it's dependent on the optimal solver results:
# Tour: [0, 2, 1, 3, 4, 8, 7, 6, 5, 0]
# Total travel cost: 294 (for example)