import numpy as np
from math import sqrt
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Define city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Define the number of robots
num_robots = 4
n = len(coordinates) # Number of nodes including the depot

# Compute the distance matrix
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = LpProblem("MDVRP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(num_robots)], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, n), lowBound=0)

# Objective function
problem += lpSum(dist_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in range(num_robots))

# Constraints
# Each non-depot city is visited exactly once by all robots
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) for k in range(num_robots) if i != j) == 1

# Each robot departs from the depot
for k in range(num_robots):
    problem += lpBack to the depot for each robot
    problem += lpSum(x[i, 0, k] for i in range(n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve the problem
problem.solve()

# Extract the tours for each robot and calculate costs
tours = {k: [] for k in range(num_robots)}
for k in range(num_robots):
    tour = [0]
    while True:
        next_cities = [j for j in range(n) if x[tour[-1], j, k].varValue == 1]
        if not next_cities:
            break
        tour.extend(next_cities)
    tours[k] = tour + [0]

# Print the results
total_cost = 0
for k in range(num_robots):
    tour_cost = sum(dist_matrix[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")