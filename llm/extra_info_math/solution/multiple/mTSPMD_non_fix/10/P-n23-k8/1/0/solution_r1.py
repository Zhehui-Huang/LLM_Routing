import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpStatus, value

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Constants and Indices
num_nodes = len(coordinates)
depots = [0]  # All robots start at depot city 0
nodes = list(range(num_nodes))
num_robots = 8

# Distance calculations
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in nodes for j in nodes if i != j}

# Problem definition
model = LpProblem("Robot_Routes", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in nodes for j in nodes if i != j), cat=LpBinary)

# The objective function is to minimize the sum of the distances
model += lpSum(x[i, j] * distances[i, j] for i in nodes for j in nodes if i != j)

# Each non-depot node is entered and left exactly once
for j in [n for n in nodes if n not in depots]:
    model += lpSum(x[i, j] for i in nodes if (i, j) in x) == 1
    model += lpSum(x[j, i] for i in nodes if (j, i) in x) == 1

# Set the number of robots departing from the initial depot
model += lpSum(x[0, j] for j in nodes if (0, j) in x) == num_robots

# Each non-depot node must be entered and left exactly once
for k in [n for n in nodes if n not in depots]:
    model += lpSum(x[k, i] for i in nodes if (k, i) in x) == 1

# Solving the model
model.solve()

# Output solution
if LpStatus[model.status] == 'Optimal':
    tours = [[] for _ in range(num_robots)]
    for i in range(num_robots):
        start = 0
        while True:
            next_town = [j for j in nodes if value(x[start, j]) == 1]
            if not next_town:
                break
            next_town = next_town[0]
            tours[i].append(next_town)
            if len(tours[i]) > 1 and tours[i][0] == tours[i][-1]:
                break
            start = next_town

    total_cost = 0
    for idx, tour in enumerate(tours):
        if len(tour) > 1:
            cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
            total_cost += cost
            print(f"Robot {idx} Tour: {tour}")
            print(f"Robot {idx} Total Travel Cost: {cost}")

    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("Failed to find optimal solution")