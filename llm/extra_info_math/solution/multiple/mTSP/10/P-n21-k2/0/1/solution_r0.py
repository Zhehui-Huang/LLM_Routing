import math
from mip import Model, xsum, minimize, BINARY

# Define the cities and their coordinates
cities = [
    (30, 40),  # Depot
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distances between every pair of nodes
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

n = len(cities)
m = 2  # Number of robots
dist = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create model
model = Model()

# Variables:
# x[i][j][k] == 1 if robot k travels from city i to city j
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]

# u[i] represents position of city i in the tour
u = [model.add_var() for i in range(n)]

# Objective: minimize the total travel cost
model.objective = minimize(xsum(dist[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m)))

# Constraints
for j in range(1, n):  # Excluding depot city 0
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot begins at the depot
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1

# Each robot ends at the depot
for k in range(m):
    model += xsum(x[i][0][k] for i in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        model += xsum(x[i][j][k] for i in range(n) if i != j) == xsum(x[j][i][k] for i in range(n) if i != j)

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * xsum(x[i][j][k] for k in range(m)) <= n - 2
            
# Solve model
model.optimize()

# Extract tours for each robot
tours = [[[] for k in range(m)] for i in range(n)]
for k in range(m):
    for i in range(n):
        for j in range(n):
            if x[i][j][k].x >= 0.99:
                tours[i][k].append(j)

for k in range(m):
    tour = [0]
    while len(tours[tour[-1]][k]) != 0:
        tour.append(tours[tour[-1]][k].pop())

    travel_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {travel_cost}")

# Total cost
overall_cost = sum(dist[tour[i]][tour[i + 1]] for k in range(m) for i in range(len(tour) - 1))
print(f"Overall Total Travel Cost: {overall_cost}")