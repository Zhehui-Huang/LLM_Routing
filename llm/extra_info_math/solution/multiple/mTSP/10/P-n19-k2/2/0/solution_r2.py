from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary
import math

# City coordinates, including depot (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
m = 2
# Number of nodes including the depot
n = len(coordinates)

# Euclidean distance function
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create problem
problem = LpProblem("Multiple_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 0, 1, LpBinary)
u = LpVariable.dicts("u", list(range(1, n)), lowBound=0)

# Cost matrix
c = [[eu.tance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Objective
problem += lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, n):
    problem += lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot departs from and arrives back at the depot
for k in range(m):
    problem += lpSum(x[0][j][k] for j in range(1, n)) == 1
    problem += lpSum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Output results
total_cost = 0
for k in range(m):
    tour = [0]
    next_city = 0
    while True:
        for j in range(n):
            if j != next_city and x[next_city][j][k].varValue > 0.9:
                next_city = j
                tour.append(j)
                break
        if next_city == 0:
            break
    tour.append(0)
    tour_cost = sum(c[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")