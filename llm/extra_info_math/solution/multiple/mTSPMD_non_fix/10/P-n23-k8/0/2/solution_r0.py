import math
from mip import Model, xsum, BINARY, OptimizationStatus

# Coordinates of the cities (depot inclusive)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of salesmen
m = 8
# Number of cities (including depots)
n = len(coordinates)
# All cities indices
V = range(n)

# Depot starts for all salesmen (multiple salesmen starting from depot city 0)
D = [0] * m

# Calculating Euclidean distance between cities
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Cost matrix
c = [[euclidean_distance(i, j) for j in V] for i in V]

# Create model
model = Model()

# Variables: x[i, j] == 1 if city j is visited after city i; 0 otherwise
x = [[model.add_var(var_type=BINARY) for j in V] for i in V]

# Objective: minimize the total travel cost
model.objective = xsum(c[i][j] * x[i][j] for i in V for j in V if i != j)

# Constraints
# Each city must be visited exactly once
for j in range(1, n):
    model += xsum(x[i][j] for i in V if i != j) == 1
    model += xsum(x[j][i] for i in V if i != j) == 1

# Subtour prevention by ensuring exactly one connection from and to depot cities
for i, dx in enumerate(D):
    model += xsum(x[dx][j] for j in V if j != dx) == 1
    model += xsum(x[j][dx] for j in V if j != dx) == 1

# Additional subtour elimination constraints
u = [model.add_var() for i in V]
for i in V:
    for j in V:
        if i != j and (i not in D or j not in D):
            model += u[i] - u[j] + n * x[i][j] <= n-1

# Solve the problem
status = model.optimize()

# Output results
total_cost = 0
tours = []

if model.num_solutions:
    for d_index in D:
        tour = [d_index]
        while True:
            next_city = [j for j in V if model.vars[n * tour[-1] + j].x >= 0.99][0]
            if next_city == d_index:
                break
            tour.append(next_city)
        tours.append(tour)
        tour_cost = sum(c[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {D.index(d_index)} Tour: {tour}")
        print(f"Robot {D.index(d_index)} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found")