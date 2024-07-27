import pulp
from math import sqrt

# Data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
num_robots = 2
num_cities = len(coordinates)
depot = 0

# Distance matrix calculation
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Optimization problem
problem = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += pulp.lpSum(distance_matrix[i][j] * x[i][j][k] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots))

# Constraints
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots)) == 1

for k in range(num_robots):
    problem += pulp.lpSum(x[depot][j][k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j][depot][k] for j in range(1, num_cities)) == 1

for k in range(num_robots):
    for p in range(1, num_cities):
        problem += pulp.lpSum(x[i][p][k] for i in range(num_cities)) - pulp.lpSum(x[p][j][k] for j in range(num_cities)) == 0

for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += u[i] - u[j] + (num_cities) * x[i][j][0] <= num_cities - 1

# Solve the problem
if problem.solve() == pulp.LpStatusOptimal:
    paths = [[] for _ in range(num_robots)]
    costs = [0] * num_robots
    
    for k in range(num_robots):
        path = []
        current_city = depot
        while True:
            next_city = None
            for j in range(num_cities):
                if pulp.value(x[current_city][j][k]) == 1:
                    path.append(j)
                    next_city = j
                    costs[k] += distance_matrix[current_city][j]
                    current_city = j
                    break
            if next_city == depot:
                break
        paths[k] = path

    for k in range(num_robots):
        print(f"Robot {k} Tour: {paths[k]}")
        print(f"Robot {k} Total Travel Cost: {costs[k]}")

    overall_cost = sum(costs)
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("Optimal solution not found.")