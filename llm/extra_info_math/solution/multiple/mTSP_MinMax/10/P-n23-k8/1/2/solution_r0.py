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

for k in range(m):  # Each robot leaves the depot once
    model += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

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
model.solve()

tours = [[] for _ in range(m)]
for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                tours[k].append((i, j))

# Convert index tours to full cycle tours starting and ending at the depot
def complete_tour(tour):
    current_location = 0
    ordered_tour = [0]
    while len(tour) > 0:
        for i, (frm, to) in enumerate(tour):
            if frm == current_location:
                ordered_tour.append(to)
                current_location = to
                tour.pop(i)
                break
    ordered_tour.append(0)  # return to depot
    return ordered_tour

completed_tours = [complete_tour(tour) for tour in tours]
tour_costs = [sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) for tour in completed_tours]

# Printing results
for k in range(m):
    print(f"Robot {k} Tour: {completed_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]:.2f}")

print(f"Maximum Travel Cost: {max(tour_costs):.2f}")