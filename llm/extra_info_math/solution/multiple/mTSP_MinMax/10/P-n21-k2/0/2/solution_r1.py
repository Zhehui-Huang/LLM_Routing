# Dependencies
import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus, value

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)  # number of nodes including depot
m = 2  # number of robots (salesmen)

# Calculate distances
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Problem
problem = LpProblem("MTSP", LpMinimize)

# Variables
x = LpVariable.dicts('x', (range(n), range(n), range(m)), cat='Binary')  # travel from i to j by k
u = LpVariable.dicts('u', range(1, n), lowBound=0, cat='Continuous')  # position in tour

# Objective
problem += lpSum([distances[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m)])

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    problem += lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Salesman leaves and returns once to the depot
for k in range(m):
    problem += lpSum(x[0][j][k] for j in range(1, n)) == 1
    problem += lpSum(x[j][0][k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        problem += lpSum(x[i][j][k] for i in range(n) if i != j) - lpSum(x[j][i][k] for i in range(n) if i != j) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i][j][k] <= n - 1

# Solve the problem
problem.solve()

# Display results
for k in range(m):
    tour = [0]
    next_city = 0
    while True:
        next_city = next(j for j in range(n) if x[next_city][j][k].value() == 1)
        if next city == 0:
            break
        tour.append(next_city)
    tour.append(0)
    tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

# Calculate maximum cost
max_cost = max(sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) for k in range(m) for tour in tours)
print(f"Maximum Travel Cost: {max_cost}")