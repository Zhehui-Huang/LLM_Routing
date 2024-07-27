from math import sqrt
from mip import Model, xsum, minimize, BINARY, INTEGER

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

n = len(cities)
dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Number of robots and depot
m = 8
depot = 0

# Model setup
model = Model()

# Variables: x[i,j] is 1 if travel from i to j
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
# Subtour prevention auxiliary variables
u = [model.add_var(var_type=INTEGER, lb=0) for i in range(n)]

# Objective: minimize total travel cost
model.objective = minimize(xsum(dist[i][j] * x[i][j] for i in range(n) for j in range(n)))

# Constraints
# Departure and arrival from the depot
model += xsum(x[depot][j] for j in range(n) if j != depot) == m
model += xsum(x[i][depot] for i in range(n) if i != depot) == m

# Each city is visited exactly once
for j in range(1, n):
    model += xsum(x[i][j] for i in range(n) if i != j) == 1
    model += xsum(x[j][i] for i in range(n) if i != j) == 1

# Subtour elimination constraints
for i in range(n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the problem
model.optimize()

# Extract tours
tours = []
for i in range(n):
    for j in range(n):
        if x[i][j].x >= 0.99 and i != j:
            tours.append((i, j))

# Organize tours starting from the depot
def find_tour(start, tours):
    current = start
    tour = [current]
    while True:
        next_steps = [t for t in tours if t[0] == current]
        if not next_steps:
            break
        next_step = next_steps[0]
        next_city = next_step[1]
        tour.append(next_city)
        current = next_city
        if next_city == start:
            break
    return tour

# Calculate and display results
total_cost = 0
robot_tours = [find_tour(depot, tours)]
for index, tour in enumerate(robot_tours):
    tour_cost = sum(dist[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)-1))
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")