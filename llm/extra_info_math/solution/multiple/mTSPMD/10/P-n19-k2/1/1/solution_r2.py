import pulp
import math

# Cities and Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Number of cities and two depots
n = len(coordinates)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) if i != j else 0 for j in range(n)] for i in range(n)]

# Initialize the model for minimizing
model = pulp.LpProblem("VRP_2_robots", pulp.LpMinimize)

# Decision variables
x = [[[pulp.LpVariable(f"x[{k}][{i}][{j}]", cat='Binary') for j in range(n)] for i in range(n)] for k in range(2)]

# Objective Function (Minimizing the total travel cost)
model += pulp.lpSum(distance_matrix[i][j] * x[k][i][j] for k in range(2) for i in range(n) for j in range(n) if i != j)

# Constraints
for k in range(2):
    # Departure and return of each robot to their respective depot
    model += pulp.lpSum(x[k][k][j] for j in range(n) if j != k) == 1
    model += pulp.lpSum(x[k][j][k] for j in range(n) if j != k) == 1

    # Every city must be visited exactly once by some robot
    for j in range(n):
        if j != k:
            model += pulp.lpSum(x[k][i][j] for i in range(n) if i != j) == pulp.lpSum(x[k][j][i] for i in range(n) if i != j)

# Each city should be visited exactly once by any robot
for j in range(n):
    if j not in [0, 1]:  # Excluding the depots
        model += pulp.lpSum(x[k][i][j] for k in range(2) for i in range(n) if i != j) == 1

# Solve the problem
model.solve()

# Retrieving the solution
robot_tours = [[] for _ in range(2)]
for k in range(2):
    start = k
    next_city = start
    while True:
        next_city = next(j for j in range(n) if pulp.value(x[k][next_city][j]) == 1)
        robot_tours[k].append(next_city)
        if next_city == start:
            break

# Calculate the total travel costs
total_costs = [0 for _ in range(2)]
for k in range(2):
    tour_length = len(robot_tours[k])
    for i in range(tour_length - 1):
        total_costs[k] += distance_matrix[robot_tours[k][i]][robot_tours[k][i + 1]]

overall_cost = sum(total_costs)

# Output results
for k in range(2):
    print(f"Robot {k} Tour: {robot_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")