import pulp
import math

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generating the distance matrix
n = len(coordinates)
distance_matrix = [[euclidean_length(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# SET UP THE OPTIMIZATION MODEL
model = pulp.LpProblem("VRP_Two_Robots", pulp.LpMinimize)

# Decision variables: x[i][j][k] where robot k travels from city i to city j
x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') if i != j else None 
       for j in range(n)] for i in range(n)] for k in range(2)]

# Objective function: Minimize the sum of selected distances
model += pulp.lpSum(distance_matrix[i][j] * x[i][j][k]
                    for k in range(2) for i in range(n) for j in range(n) if i != j)

# Constraint: Departure from each depot for each robot
for k in range(2):
    model += pulp.lpSum(x[k][j][k] for j in range(n) if j != k) == 1

# Constraint: Arrival to each depot for each robot
for k in range(2):
    model += pulp.lpSum(x[j][k][k] for j in range(n) if j != k) == 1

# Constraint: Each city must be visited exactly once by any robot
for c in range(2, n):  # Cities excluding depots
    model += pulp.lpSum(x[i][c][k] for k in range(2) for i in range(n) if i != c) == 1

# Constraint: Continuity of a route for each robot
for k in range(2):
    for j in range(1, n):  # Exclude the robot's start depot
        if j != k:  # Each non-depot city
            model += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) == pulp.lpSum(x[j][i][k] for i in range(n) if i != j)

# Solve the model
model.solve()

# Extract paths
paths = [[] for _ in range(2)]
costs = [0 for _ in range(2)]

# Utilize the solution
for k in range(2):
    start_city = k
    next_city = start_city
    while True:
        next_city = next((j for j in range(n) if pulp.value(x[next_city][j][k]) == 1 and j != next_city), None)
        if next_city is None or next_city == start_city:
            paths[k].append(start_city)
            break
        paths[k].append(next_city)
        if len(paths[k]) > 1:
            costs[k] += distance_matrix[paths[k][-2]][next_city]

print_result(paths, costs)

def print_result(paths, costs):
    overall_cost = sum(costs)
    for k in range(2):
        print(f"Robot {k} Tour: {paths[k]}")
        print(f"Robot {k} Total Travel Cost: {costs[k]:.2f}")
    print(f"Overall Total Travel Cost: {overall_cost:.2f}")