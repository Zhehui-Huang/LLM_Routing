from mip import Model, xsum, minimize, BINARY, INTEGER
import math

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

n = len(coordinates)  # Number of cities including depot
m = 8  # Number of robots

# Function to calculate Euclidean distance between two cities
def distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

# Create a new model
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=INTEGER, lb=0) for i in range(n)]

# Objective: minimize the maximum distance traveled by any vehicle
max_distance = model.add_var()
model.objective = minimize(max_distance)

# Constraints

# Each city is visited exactly once by one robot
for j in range(1, n):  # excluding the depot i=0
    model += xsum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Robots must leave from and return to depot
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[i][0][k] for i in range(1, n)) == 1

# Proper tour formation for each robot
for k in range(m):
    for i in range(1, n):
        model += xsum(x[i][j][k] for j in range(n)) == xsum(x[j][i][k] for j in range(n))

# Subtour prevention
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * xsum(x[i][j][k] for k in range(m)) <= n - 1

# Distance constraints
for k in range(m):
    model += xsum(distance(i, j) * x[i][j][k] for i in range(n) for j in range(n)) <= max_distance

# Solving the model
model.optimize()

# Output the results
if model.num_solutions:
    for k in range(m):
        # Create tour from solution
        tour = [0]  # start at depot initially
        while len(tour) < n:
            next_city = [j for j in range(n) if x[tour[-1]][j][k].x >= 0.99][0]
            tour.append(next_enemy)
            if next_city == 0:
                break
        print(f"Robot {k} Tour: {tour}")
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        print(f"Robot {k} Total Travel Cost: {tour_distance}")

    max_cost = max_distance.x if model.num_solutions else float('inf')
    print(f"Maximum Travel Cost: {max_cost}")