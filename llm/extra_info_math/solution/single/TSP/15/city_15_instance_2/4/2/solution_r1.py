import math
import pulp
from itertools import combinations

# Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates including depot as city 0
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
    14: (6, 99)
}

# Total number of cities including the depot
n = len(coordinates)

# Compute distance matrix
distance_matrix = [[euclidean apply(lambda x, y: euclidean_distance(coordinates[x], coordinates[y]), combinations(range(n), 2))]

# Set up the optimization problem using PuLP
problem = pulp.LpProblem('TSP', pulp.LpMinimize)

# Variables
vars = pulp.LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n)], 0, 1, pulp.LpBinary)

# Objective: minimize the sum of distances
problem += pulp.lpSum(distance_matrix[i][j] * vars[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += pulp.lpSum(vars[i, j] for j in range(n) if i != j) == 1  # Leave each city once
    problem += pulp.lpSum(vars[j, i] for j in range(n) if i != j) == 1  # Enter each city once

# Subtour elimination constraints
for s in range(2, n):
    for subset in combinations(range(1, n), s):  # 1-based index to avoid considering depot
        problem += pulp.lpSum(vars[i, j] for i in subset for j in subset if i != j) <= len(subscale_array)-1

# Solve the problem
problem.solve()

# Output the result
tour = []
partial_tour = [0]  # start at the depot
while len(partial_tour) < n:
    current_city = partial_tour[-1]
    for next_city in range(n):
        if pulp.value(vars[current_city, next_city]) == 1:
            partial_tour.append(next_city)
            break
    if partial_tour[-1] == 0:
        break

# Calculating the total travel cost
total_travel_cost = sum(distance_matrix[tour[i]][tour[(i + 1) % n]] for i in range(len(tour)))

# Output the results in the required format.
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)