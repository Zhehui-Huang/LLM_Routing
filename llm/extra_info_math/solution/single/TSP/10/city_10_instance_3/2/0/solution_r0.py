import pulp
import math
from itertools import combinations

# Coordinates of cities including the depot city 0
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Euclidean distance computation
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities including the depot
n = len(coordinates)

# Distance matrix
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables x_ij
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)],
                          cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # each city is left exactly once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # each city is entered exactly once

# Subtour elimination
for k in range(2, n):
    for S in combinations(range(1, n), k):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Check if a valid solution has been found
if status == pulp.LpStatusOptimal:
    tour = []
    current_city = 0
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        if next_city == 0:
            break
        current_city = next_city

    # Adjusting the output to satisfy 0-start requirement for the tour
    tour = [0] + tour
    total_cost = pulp.value(problem.objective)

    # Output the result
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("Failed to find a valid tour")