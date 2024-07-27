import pulp
from math import sqrt

# Define city coordinates and city groups
city_coords = [
    (50, 3), (41, 82), (25, 46), (30, 82),
    (71, 69), (80, 19), (89, 45), (75, 55),
    (11, 67), (7, 32)
]
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Compute Euclidean distance between points
def euclidean_distance(a, b):
    return sqrt((city_coords[a][0] - city_coords[b][0]) ** 2 + (city_coords[a][1] - city_coords[b][1]) ** 2)

# Define the problem
problem = pulp.LpProblem("RobotTourProblem", pulp.LpMinimize)

# Variables x_ij: whether the robot travels directly from i to j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary) for i in range(10) for j in range(10) if i != j}

# Objective: Minimize the distance traveled
problem += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(10) for j in range(10) if i != j)

# Depart from and return to the depot exactly once, and visiting one city per group
for group in city_groups:
    problem += pulp.lpSum(x[0, j] for j in group) == 1  # from depot to one city in each group
    problem += pulp.lpSum(x[j, 0] for j in group) == 1  # to depot from one city in each group

# Each city in a group must be entered and left exactly once
for k in range(10):
    if k != 0:
        problem += pulp.lpSum(x[i, k] for i in range(10) if i != k) == pulp.lpSum(x[k, j] for j in range(10) if j != k)

# Solving the problem
problem.solve()

# Retrieving the result
tour = [0]
current = 0
total_cost = 0.0
for _ in range(len(city_groups) + 1):
    next_city = [j for j in range(10) if j != current and pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    total_cost += euclidean_distance(current, next_city)
    current = next_city

tour.append(0)  # Return to depot
total_cost += euclidean_distance(current, 0)

# Displaying the result
print("Tour:", tour)
print("Total travel cost:", total_cost)