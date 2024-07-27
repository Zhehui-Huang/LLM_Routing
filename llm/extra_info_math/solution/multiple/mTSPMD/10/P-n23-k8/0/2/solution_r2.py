import numpy as np
from pulp import *

# Define the coordinates of each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculating Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Building the distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Initialize the problem
problem = LpProblem("VRP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), cat='Binary')
u = LpVariable.dicts("u", range(num_cities), lowBound=0, cat="Continuous")

# Objective function
problem += lpSum(distance_matrix[i][j] * x[i][j][k] for k in range(num_robots) for i in range(num_cities) for j in range(num_cities))

# Constraints
# Enter and exit each city once
for k in range(num_robots):
    for j in range(num_cities):
        if j != k:  # Ignore depot self-loops
            problem += lpSum(x[i][j][k] for i in range(num_cities) if i != j) == lpSum(x[j][i][k] for i in range(num_cities) if i != j), f"flow_continuity_{j}_{k}"

# Each robot returns to its starting depot
for k in range(num_robots):
    problem += lpSum(x[k][j][k] for j in range(num_cities) if j != k) == 1, f"start_from_depot_{k}"
    problem += lpSum(x[j][k][k] for j in range(num_cities) if j != k) == 1, f"return_to_depot_{k}"

# Subtour elimination
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i][j][k] <= num_cities - 1, f"subtour_elimination_{i}_{j}_{k}"

# Solve the problem
problem.solve()

# Display the tours for each robot
overall_cost = 0
for k in range(num_robots):
    city = k
    tour = [city]
    tour_cost = 0
    while True:
        next_cities = [j for j in range(num_cities) if x[city][j][k].varValue == 1]
        if next_cities:
            next_city = next_cities[0]
            tour_cost += distance_matrix[city][next_city]
            city = next_city
            if city == k:
                break
            tour.append(city)
        else:
            break
    tour.append(k)  # Return to depot
    overall_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")