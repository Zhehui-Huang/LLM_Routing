import pulp
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of each city including depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)
m = 2  # Number of robots

# Create the distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
model = pulp.LpProblem("Vehicle_Routing_Problem", pulp.LpMinimize)

# Variables
x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for k in range(m)] for j in range(n)] for i in range(n)]
u = [pulp.LpVariable(f"u_{i}", lowBound=1, cat='Continuous') for i in range(1, n)]  # no u_0

# Objective Function
model += pulp.lpSum(distance_matrix[i][j] * x[i][j][k] for k in range(m) for i in range(n) for j in range(n))

# Each city must be visited exactly once by one robot
for j in range(1, n):
    model += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Each robot must leave and return to the depot
for k in range(m):
    model += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

# Flow conservation constraints
for k in range(m):
    for j in range(1, n):
        model += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) == pulp.lpSum(x[j][i][k] for i in range(n) if i != j)

# Subtour Elimination Constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i-1] - u[j-1] + (n-1) * x[i][j][k] <= n-2

# Solve the problem
model.solve()

# Output results
for k in range(m):
    print(f"Robot {k} Tour:")
    path = [0]
    current_location = 0
    while True:
        next_location = None
        for j in range(n):
            if pulp.value(x[current_location][j][k]) == 1:
                next_location = j
                path.append(next_location)
                current_location = next_location
                break
        if next_location == 0:
            print(path)
            break

for k in range(m):
    total_cost = sum(distance_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
    print(f"Robot {k} Total Travel Cost: {total_cost}")

overall_cost = sum(distance_matrix[path[i]][path[i + 1]] for k in range(m) for i in range(len(path) - 1))
print("Overall Total Travel Cost:", overall_cost)