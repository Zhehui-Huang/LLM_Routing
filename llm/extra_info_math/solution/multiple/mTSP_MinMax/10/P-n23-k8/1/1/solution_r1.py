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

# Constraint 1: Each city is visited exactly once by one robot
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Constraint 2: Flow conservation
for k in range(m):
    for p in range(1, n):
        model.add_constr(xsum(x[p][j][k] for j in range(n) if j != p) -
                         xsum(x[i][p][k] for i in range(n) if i != p) == 0)

# Constraint 3: Each robot must leave and return to the depot exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[i][0][k] for i in range(1, n)) == 1

# Constraint 4: Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i-1] - u[j-1] + n * xsum(x[i][j][k] for k in range(m)) <= n - 1

# Constraint 5: Maximizing the minimum distance traveled by any robot
for k in range(m):
    model += xsum(c[i][j] * x[i][j][k] for i in range(n) for j in range(n)) <= max_distance

# Solving the model
status = model.optimize(max_seconds=300)

# Output results
tours = []
if status == model.OPTIMAL or status == model.FEASIBLE:
    print("Found a solution")
    distances = []
    for k in range(m):
        tour = [0]
        cost = 0
        current = 0
        visited = set(tour)
        while len(visited) < n - 1:
            for j in range(1, n):
                if x[current][j][k].x >= 0.99 and j not in visited:
                    tour.append(j)
                    visited.add(j)
                    cost += c[current][j]
                    current = j
                    break
        tour.append(0)
        cost += c[current][0]
        tours.append((tour, cost))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {cost}")
        
    max_cost = max(t[1] for t in tours)
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("No feasible solution found")