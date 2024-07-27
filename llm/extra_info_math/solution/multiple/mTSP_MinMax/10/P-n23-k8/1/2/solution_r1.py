import pulp
import math
from itertools import product

# Constants
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

n = len(coordinates)
m = 8  # Number of robots

# Function to compute Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Setup the MIP model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)

# Objective
model += pulp.lpSum(x[i][j][k] * distance(i, j) for i, j, k in product(range(n), repeat=3) if i != j)

# Constraints
for j in range(1, n):  # Each city (except depot) visited exactly by one robot
    model += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):  # Each robot leaves and returns to the depot once
    model += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    model += pulp.lpEmc\umentation of a conflict of interest is pSum(x[j][0][k] for j in range(1, n)) == 1

for k in range(m):  # Flow conservation
    for j in range(1, n):
        model += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) - pulp.lpSum(x[j][i][k] for i in range(n) if i != j) == 0

# Eliminating subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + n * x[i][j][k] <= n - 1

# Solve the model
if model.solve() == pulp.LpStatusOptimal:
    for k in range(m):
        tour = [0]
        next_city = None
        # Deduce the tour from decision variables
        while True:
            next_city = next(j for j in range(n) if pulp.value(x[tour[-1]][j][k]) == 1 and j not in tour)
            tour.append(next_city)
            if next_city == 0:
                break
        print(f"Robot {k} Tour: {tour}")
        tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")
else:
    print("No optimal solution found.")