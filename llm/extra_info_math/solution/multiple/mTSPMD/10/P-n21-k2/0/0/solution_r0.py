import pulp
import math

# Coordinates of cities including the depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Calculate Euclidean distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Number of depots and total nodes
depots = [0, 1]
total_cities = len(coordinates)

# VRP formulation using Pulp
problem = pulp.LpProblem("Multiple_Depot_Vehicle_Routing_Problem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for k in depots for i in range(total_cities) for j in range(total_cities)), cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for k in depots for i in range(total_cities) for j in range(total_cities))

# Constraints
# Each customer city is visited exactly once
for j in range(total_cities):
    if j not in depots:
        problem += pulp.lpSum(x[i, j, k] for k in depots for i in range(total_cities)) == 1

# Ensure route continuity and correct number of trips from/to depots
for k in depots:
    for i in range(total_cities):
        # Sum of outgoing edges must be equal to incoming edges
        problem += pulp.lpSum(x[i, j, k] for j in range(total_cities) if j != i) == pulp.lpSum(x[j, i, k] for j in range(total_cities) if j != i)

    # Depart from the depot and return to the depot
    problem += pulp.lpSum(x[k, j, k] for j in range(total_cities) if j != k) == 1
    problem += pulp.lpSum(x[j, k, k] for j in range(total_cities) if j != k) == 1

# Solve the problem
problem.solve()

# Extract the tour and cost details
tours = {k: [] for k in depots}
costs = {k: 0 for k in depots}

for k in depots:
    next_city = k
    while True:
        tours[k].append(next_city)
        next_city = next(j for j in range(total_cities) if pulp.value(x[next_city, j, k]) == 1)
        if next_city == k:
            tours[k].append(next_city)
            break

for k in tours:
    tour_length = len(tours[k])
    costs[k] = sum(distance_matrix[tours[k][i]][tours[k][i + 1]] for i in range(tour_length - 1))

# Output
total_cost = sum(costs.values())
for k in depots:
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Overall Total Travel Cost: {total_cost}")