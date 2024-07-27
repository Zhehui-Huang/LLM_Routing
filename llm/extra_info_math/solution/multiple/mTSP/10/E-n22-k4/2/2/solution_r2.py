import pulp
import math

# Coordinates of the cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
num_cities = len(coordinates)
num_robots = 4

def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (range(1, num_cities)), lowBound=0, upBound=num_cities - 1, cat=pulp.LpContinuous)

# Objective Function
problem += pulp.lpSum(distance(i, j) * x[i][j][k] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots) if i != j)

# Constraints
# Each non-depot city must be visited exactly once by one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# Each robot leaves depot once and returns once
for k in range(num_robots):
    problem += pulp.lpSum(x[0][j][k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j][0][k] for j in range(1, num_cities)) == 1

# Flow conservation
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) if i != j) - pulp.lpSum(x[j][i][k] for i in range(num_cities) if i != j) == 0

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += u[i] - u[j] + (num_cities) * x[i][j][k] <= num_cities - 1

# Solve the problem
problem.solve()

# Output Results
total_distance = 0
for k in range(num_robots):
    print(f"Robot {k} Tour:")
    first_city = next(i for i in range(num_cities) if x[0][i][k].value() == 1)
    tour = [0, first_city]
    distance_k = distance(0, first_city)

    while tour[-1] != 0:
        next_city = next(j for j in range(num_cities) if x[tour[-1]][j][k].value() == 1)
        tour.append(next_city)
        distance_k += distance(tour[-2], next_city)

    print(tour)
    print(f"Distance for Robot {k}: {distance_k:.2f}")
    total_distance += distance_k

print(f"Total Distance: {total_distance:.2f}")