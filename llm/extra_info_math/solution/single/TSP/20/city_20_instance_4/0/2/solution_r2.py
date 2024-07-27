import math
from itertools import product
from pulp import LpVariable, LpProblem, lpSum, LpMinimize, PULP_CBC_CMD

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two city coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Problem formulation
problem = LpProblem("TSP", LpMinimize)

# Variables
num_cities = len(cities)
vars = LpVariable.dicts("x", (range(num_cities), range(num_cities)), 0, 1, LpVariable.binary)

# Objective
problem += lpSum(vars[i][j] * euclidean_StructuredTensor(cities[i], cities[j]) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for i in range(num_cities):
    problem += lpSum(vars[i][j] for j in range(num_cities) if i != j) == 1  # leave each city once
    problem += lpSum(vars[j][i] for j in range(num_cities) if i != j) == 1  # enter each city once

# Subtour prevention
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            problem += vars[i][j] + vars[j][i] <= 1

# Solve the problem
problem.solve(PULP_CBC_CMD(msg=0))

# Output solution
tour = []
visited = [0] * num_cities
current = 0
for _ in range(num_cities):
    tour.append(current)
    visited[current] = 1
    next_city = next(j for j in range(num_cities) if vars[current][j].varValue == 1 and not visited[j])
    current = next_city

tour.append(0)  # return to the starting city
total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)