from mip import Model, xsum, minimize, BINARY
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
u = [model.add_var() for i in range(1, n)]

# Objective: minimize the maximum distance traveled by any vehicle
max_distance = model.add_var()
model.objective = minimize(max_distance)

# Constraints

# Each city is visited exactly once by one robot
for j in range(1, n):  # excluding the depot i=0
    model += xsum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Flow conservation constraints for non-depot cities
for k in range(m):
    for p in range(1, n):  # excluding the depot i=0
        model += xsum(x[i][p][k] for i in range(n)) - xsum(x[p][j][k] for j in range(n)) == 0

# Each robot leaves the depot exactly once and returns exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[i][0][k] for i in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i-1] - u[j-1] + n * x[i][j][k] <= n - 1

# Max distance calculation
for k in range(m):
    model += xsum(distance(i, j) * x[i][j][k] for i in range(n) for j in range(n)) <= max_distance

# Solving the model
model.optimize()

# Output the solution
if model.num_solutions:
    for k in range(m):
        tour = []
        for i in range(n):
            for j in range(n):
                if x[i][j][k].x >= 0.99:
                    tour.append((i, j))
        tour = sorted(tour, key=lambda x: x[0])
        proper_tour = [0] + [j for i, j in tour if i == 0]
        current_city = proper_tour[-1]
        while len(proper_tour) < n:
            for i, j in tour:
                if i == current_city:
                    current_city = j
                    proper_tour.append(j)
                    break
        print(f"Robot {k} Tour: {proper_tour}")
        tour_distance = sum(distance(proper_tour[i], proper_tour[i+1]) for i in range(len(proper_tour)-1))
        print(f"Robot {k} Total Travel Cost: {tour_distance}")

    print(f"Maximum Travel Cost: {max_distance.x}")