from pulp import *
from math import sqrt

# Define the coordinates for the depot and the cities
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}
n = len(cities)
m = 2  # Number of robots

# Calculate Euclidian distances between each pair of nodes
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distance = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n)}

# Define the model
model = LpProblem("Vehicle_Routing_Problem", LpMinimize)

# Define the variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')

# Add objective
model += lpSum(distance[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Each city is visited exactly once by one robot, excluding the depot
for j in range(1, n):
    model += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot leaves and enters the depot
for k in range(m):
    model += lpSum(x[0, j, k] for j in range(1, n)) == 1
    model += lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Continuity of tour for each robot
for k in range(m):
    for j in range(1, n):
        model += lpSum(x[i, j, k] for i in range(n) if i != j) - lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Solve the model
model.solve()

# Output the results if an optimal solution was found
if LpStatus[model.status] == 'Optimal':
    for k in range(m):
        tour = [0]
        while True:
            j = next(j for j in range(n) if pulp.value(x[tour[-1], j, k]) == 1)
            tour.append(j)
            if j == 0:
                break
        print(f"Robot {k} Tour: {tour}")
        tour_distance = sum(distance[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Robot {k} Total Travel Cost: {tour_distance}")
else:
    print("No optimal solution found.")