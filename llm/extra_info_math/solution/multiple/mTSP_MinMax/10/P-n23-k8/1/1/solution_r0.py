import math
from mip import Model, xsum, minimize, BINARY

# Given coordinates and the number of salesmen
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
n = len(coordinates)  # number of nodes
m = 8  # number of salesmen

# Calculate the Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Model creation
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(1, n)]

# Objective
max_distance = model.add_var()
model.objective = minimize(max_distance)

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        model.add_constr(xsum(x[p][j][k] for j in range(n) if j != p) -
                         xsum(x[i][p][k] for i in range(n) if i != p) == 0)

# Each salesman must leave the depot exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[i][0][k] for i in range(1, n)) == 1

# Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i-1] - u[j-1] + n * xsum(x[i][j][k] for k in range(m)) <= n - 1

# Maximizing the minimum distance traveled by any robot
for k in range(m):
    model += xsum(c[i][j] * x[i][j][k] for i in range(n) for j in range(n)) <= max_distance

# Solving the model
status = model.optimize(max_seconds=300)

# Output results
if status == model.OPTIMAL or status == model.FEASIBLE:
    print("Found a solution")
    for k in range(m):
        tour = []
        for i in range(n):
            for j in range(n):
                if x[i][j][k].x >= 0.99:
                    tour.append((i, j))
        # Simplify the tour representation
        optimized_tour = [0]
        current_location = 0
        while len(tour) > 0:
            for i, (start, end) in enumerate(tour):
                if start == current_location:
                    optimized_tour.append(end)
                    current_location = end
                    tour.pop(i)
                    break
        print(f'Robot {k} Tour: {optimized_tour}')
else:
    print("No feasible solution found")

# Calculate the max distance
distances = []
for k in range(m):
    cost = sum(c[i][j] * x[i][j][k].x for i in range(n) for j in range(n))
    distances.append(cost)
if distances:
    max_cost = max(distances)
    print(f'Maximum Travel Cost: {max_cost}')