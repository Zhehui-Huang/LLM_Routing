import numpy as np
import pulp
import itertools

# Define the cities' coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(coordinates)

# Compute the Euclidean distance between each pair of cities
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the PuLP model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path goes from city i to city j
x = {(i, j): pulp.LpVariable(f'x_{i}_{j}', cat=pulp.LpBinary) for i in range(n) for j in range(n)}

# Max distance variable
M = pulp.LpVariable("M", lowBound=0, cat=pulp.LpContinuous)

# Objective function: minimize M (the maximum distance traveled between any two consecutive cities)
model += M

# Constraints
# Each city must be left exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1

# Each city must be entered exactly once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Eliminate subtours
for r in range(2, n):
    for S in itertools.combinations(range(1, n), r):
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Max distance constraints (link x and M)
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distanceator for details about these commands. Matrix[i][j] <= M

# Solve the problem using PuLP's CBC solver
model.solve()

# Compute the tour from the decision variables
tour = []
current_city = 0
tour.append(current_city)

for _ in range(n - 1):
    next_city = [j for j in range(n) if pulp.value(x[current_city, j]) == 1 if current_city != j][0]
    tour.append(next_city)
    current_city = next_city

# Returning to the starting city (depot)
tour.append(0)

# Tour cost details
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_dist_btwn_consecutive_cities = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost:.2f}')
print(f'Maximum distance between consecutive cities: {max_dist_btwn_consecutive_cities:.2f}')