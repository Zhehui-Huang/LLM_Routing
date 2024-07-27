import pulp
import math
from itertools import permutations, product

# City coordinates as given
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
number_of_cities = len(city_coordinates)
number_of_robots = 4

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Compute the distance matrix
distance_matrix = [[calculate_distance(city_coordinates[i], city_coordinates[j]) for j in range(number_of_cities)] for i in range(number_of_cities)]

# Creating the LP problem
problem = pulp.LpProblem("MultiRobotTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(number_of_cities), range(number_of_cities), range(number_of_robots)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, number_of_cities), lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += pulp.lpSum([distance_matrix[i][j] * x[i][j][k] for i, j, k in product(range(number_only_of_cities), repeat=3) if i != j])

# Constraints
# Each city is visited exactly once by one salesman:
for j in range(1, number_of_cities):
    problem += pulp.lpSum([x[i][j][k] for i in range(number_of_cities) for k in range(number_of_robots) if i != j]) == 1

# Each robot leaves and returns to the depot once
for k in range(number_of_robots):
    problem += pulp.lpSum([x[0][j][k] for j in range(1, number_of_cities)]) == 1
    problem += pulp.lpSum([x[j][0][k] for j in range(1, number_of_cities)]) == 1

# Flow conservation constraints
for k in range(number_of_robots):
    for j in range(1, number_of_cities):
        problem += pulp.lpSum([x[i][j][k] for i in range(number_of_cities) if i != j]) - pulp.lpSum([x[j][i][k] for i in range(number_of_cities) if i != j]) == 0

# Subtour elimination constraints
for i in range(1, number_of_cities):
    for j in range(1, number_of_cities):
        if i != j:
            for k in range(number_of_robots):
                problem += u[i] - u[j] + (number_of_cities - 1) * x[i][j][k] <= number_of_cities - 2

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Print results
total_cost = 0
for k in range(number_of_robots):
    tour = [0]
    next_city = 0
    while True:
        next_city = next(j for j in range(number_of_cities) if pulp.value(x[next_city][j][k]) == 1)
        if next_city == 0:
            break
        tour.append(next_city)
    tour.append(0)  # return to depot
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")