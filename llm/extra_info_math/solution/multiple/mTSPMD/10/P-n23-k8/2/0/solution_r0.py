import pulp
import math

# Data on cities and coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Depot IDs corresponding to robots
depots = list(range(8))
num_robots = len(depots)
num_cities = len(coordinates)

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Creating the cost matrix
cost_matrix = {}
for i in range(num_cities):
    cost_matrix[i] = {}
    for j in range(num_cities):
        if i != j:
            cost_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[i][j] = float('inf')  # disallow self-loops

# Problem declaration
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("trips", [(i, j, k) for k in depots for i in range(num_cities) for j in range(num_cities)],
                          cat='Binary')

# Objective function
problem += pulp.lpSum(cost_matrix[i][j] * x[(i, j, k)] for k in depots for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each robot starts and ends at their depot
for k in depits:
    problem += pulp.lpSum(x[(k, j, k)] for j in range(num_cities) if j != k) == 1
    problem += pulp.lpSum(x[(j, k, k)] for j in range(num_cities) if j != k) == 1

# Each city is visited exactly once
for j in range(num_cities):
    if j not in depots:
        problem += pulp.lpSum(x[(i, j, k)] for k in depots for i in range(num_cities) if i != j) == 1

# Continuity of a tour for each robot without considering depots
for k in depots:
    for i in range(num_cities):
        problem += pulp.lpSum(x[(i, j, k)] for j in range(num_cities) if i != j) == pulp.lpSum(x[(j, i, k)] for j in range(num_cities) if i != j)

# Solving the model
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))
if status == pulp.LpStatusOptimal:
    print("Solution found")
    total_cost = 0
    for k in depots:
        print(f"Robot {k} Tour: ", end="")
        tour_cost = 0
        current_city = k
        tour = [current_city]
        while True:
            next_cities = [j for j in range(num_cities) if pulp.value(x[(current_city, j, k)]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            tour_cost += cost_matrix[current_city][next_city]
            current_city = next_city
            tour.append(current_city)
            if current_city == k:
                break
        print(tour)
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Stress: {total_cost}")
else:
    print("An optimal solution has not been found.")