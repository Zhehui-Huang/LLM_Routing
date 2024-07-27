import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the city coordinates (indexed from 0 to n)
coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

n = len(coordinates)  # Number of cities, including the depot city

# Create the distance matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define problem
problem = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], 0, 1, LpInteger)

# Objective
problem += lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if j != i) == 1  # leave each city
    problem += lpSum(x[j, i] for j in range(n) if j != i) == 1  # enter each city

# Subtour elimination
for s in range(2, n):  # size of subset
    for S in itertools.combinations(range(1, n), s):  # don't include depot
        problem += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve()

# Retrieve solution
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if x[current_city, j].value() == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Output tour and calculate total cost
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
print("Tour:", [0] + tour)
print("Total travel cost:", total_cost)