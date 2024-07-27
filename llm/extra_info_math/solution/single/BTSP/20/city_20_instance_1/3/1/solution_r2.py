from mip import Model, xsum, BINARY, minimize, OptimizationStatus
import math

# City coordinates
coords = [
    (14, 77), # Depot city 0
    (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28),
    (27, 45), (90, 85), (98, 76), (6, 19),
    (26, 29), (21, 79), (49, 23), (78, 76),
    (68, 45), (50, 28), (69, 9)
]

n = len(coords)

# Calculate Euclidean distances between each pair of points
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

dist = [[calc_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Create a new model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] if i != j else [0]*n for i in range(n)]
max_dist = model.add_var()

# Objective is to minimize the maximum distance traveled between two consecutive cities
model.objective = minimize(max_dist)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Maximin distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += dist[i][j] * x[i][j] <= max_dist

# Sub-tour elimination using Miller-Tucker-Zemlin (MTZ) Constraints
u = [model.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * x[i][j] <= n - 2

# Optimize model
status = model.optimize(max_seconds=300)

if status == OptimizationStatus.OPTIMAL or status == Optimization sulution:
    tour = []
    current = 0
    for _ in range(n):
        tour.append(current)
        next_cities = [j for j in range(n) if x[current][j].x > 0.9 and j != current]
        if next_cities:
            current = next_cities[0]
    tour.append(0)  # Return to the depot
    
    total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("The problem did not find an optimal solution within the time limit.")