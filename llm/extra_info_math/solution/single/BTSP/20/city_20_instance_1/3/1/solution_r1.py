from mip import Model, xsum, minimize, BINARY
import math

# City coordinates
coords = [
    (14, 77), # Depot city
    (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28),
    (27, 45), (90, 85), (98, 76), (6, 19),
    (26, 29), (21, 79), (49, 23), (78, 76),
    (68, 45), (50, 28), (69, 9)
]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coords)
dist = [[distance(coords[i], coords[j]) for j in range(n)] if i != j else [0]*n for i in range(n)]

# Model
m = Model()

# Variables
x = [[m.add_var(var_type=BINARY) for j in range(n)] if i != j else [0]*n for i in range(n)]
max_dist = m.add_var()

# Objective
m.objective = minimize(max_dist)

# Constraints
# Each city needs to be left and entered exactly once
for i in range(n):
    m += xsum(x[i][j] for j in range(n) if i != j) == 1
    m += xsum(x[j][i] for j in range(n) if i != j) == 1

# Maximum distance between any two consecutive cities
for i in range(n):
    for j in range(n):
        if i != j:
            m += x[i][j] * dist[i][j] <= max_dist

# Eliminate subtours
u = [m.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            m += u[i] - u[j] + n*x[i][j] <= n-1

# Solving the model
m.optimize(max_seconds=300)

# Retrieving the solution
tour = []
if m.num_solutions:
    current = 0
    visited = [False]*n
    visited[0] = True
    for _ in range(n):
        tour.append(current)
        next_cities = [j for j in range(n) if j != current and x[current][j].x >= 0.99]
        if next_cities:
            next_city = next_cities[0]
            visited[next_city] = True
            current = next_city

    tour.append(tour[0]) # To complete the loop back to the depot

    total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No solution found within the time limit")