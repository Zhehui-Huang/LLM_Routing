from math import sqrt
from mip import Model, xsum, minimize, BINARY

# Defining coordinates (with depot cities included)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

n = len(coordinates)  # Number of nodes or cities
m = 4  # Number of robots or salesmen (one for each depot)

# Calculate distance matrix
dist = [[sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 +
              (coordinates[i][1] - coordinates[j][1]) ** 2)
         for j in range(n)] for i in range(n)]

# Create model
model = Model()

# Variables: x[i][j][k] = 1 if salesman k travels from city i to city j
x = [[[model.add_var('x({},{},{})'.format(i, j, k), var_type=BINARY) for k in range(m)]
      for j in range(n)] for i in range(n)]

# Optimization Function: Minimize the total distance traveled
model.objective = minimize(xsum(dist[i][j]*x[i][j][k] for i in range(n)
                                for j in range(n) for k in range(m)))

# Constraints
# Each non-depot city is visited exactly once by any salesman
for j in range(4, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Salesman leaves and enters his respective depot
for k in range(m):
    model += xsum(x[k][j][k] for j in range(n) if j != k) == 1
    model += xsum(x[j][k][k] for j in range(n) if j != k) == 1

# Every city must be left by the salesman arriving there
for j in range(1, n):
    for k in range(m):
        model += xsum(x[i][j][k] for i in range(n) if i != j) == \
                 xsum(x[j][i][k] for i in range(n) if i != j)

# Eliminate subtours
u = [model.add_var('u({})'.format(i)) for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n-1) * x[i][j][k] <= n-2

# Solve the model
model.optimize()

# Retrieve and print routes for each robot
for k in range(m):
    tour = []
    for i in range(n):
        for j in range(n):
            if x[i][j][k].x >= 0.99:
                tour.append((i, j))
    # Generate tour sequence
    current_location = k
    sequence = [current_location]
    tour_cost = 0
    while len(sequence) < len(tour) + 1:
        for (i, j) in tour:
            if i == current_location:
                current_location = j
                tour_cost += dist[i][j]
                sequence.append(j)
                break
    print(f"Robot {k} Tour: {sequence}")
    print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")

# Calculate and print the overall cost
overall_cost = sum(dist[i][j] for k in range(m)
                   for i in range(n) for j in range(n) if x[i][j][k].x > 0.99)
print(f"Overall Total Travel Cost: {overall_cost:.2f}")