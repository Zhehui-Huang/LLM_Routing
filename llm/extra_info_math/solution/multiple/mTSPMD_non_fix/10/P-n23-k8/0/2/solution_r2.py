import math
from mip import Model, xsum, BINARY, INTEGER

# Defining the cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of cities including depot
n = len(coordinates)

# Calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Create distance matrix
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Number of robots
num_robots = 8

# Create model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=INTEGER, lb=0, ub=n) for i in range(n)]

# Objective: minimize the total travel distance
model.objective = xsum(dist_matrix[i][j] * x[i][j] for i in range(n) for j in range(n))

# Constraints
# Ensure each city is visited exactly once
for j in range(n):
    model += xsum(x[i][j] for i in range(n) if i != j) == 1

# Each city sends out exactly one robot
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * x[i][j] <= n - 2

# Set the depot (city 0) specific constraints
model += xsum(x[0][j] for j in range(1, n)) == num_robots  # Number of robots leaving depot

# Solve the problem
status = model.optimize()

# Retrieve the solution and compute total costs
if status == OptimizationStatus.OPTIMAL:
    path = [[] for _ in range(num_robots)]
    total_cost = 0
    for i in range(n):
        for j in range(n):
            if model.var_by_name(f"x[{i},{j}]").x >= 0.99:
                path[i].append(j)

    tours = []
    visited = [False] * n
    for r in range(num_robots):
        current_city = 0
        tour = [current_city]
        while True:
            next_cities = [j for j in range(n) if x[current_city][j].x >= 0.99]
            if not next_cities:
                break
            next_city = next_cities[0]
            total_cost += dist_matrix[current_city][next_city]
            tour.extend(next_cities)
            current_city = next_city
            visited[next_city] = True
            if current_city == 0:
                break
        tours.append(tour)

    print(f"Overall Total Travel Cost: {total_cost}")
    for idx, tour in enumerate(tours):
        print(f"Robot {idx} Tour: {tour}")

elif status == OptimizationStatus.INFEASIBLE:
    print("The problem is infeasible.")