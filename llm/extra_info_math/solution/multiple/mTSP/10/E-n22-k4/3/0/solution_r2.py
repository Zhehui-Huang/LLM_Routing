import numpy as np
from math import sqrt
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus, value, LpBinary

# Coordinates of each city including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4
# Number of nodes including the depot
n = len(coordinates)

# Calculate Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the optimization problem
problem = LpProblem("MDVRP", LpMinimize)

# Decision variable x[i][j][k]: whether robot k travels from city i to city j
x = LpVariable.dicts("x", [(i, j, k) for k in range(num_robots) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)
# Helper variable u[i] for subtour elimination
u = LpVariable.dicts("u", range(1, n), lowBound=0)

# Objective: minimize the total distance traveled by all robots
problem += lpSum(distance_matrix[i][j] * x[i, j, k] for k in range(num_robots) for i in range(n) for j in range(n) if i != j)

# Each city is visited once: entry and exit by any robot
for j in range(1, n):
    problem += lpSum(x[i, j, k] for k in range(num_robots) for i in range(n) if i != j) == 1
    problem += lpSum(x[j, i, k] for k in range(num_robots) for i in range(n) if i != j) == 1

# Each robot must leave and return to the depot
for k in range(num_robots):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Check if the problem was solved to optimality
if LpStatus[problem.status] == "Optimal":
    # Extract tours for each robot
    tours = {k: [] for k in range(num_robots)}
    for k in range(num_robots):
        tour = [0]  # start at the depot
        current_city = 0
        while True:
            next_cities = [j for j in range(n) if j != current_city and value(x[current_city, j, k]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            tour.append(next_city)
            current_city = next_city
        tour.append(0)  # end at the depot
        tours[k] = tour

        # Calculate and print the cost of the tour
        tour_cost = sum(distance_matrix[tours[k][i]][tours[k][i + 1]] for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tours[k]}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    # Overall cost
    overall_cost = sum(sum(distance_matrix[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1)) for k in range(num_robots))
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("Failed to reach optimality.")