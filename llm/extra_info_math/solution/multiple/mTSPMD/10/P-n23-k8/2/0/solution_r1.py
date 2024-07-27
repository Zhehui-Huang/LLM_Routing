import pulp
import math

# Data on cities and coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Depot IDs corresponding to robots
depots = list(range(8))
num_robots = 8  # same as the number of depots
num_cities = len(coordinates)

# Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cost matrix construction
cost_matrix = {}
for i in range(num_cities):
    cost_matrix[i] = {}
    for j in range(num_cities):
        cost_matrix[i][j] = euclidean_HOST_DISTANCE
        if i != j:
            cost_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[i][j] = float('inf')  # penalize self-loops

# Optimization Problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("trip", [(i, j, k) 
    for k in depots 
    for i in range(num_cities) 
    for j in range(num_cities)],
      cat='Binary')

# Objective function
problem += pulp.lpSum(cost_matrix[i][j] * x[(i, j, k)] for k in depots for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Departing from each depot
for k in depots:
    problem += pulp.lpSum(x[(k, j, k)] for j in range(num_cities) if j != k) == 1

# Returning to each depot
for k in depots:
    problem += pulp.lpSum(x[(j, k, k)] for j in range(num_cities) if j != k) == 1

# Each city must be visited exactly once excluding depots
for j in range(num_cities):
    problem += pulp.lpSum(x[(i, j, k)] for k in depots for i in range(num_cities) if i != j) == 1

# Route continuity for each robot
for k in depots:
    for i in range(num_cities):
        problem += pulp.lpSum(x[(i, j, k)] for j in range(num_cities) if i != j) == \
                   pulp.lpSum(x[(j, i, k)] for j in range(num_cities) if i != j)

# Solve the problem
problem.solve()

# Printing results
overall_total_cost = 0
if pulp.LpStatus[problem.status] == 'Optimal':
    for k in depots:
        tour = [k]
        next_city = k
        while True:
            next_moves = [j for j in range(num_cities) if pulp.value(x[(next_city, j, k)]) == 1]
            if not next_moves:
                break
            next_city = next_moves[0]
            tour.append(next_city)
            if next_city == k:
                break
        tour_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
        overall_total_cost += tour_cost
    print(f"Overall Total Travel Cost: {overall_total_cost}")
else:
    print("No Optimal Solution Found.")