from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, LpBinary
import itertools
import math

# Define the coordinates of the cities
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def euclidean_dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Number of cities including the depot
n = len(coordinates)

# Cost matrix c_ij
cost = {(i, j): euclidean_input_vector_dist(i, j) for i in coordinates for j in coordinates if i != j}

# Creating the problem
model = LpProblem("tsp", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j], cat='Binary')

# Objective function
model += lpSum(x[i, j] * cost[i, j] for i in coordinates for j in coordinates if i != j)

# Constraints
for k in coordinates:
    model += lpSum(x[i, k] for i in coordinates if i != k and (i, k) in x) == 1
    model += lpSum(x[k, j] for j in coordinates if k != j and (k, j) in x) == 1

# Subtour elimination constraints
for s in range(2, n):
    for S in itertools.combinations([i for i in coordinates if i != 0], s):  # exclude depot
        model += lpSum(x[i, j] for i in S for j in S if i != j and (i, j) in x) <= len(S) - 1

# Solve the problem
model.solve()

# Retrieving the solution
tour = [0]
total_distance = 0

while True:
    current_city = tour[-1]
    next_cities = [j for j in coordinates if j != current_city and x[(current_city, j)].value() == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    total_distance += cost[(current_city, next_city)]

    if next_city == 0:
        break

# Output
print("Tour:", tour)
print("Total travel cost:", total_distance)