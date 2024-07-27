import pulp
from math import sqrt

# Define the data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
num_robots = 2
num_cities = len(coordinates)
depot = 0

# Calculate distance matrix
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the problem
problem = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat=pulp.LpContinuous)

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i][j][k] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots))

# Constraints
# Each salesperson leaves each city at most once and every city is visited exactly once by any salesman.
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots)) == 1

# Each salesperson leaves the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[depot][j][k] for j in range(1, num_cities)) == 1

# Each salesperson returns to the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[i][depot][k] for i in range(1, num_cities)) == 1

# Flow conservation constraint
for k in range(num_robots):
    for p in range(1, num_cities):
        problem += pulp.lpSum(x[i][p][k] for i in range(num_cities)) - pulp.lpSum(x[p][j][k] for j in range(num_cities)) == 0

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i][j][k] <= num_cities - 1

# Solve the problem
problem.solve()

# Extract Solution
tours = [[] for _ in range(num_robots)]
total_cost = 0

for k in range(num_robots):
    tour_cost = 0
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i][j][k]) == 1:
                tours[k].append(i)
                tour_cost += distance_matrix[i][j]
    tours[k].append(tours[k][0])  # complete the tour back to the depot
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")