import math
from mip import Model, xsum, minimize, BINARY, INTEGER

# Define the cities and their coordinates
cities = [
    (30, 40),  # Depot
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Helper function to calculate Euclidean distance
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

n = len(cities)  # Total cities including depot
m = 2  # Number of robots

dist = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

model = Model()

# x[i, j, k] is a binary variable: 1 if salesman k travels from city i to city j
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)] 

# u[i] is a continuous variable that represents the sequence in which city i is visited
u = [model.add_var(var_type=INTEGER, lb=0) for i in range(n)]

# Objective: Minimize the total distance traveled by all salesmen
model.objective = minimize(xsum(dist[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m)))

# Constraints

# Every city must be visited exactly once by exactly one salesman
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Salesman must leave and enter the depot
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[i][0][k] for i in range(1, n)) == 1

# Every city must be entered and left once
for k in range(m):
    for j in range(1, n):
        model += xsum(x[i][j][k] for i in range(n) if i != j) == xsum(x[j][i][k] for i in range(n) if i != j)

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n - 1) * x[i][j][k] <= n - 2

model.optimize()

# Extract tours from the variables
tours = {k: [] for k in range(m)}
for k in range(m):
    tour = [0]
    while True:
        next_city = None
        for j in range(n):
            if x[tour[-1]][j][k].x >= 0.99 and j not in tour:
                next_city = j
                tour.append(next_city)
                break
        if next_city == 0:
            break
    tours[k] = tour

# Calculate and display the results
for k in tours:
    print(f"Robot {k} Tour: {tours[k]}")
    tour_cost = sum(dist[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

overall_cost = sum(sum(dist[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1)) for k in tours)
print(f"Overall Total Travel Cost: {overall_cost}")