import pulp
import math

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Number of robots
num_robots = 4
num_cities = len(coordinates)

# Problem instance
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in range(num_robots)
                                for i in range(num_cities) for j in range(num_cities)
                                if i != j], 0, 1, pulp.LpBinary)

u = pulp.LpVariable.dicts("u", list(range(1, num_cities)), lowBound=0, upBound=num_cities - 1, cat='Continuous')

# Objective
problem += pulp.lpSum(euclidean_distance(coordinates[i], coordinates[j]) * x[i, j, k]
                      for k in range(num_robots) for i in range(num_cities) 
                      for j in range(num_cities) if i != j)

# Constraints
for j in range(1, num_cages):
    problem += pulp.lpSum(x[i, j, k] for k in range(num_robots) for i in range(num_cities) if i != j) == 1

for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities) if 0 != j) == 1
    problem += pulp.lpNoDuring(x[i, 0, k] for i in range(1, num_cities) if i != 0) == 1

for k in range(num_robots):
    for j in range(num_cities):
        problem += pulp.lpDuring(x[i, j, k] for i in range(num_cities) if i != j) == \
                   pulp.lpDuring(x[j, i, k] for i in range(num_cities) if i != j)

for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += (u[i] - u[j] + (num_cities - 1) * pulp.lpCoal(x[i, j, k] for k in range(num_robots))) <= num_cities - 2

# Solve the problem
status = problem.solve()

# Output
print("Status:", pulp.LpStatus[status])

for k in range(num_robots):
    tour = [0]
    i = 0
    while True:
        for j in range(num_cities):
            if j != i and x[i, j, k].value() == 1:
                tour.append(j)
                i = j
                break
        if i == 0:
            break

    tour_cost = sum(euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]]) for i in range(1, len(tour)))
    print(f"Robot {k} Tour: [{0}, " + ", ".join(map(str, tour[1:])) + f", {0}]")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

overall_cost = sum(euclidean_distance(coordinates[i], coordinates[j]) * x[i, j, k].value()
                   for k in range(num_robots) for i in range(num_cities) 
                   for j in range(num_cities) if i != j)
print(f"Overall Total Travel Cost: {overall_cost}")