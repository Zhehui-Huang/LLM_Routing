import math
from itertools import combinations
from mip import Model, xsum, minimize, BINARY, INTEGER, OptimizationStatus

# City coordinates
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of Cities
n = len(coords)

# Distance calculation using Euclidean distance
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# Create a model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
d = model.add_var()

# Objective: minimize the maximum distance d
model.objective = minimize(d)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination using lazy constraints or SECs (classical approach)
for S in range(3, n+1):
    for subset in combinations(range(1, n), S):
        model += xsum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i][j] * distance(i, j) <= d

# Solve the model
status = model.optimize()

# Extract and print the results appropriately
if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:
    path = []
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                path.append((i, j))

    # Determining the tour from depot
    tour = [0]
    while len(tour) < n:
        next_city = [j for i, j in path if i == tour[-1]][0]
        tour.append(next_city)

    tour.append(0)  # complete the loop back to depot
    
    max_distance_in_tour = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    total_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance_in_tour}")
else:
    print("No feasible solution found.")