import pulp
import math
from itertools import product

# Coordinates for each city including the depot (0 indexed)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Compute distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Constants
n = len(coordinates)  # Total cities including depot
m = 4  # Number of robots

# Define the cost matrix
cost = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Setting up the problem
problem = pulp.LpProblem("VRP_Multi_Salesman", pulp.LpMinimize)

# Assignment variables: x[i, j, k] = 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j, k) for i, j, k in product(range(n), range(n), range(m)) if i != j], cat=pulp.LpBinary)

# Positional variables, helps prevent subtour
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n, cat=pulp.LpContinuous)

# Objective: minimize the maximum distance
max_distance = pulp.LpVariable("max_distance", lowBound=0)
problem += max_distance

# Each city is visited exactly once by exactly one robot, starting from depot
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot leaves each city exactly once and returns exactly once
for k in range(m):
    for i in range(n):
        problem += pulp.lpSum(x[i, j, k] for j in range(n) if i != j) == pulp.lpSum(x[j, i, k] for j in range(n) if i != j)

# Each robot starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Limit maximum distance for any robot
for k in range(m):
    problem += pulp.lpSum(cost[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solving the problem
if problem.solve() == pulp.PULP_CBC_CMD(msg=False):
    print("Optimal solution found.")
    
    # Output results
    for k in range(m):
        print(f"Robot {k} tour:")
        for i in range(n):
            for j in range(n):
                if i != j and x[i, j, k].varValue == 1:
                    print(f"{i} -> {j}", end=" ")
        print("\n")
    
    print(f"Maximum distance traveled: {max_distance.varValue}")
else:
    print("No optimal solution found.")